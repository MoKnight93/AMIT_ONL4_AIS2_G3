from core.hospital_manager import HospitalManager

def show_menu():
    print("\n" + "="*40)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. View All Departments")
    print("5. View All Patients")
    print("6. View All Staff")
    print("7. Assign Patient to Department")
    print("8. Assign Staff to Department")
    print("9. Remove Patient")
    print("10. Remove Staff")
    print("11. Save Data")
    print("12. Exit")
    print("="*40)


def add_department(manager):
    name = input("Enter department name: ")
    manager.add_department(name)


def add_patient(manager):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    medical_record = input("Enter medical record: ")
    manager.add_patient(name, age, medical_record)


def add_staff(manager):
    name = input("Enter staff name: ")
    age = int(input("Enter staff age: "))
    position = input("Enter position: ")
    manager.add_staff(name, age, position)


def view_departments(manager):
    departments = manager.get_all_departments()
    if departments:
        for dept in departments:
            print(dept)
    else:
        print("No departments found.")


def view_patients(manager):
    patients = manager.get_all_patients()
    if patients:
        for patient in patients:
            print(patient)
    else:
        print("No patients found.")


def view_staff(manager):
    staff = manager.get_all_staff()
    if staff:
        for member in staff:
            print(member)
    else:
        print("No staff found.")


def assign_patient(manager):
    patient_id = int(input("Enter patient ID: "))
    dept_name = input("Enter department name: ")
    manager.assign_patient_to_department(patient_id, dept_name)


def assign_staff(manager):
    staff_id = int(input("Enter staff ID: "))
    dept_name = input("Enter department name: ")
    manager.assign_staff_to_department(staff_id, dept_name)


def remove_patient(manager):
    patient_id = int(input("Enter patient ID: "))
    manager.remove_patient(patient_id)


def remove_staff(manager):
    staff_id = int(input("Enter staff ID: "))
    manager.remove_staff(staff_id)


def run_console():
    """Run the console interface."""
    manager = HospitalManager()
    
    while True:
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_department(manager)
        elif choice == '2':
            add_patient(manager)
        elif choice == '3':
            add_staff(manager)
        elif choice == '4':
            view_departments(manager)
        elif choice == '5':
            view_patients(manager)
        elif choice == '6':
            view_staff(manager)
        elif choice == '7':
            assign_patient(manager)
        elif choice == '8':
            assign_staff(manager)
        elif choice == '9':
            remove_patient(manager)
        elif choice == '10':
            remove_staff(manager)
        elif choice == '11':
            manager.save_data()
        elif choice == '12':
            print("Saving data before exit...")
            manager.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
