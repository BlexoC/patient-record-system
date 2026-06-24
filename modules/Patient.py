from modules.person import Person
class Patient(Person):
    def __init__(self, patient_id, name, email, phonenumber,dob):
        super().__init__(name, email, phonenumber,dob)
        self.patient_id = patient_id

    

    def display(self):
        def display(self):
            print (f"Patient ID : {self.patient_id}")
            print (f"Name : {self.name}")
            print (f"Email : {self.email}")
            print (f"PhoneNumber : {self.phonenumber}")
            print (f"Date of Birth: {self.dob}")

    def to_dict(self):
        return{
            "patient_id": self.patient_id,
            "name": self.name,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "dob": self.dob,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            patient_id=data["patient_id"],
            name = data ["name"],
            email = data ["email"],
            phonenumber = data ["phonenumber"],
            dob = data["dob"]
        )
    


        