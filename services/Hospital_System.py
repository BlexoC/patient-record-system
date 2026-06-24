import json
import os

from modules.Patient import Patient
from modules.ward import Ward
from modules.administration import Administration

PATIENT_FILE = "data/patient.json"
WARD_FILE = "data/ward.json"
ADMINISTRATION_FILE = "data/administration.json"


class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.wards = []
        self.administrations = []

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id.lower() == patient_id.lower():
                return patient
        return None

    def find_ward(self, ward_id):
        for ward in self.wards:
            if ward.ward_id.lower() == ward_id.lower():
                return ward
        return None

    def already_administered(self, patient_id, ward_id):
        for admin in self.administrations:
            if (
                admin.patient_id.lower() == patient_id.lower()
                and admin.ward_id.lower() == ward_id.lower()
            ):
                return True
        return False

    def count_enrolled(self, ward_id):
        return sum(
            1
            for admin in self.administrations
            if admin.ward_id.lower() == ward_id.lower()
        )

    def line(self):
        print("-" * 48)

    # ─── PATIENT METHODS ───────────────────────────────

    def add_patient(self):
        self.line()
        print("ADD NEW PATIENT")
        self.line()

        patient_id = input("Patient ID : ").strip()
        if not patient_id:
            print("[!] Patient ID cannot be empty.")
            return
        if self.find_patient(patient_id):
            print(f"[!] ID `{patient_id}` already exists.")
            return

        name = input("Name       : ").strip()
        if not name:
            print("[!] Name cannot be empty.")
            return

        email = input("Email      : ").strip()
        if not email or "@" not in email:
            print("[!] Enter a valid email.")
            return

        phone = input("Phone      : ").strip()
        if not phone or not phone.isdigit():
            print("[!] Enter a valid phone number.")
            return

        dob = input("Date of Birth (YYYY-MM-DD) : ").strip()
        if not dob:
            print("[!] Enter a valid date of birth.")
            return

        self.patients.append(Patient(patient_id, name, email, int(phone), dob))
        print(f"\n [✓] {name} added successfully.")

    def view_patients(self):
        self.line()
        print("ALL PATIENTS")
        self.line()

        if not self.patients:
            print("No patients found.")
            return

        for i, patient in enumerate(self.patients, 1):
            print(f"\n [{i}]")
            patient.display()

    def search_patients(self):
        self.line()
        print("SEARCH PATIENT")
        self.line()

        query = input("Enter ID or Name : ").strip().lower()
        if not query:
            print("[!] Search cannot be empty.")
            return

        results = [
            p
            for p in self.patients
            if query in p.patient_id.lower() or query in p.name.lower()
        ]

        if not results:
            print("No patients found.")
            return

        print(f"\n {len(results)} result(s) found:\n")
        for patient in results:
            patient.display()
            self.line()

    def update_patient(self):
        self.line()
        print("UPDATE PATIENT")
        self.line()

        patient_id = input("Enter Patient ID to update : ").strip()
        patient = self.find_patient(patient_id)
        if not patient:
            print(f"[!] Patient `{patient_id}` not found.")
            return

        print("Leave field blank to keep current value.\n")

        name = input(f"Name [{patient.name}] : ").strip()
        if name:
            patient.name = name

        email = input(f"Email [{patient.email}] : ").strip()
        if email:
            if "@" not in email:
                print("[!] Invalid email, keeping current.")
            else:
                patient.email = email

        phone = input(f"Phone [{patient.phonenumber}] : ").strip()
        if phone:
            if not phone.isdigit():
                print("[!] Invalid phone number, keeping current.")
            else:
                patient.phonenumber = int(phone)

        dob = input(f"Date of Birth [{patient.dob}] : ").strip()
        if dob:
            patient.dob = dob

        print(f"\n [✓] Patient `{patient_id}` updated successfully.")

    def delete_patient(self):
        self.line()
        print("DELETE PATIENT")
        self.line()

        patient_id = input("Enter Patient ID to delete : ").strip()
        patient = self.find_patient(patient_id)
        if not patient:
            print(f"[!] Patient `{patient_id}` not found.")
            return

        confirm = (
            input(f"Are you sure you want to delete {patient.name}? (yes/no) : ")
            .strip()
            .lower()
        )
        if confirm != "yes":
            print("Deletion cancelled.")
            return

        self.patients.remove(patient)
        print(f"\n [✓] Patient `{patient_id}` deleted successfully.")

    # ─── WARD METHODS ──────────────────────────────────

    def add_ward(self):
        self.line()
        print("ADD NEW WARD")
        self.line()

        ward_id = input("Ward ID   : ").strip()
        if not ward_id:
            print("[!] Ward ID cannot be empty.")
            return
        if self.find_ward(ward_id):
            print(f"[!] Ward `{ward_id}` already exists.")
            return

        ward_name = input("Ward Name : ").strip()
        if not ward_name:
            print("[!] Ward name cannot be empty.")
            return
        doctor_name = input("Doctor Name : ").strip()
        if not doctor_name:
            print("[!] Doctor name cannot be empty.")
            return

        capacity = input("Capacity  : ").strip()
        if not capacity.isdigit():
            print("[!] Capacity must be a number.")
            return

        self.wards.append(Ward(ward_id, ward_name, doctor_name, capacity))
        print(f"\n [✓] Ward `{ward_name}` added successfully.")

    def view_wards(self):
        self.line()
        print("ALL WARDS")
        self.line()

        if not self.wards:
            print("No wards found.")
            return

        for i, ward in enumerate(self.wards, 1):
            enrolled = self.count_enrolled(ward.ward_id)
            print(f"\n [{i}]")
            ward.display()
            print(f"      Enrolled : {enrolled}/{ward.capacity}")

    # ─── ADMISSION METHODS ─────────────────────────────

    def admit_patient(self):
        self.line()
        print("ADMIT PATIENT TO WARD")
        self.line()

        patient_id = input("Patient ID : ").strip()
        patient = self.find_patient(patient_id)
        if not patient:
            print(f"[!] Patient `{patient_id}` not found.")
            return

        ward_id = input("Ward ID    : ").strip()
        ward = self.find_ward(ward_id)
        if not ward:
            print(f"[!] Ward `{ward_id}` not found.")
            return

        if self.already_administered(patient_id, ward_id):
            print(
                f"[!] Patient `{patient_id}` is already admitted to ward `{ward_id}`."
            )
            return

        enrolled = self.count_enrolled(ward_id)
        if enrolled >= ward.capacity:
            print(f"[!] Ward `{ward_id}` is full.")
            return

        self.administrations.append(Administration(patient_id, ward_id))
        print(
            f"\n [✓] Patient `{patient_id}` admitted to ward `{ward_id}` successfully."
        )

    def discharge_patient(self):
        self.line()
        print("DISCHARGE PATIENT")
        self.line()

        patient_id = input("Patient ID : ").strip()
        patient = self.find_patient(patient_id)
        if not patient:
            print(f"[!] Patient `{patient_id}` not found.")
            return

        ward_id = input("Ward ID    : ").strip()
        ward = self.find_ward(ward_id)
        if not ward:
            print(f"[!] Ward `{ward_id}` not found.")
            return

        admin = None
        for a in self.administrations:
            if (
                a.patient_id.lower() == patient_id.lower()
                and a.ward_id.lower() == ward_id.lower()
            ):
                admin = a
                break

        if not admin:
            print(
                f"[!] No active admission found for patient `{patient_id}` in ward `{ward_id}`."
            )
            return

        self.administrations.remove(admin)
        print(
            f"\n [✓] Patient `{patient_id}` discharged from ward `{ward_id}` successfully."
        )

    # ─── SAVE & LOAD ───────────────────────────────────

    def save_data(self):
        os.makedirs("data", exist_ok=True)

        with open(PATIENT_FILE, "w") as f:
            json.dump([p.to_dict() for p in self.patients], f, indent=4)

        with open(WARD_FILE, "w") as f:
            json.dump([w.to_dict() for w in self.wards], f, indent=4)

        with open(ADMINISTRATION_FILE, "w") as f:
            json.dump([a.to_dict() for a in self.administrations], f, indent=4)

        print("\n [✓] Data saved successfully.")

    def load_data(self):
        if os.path.exists(PATIENT_FILE) and os.path.getsize(PATIENT_FILE) > 0:
            with open(PATIENT_FILE, "r") as f:
                self.patients = [Patient.from_dict(p) for p in json.load(f)]

        if os.path.exists(WARD_FILE) and os.path.getsize(WARD_FILE) > 0:
            with open(WARD_FILE, "r") as f:
                self.wards = [Ward.from_dict(w) for w in json.load(f)]

        if os.path.exists(ADMINISTRATION_FILE) and os.path.getsize(ADMINISTRATION_FILE) > 0:
            with open(ADMINISTRATION_FILE, "r") as f:
                self.administrations = [Administration.from_dict(a) for a in json.load(f)]
