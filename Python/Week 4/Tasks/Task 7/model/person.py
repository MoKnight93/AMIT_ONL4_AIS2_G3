class Person:
    """Base class for all people."""
    _id_counter = 1
    
    def __init__(self, name, age):
        self.person_id = Person._id_counter
        Person._id_counter += 1
        self.name = name
        self.age = age
    
    def view_info(self):
        return f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}"