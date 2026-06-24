from services.Hospital_System import HospitalSystem


def main():
    system = HospitalSystem()
    system.load_data()

    while True:
        print("\n" + "=" * 48)
        print("       PATIENT RECORD MANAGEMENT SYSTEM")
        print("=" * 48)
        print("  [1] Manage Patients")
        print("  [2] Manage Wards")
        print("  [3] Admissions")
        print("  [4] Save Data")
        print("  [0] Exit")
        print("=" * 48)

        choice = input("Select Option : ").strip()

        if choice == "1":
            while True:
                print("\n" + "-" * 48)
                print("         PATIENT MENU")
                print("-" * 48)
                print("  [1] Add Patient")
                print("  [2] View All Patients")
                print("  [3] Search Patient")
                print("  [4] Update Patient")
                print("  [5] Delete Patient")
                print("  [0] Back")
                print("-" * 48)

                sub = input("Select Option : ").strip()

                if sub == "1":
                    system.add_patient()
                elif sub == "2":
                    system.view_patients()
                elif sub == "3":
                    system.search_patients()
                elif sub == "4":
                    system.update_patient()
                elif sub == "5":
                    system.delete_patient()
                elif sub == "0":
                    break
                else:
                    print("[!] Invalid option, try again.")

        elif choice == "2":
            while True:
                print("\n" + "-" * 48)
                print("           WARD MENU")
                print("-" * 48)
                print("  [1] Add Ward")
                print("  [2] View All Wards")
                print("  [0] Back")
                print("-" * 48)

                sub = input("Select Option : ").strip()

                if sub == "1":
                    system.add_ward()
                elif sub == "2":
                    system.view_wards()
                elif sub == "0":
                    break
                else:
                    print("[!] Invalid option, try again.")

        elif choice == "3":
            while True:
                print("\n" + "-" * 48)
                print("         ADMISSIONS MENU")
                print("-" * 48)
                print("  [1] Admit Patient")
                print("  [2] Discharge Patient")
                print("  [0] Back")
                print("-" * 48)

                sub = input("Select Option : ").strip()

                if sub == "1":
                    system.admit_patient()
                elif sub == "2":
                    system.discharge_patient()
                elif sub == "0":
                    break
                else:
                    print("[!] Invalid option, try again.")

        elif choice == "4":
            system.save_data()

        elif choice == "0":
            system.save_data()
            print("\n [✓] Data saved. Goodbye!\n")
            break

        else:
            print("[!] Invalid option, try again.")


if __name__ == "__main__":
    main()
