from modules.person import Person

class Patient(Person):
    def __init__(self, patient_id, name, email, phonenumber,dob):
        super().__init__(name, email, phonenumber,dob)
        self.patient_id = patient_id

    

    