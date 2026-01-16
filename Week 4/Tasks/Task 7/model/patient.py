from model.person import Person

class Patient(Person):
    """Patient class."""
    
    def __init__(self, name, age, medical_record=""):
        super().__init__(name, age)
        self.medical_record = medical_record
    
    def __str__(self):
        return f"Patient ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Record: {self.medical_record}"
