class Department:
    """Department class."""
    _id_counter = 1
    
    def __init__(self, name):
        self.department_id = Department._id_counter
        Department._id_counter += 1
        self.name = name
        self.patients = []
        self.staff = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def add_staff(self, staff_member):
        self.staff.append(staff_member)
    
    def __str__(self):
        return f"Department: {self.name}, Patients: {len(self.patients)}, Staff: {len(self.staff)}"