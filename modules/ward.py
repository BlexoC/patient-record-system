class Ward:
    def __init__(self,ward_id,ward_name, doctor_name,capacity):
        self.ward_hey =ward_id
        self.ward_name =ward_name
        self.doctor_name = doctor_name
        self.capacity = capacity

    def is_full(self, administerd_count):
        return administerd_count >= self.capacity
    
    def display(self, administerd_count=None):
        print(f"Ward ID : {self.ward_id}")
        print(f"Ward Name : {self.ward_name}")
        print(f"Doctor Name : {self.doctor_name}")
        print(f"Capacity : {self.capacity} patients")
        if administerd_count is not None:
            available =self.capacity - administerd_count
            print(f"Available : {available} slot (s)")

    def to_dict (self):
        return {
            "ward_id" : self.ward_id,
            "ward_name" : self.ward_name,
            "doctor_name" : self.doctor_name,
            "capacity" : self.capacity
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            ward_id = data["ward_id"],
            ward_name = data["ward_name"],
            doctor_name = data["doctor_name"],
            capacity = int(data ["capacity"])
        )
        
# ward cannot be accessed test


        