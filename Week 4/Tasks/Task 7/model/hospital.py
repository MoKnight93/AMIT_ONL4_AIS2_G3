class Hospital:
    """Hospital class."""
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)