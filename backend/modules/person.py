from datetime import datetime
class Person:
    def __init__(self, name: str, email, phonenumber: int, dob):
        self.name = name
        self.email = email
        self. phonenumber = phonenumber
        self.dob = dob or datetime.now().strftime("%Y-%m-%d")