from modules.person import Person
class Patient(Person):
    def __init__(self, patient_id, name, email, phonenumber,dob):
        super().__init__(name, email, phonenumber,dob)
        self.patient_id = patient_id

    

    def display(self):
        def display(self):
            print (f"Patient ID : {self.patient_id}")
            print (f"Name : {self.patient_id}")
            print (f"Email : {self.patient_id}")
            print (f" : {self.patient_id}")
            print (f"Patient ID : {self.patient_id}")

        