import os
import csv
from model.hospital import Hospital
from model.department import Department
from model.patient import Patient
from model.staff import Staff
from model.person import Person

class HospitalManager:
    """Main manager class with data persistence."""
    
    def __init__(self, hospital_name="City Hospital", location="Main Street"):
        self.hospital = Hospital(hospital_name, location)
        self.patients = {}
        self.staff = {}
        self.data_folder = "data"
        
        # Load existing data on startup
        self.load_data()
    
    # ========== Department Operations ==========
    def add_department(self, name):
        department = Department(name)
        self.hospital.add_department(department)
        print(f"Department '{name}' added.")
        return department.department_id
    
    def get_all_departments(self):
        return self.hospital.departments
    
    def get_department_by_name(self, name):
        for dept in self.hospital.departments:
            if dept.name.lower() == name.lower():
                return dept
        return None
    
    # ========== Patient Operations ==========
    def add_patient(self, name, age, medical_record=""):
        patient = Patient(name, age, medical_record)
        self.patients[patient.person_id] = patient
        print(f"Patient added. ID: {patient.person_id}")
        return patient.person_id
    
    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient removed.")
        else:
            print("Patient not found.")
    
    def get_all_patients(self):
        return list(self.patients.values())
    
    # ========== Staff Operations ==========
    def add_staff(self, name, age, position):
        staff_member = Staff(name, age, position)
        self.staff[staff_member.person_id] = staff_member
        print(f"Staff added. ID: {staff_member.person_id}")
        return staff_member.person_id
    
    def remove_staff(self, staff_id):
        if staff_id in self.staff:
            del self.staff[staff_id]
            print("Staff removed.")
        else:
            print("Staff not found.")
    
    def get_all_staff(self):
        return list(self.staff.values())
    
    # ========== Assignment Operations ==========
    def assign_patient_to_department(self, patient_id, department_name):
        if patient_id in self.patients:
            dept = self.get_department_by_name(department_name)
            if dept:
                patient = self.patients[patient_id]
                dept.add_patient(patient)
                print(f"Patient assigned to {department_name}.")
            else:
                print("Department not found.")
        else:
            print("Patient not found.")
    
    def assign_staff_to_department(self, staff_id, department_name):
        if staff_id in self.staff:
            dept = self.get_department_by_name(department_name)
            if dept:
                staff_member = self.staff[staff_id]
                dept.add_staff(staff_member)
                print(f"Staff assigned to {department_name}.")
            else:
                print("Department not found.")
        else:
            print("Staff not found.")
    
    # ========== Data Persistence ==========
    def save_data(self):
        """Save all data to CSV files."""
        try:
            # Create data folder if not exists
            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)
            
            # Save departments
            dept_file = os.path.join(self.data_folder, "departments.csv")
            with open(dept_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['department_id', 'name'])
                for dept in self.hospital.departments:
                    writer.writerow([dept.department_id, dept.name])
            
            # Save patients
            patient_file = os.path.join(self.data_folder, "patients.csv")
            with open(patient_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['person_id', 'name', 'age', 'medical_record'])
                for patient in self.patients.values():
                    writer.writerow([patient.person_id, patient.name, patient.age, patient.medical_record])
            
            # Save staff
            staff_file = os.path.join(self.data_folder, "staff.csv")
            with open(staff_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['person_id', 'name', 'age', 'position'])
                for staff_member in self.staff.values():
                    writer.writerow([staff_member.person_id, staff_member.name, staff_member.age, staff_member.position])
            
            # Save assignments (which patient/staff is in which department)
            assign_file = os.path.join(self.data_folder, "assignments.csv")
            with open(assign_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['type', 'person_id', 'department_name'])
                for dept in self.hospital.departments:
                    for patient in dept.patients:
                        writer.writerow(['patient', patient.person_id, dept.name])
                    for staff_member in dept.staff:
                        writer.writerow(['staff', staff_member.person_id, dept.name])
            
            # Save counters
            counter_file = os.path.join(self.data_folder, "counters.csv")
            with open(counter_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['class_name', 'counter'])
                writer.writerow(['Person', Person._id_counter])
                writer.writerow(['Department', Department._id_counter])
            
            print("Data saved successfully!")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self):
        """Load data from CSV files."""
        try:
            if not os.path.exists(self.data_folder):
                return  # No data to load
            
            # Load counters first
            counter_file = os.path.join(self.data_folder, "counters.csv")
            if os.path.exists(counter_file):
                with open(counter_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row['class_name'] == 'Person':
                            Person._id_counter = int(row['counter'])
                        elif row['class_name'] == 'Department':
                            Department._id_counter = int(row['counter'])
            
            # Load departments
            dept_file = os.path.join(self.data_folder, "departments.csv")
            if os.path.exists(dept_file):
                with open(dept_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Manually set department_id to maintain consistency
                        dept = Department(row['name'])
                        dept.department_id = int(row['department_id'])
                        self.hospital.add_department(dept)
            
            # Load patients
            patient_file = os.path.join(self.data_folder, "patients.csv")
            if os.path.exists(patient_file):
                with open(patient_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        patient = Patient(row['name'], int(row['age']), row['medical_record'])
                        patient.person_id = int(row['person_id'])
                        self.patients[patient.person_id] = patient
            
            # Load staff
            staff_file = os.path.join(self.data_folder, "staff.csv")
            if os.path.exists(staff_file):
                with open(staff_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        staff_member = Staff(row['name'], int(row['age']), row['position'])
                        staff_member.person_id = int(row['person_id'])
                        self.staff[staff_member.person_id] = staff_member
            
            # Load assignments
            assign_file = os.path.join(self.data_folder, "assignments.csv")
            if os.path.exists(assign_file):
                with open(assign_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        person_id = int(row['person_id'])
                        dept_name = row['department_name']
                        
                        if row['type'] == 'patient' and person_id in self.patients:
                            self.assign_patient_to_department(person_id, dept_name)
                        elif row['type'] == 'staff' and person_id in self.staff:
                            self.assign_staff_to_department(person_id, dept_name)
            
            print("Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")