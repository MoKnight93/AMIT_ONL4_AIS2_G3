from model.person import Person

class Staff(Person):
    """Staff class."""
    
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def __str__(self):
        return f"Staff ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Position: {self.position}"