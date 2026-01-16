import tkinter as tk
from tkinter import ttk, messagebox
from core.hospital_manager import HospitalManager


class HospitalGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("900x600")
        
        self.manager = HospitalManager()
        
        # Auto-save on window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create all tabs
        self.create_department_tab()
        self.create_patient_tab()
        self.create_staff_tab()
        self.create_view_tab()
    
    def create_department_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Departments")
        
        tk.Label(tab, text="Department Management", font=('Arial', 14, 'bold')).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text="Add Department", padding=20)
        frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(frame, text="Department Name:").grid(row=0, column=0, sticky='w', pady=5)
        self.dept_name = tk.Entry(frame, width=40)
        self.dept_name.grid(row=0, column=1, padx=10)
        
        ttk.Button(frame, text="Add Department", command=self.add_department).grid(row=1, column=1, pady=10)
        
        list_frame = ttk.LabelFrame(tab, text="All Departments", padding=20)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.dept_listbox = tk.Listbox(list_frame, font=('Arial', 10), height=15)
        self.dept_listbox.pack(fill='both', expand=True)
        
        ttk.Button(tab, text="Refresh", command=self.refresh_departments).pack(pady=5)
        
        self.refresh_departments()
    
    def create_patient_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Patients")
        
        tk.Label(tab, text="Patient Management", font=('Arial', 14, 'bold')).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text="Add Patient", padding=20)
        frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='w', pady=5)
        self.patient_name = tk.Entry(frame, width=40)
        self.patient_name.grid(row=0, column=1, padx=10)
        
        tk.Label(frame, text="Age:").grid(row=1, column=0, sticky='w', pady=5)
        self.patient_age = tk.Entry(frame, width=40)
        self.patient_age.grid(row=1, column=1, padx=10)
        
        tk.Label(frame, text="Medical Record:").grid(row=2, column=0, sticky='w', pady=5)
        self.patient_record = tk.Entry(frame, width=40)
        self.patient_record.grid(row=2, column=1, padx=10)
        
        tk.Label(frame, text="Department (optional):").grid(row=3, column=0, sticky='w', pady=5)
        self.patient_dept = tk.Entry(frame, width=40)
        self.patient_dept.grid(row=3, column=1, padx=10)
        
        ttk.Button(frame, text="Add Patient", command=self.add_patient).grid(row=4, column=1, pady=10)
        
        remove_frame = ttk.LabelFrame(tab, text="Remove Patient", padding=20)
        remove_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(remove_frame, text="Patient ID:").grid(row=0, column=0, sticky='w', pady=5)
        self.patient_id_remove = tk.Entry(remove_frame, width=20)
        self.patient_id_remove.grid(row=0, column=1, padx=10)
        
        ttk.Button(remove_frame, text="Remove", command=self.remove_patient).grid(row=0, column=2, padx=10)
        
        list_frame = ttk.LabelFrame(tab, text="All Patients", padding=20)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.patient_listbox = tk.Listbox(list_frame, font=('Arial', 10), height=10)
        self.patient_listbox.pack(fill='both', expand=True)
        
        ttk.Button(tab, text="Refresh", command=self.refresh_patients).pack(pady=5)
        
        self.refresh_patients()
    
    def create_staff_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Staff")
        
        tk.Label(tab, text="Staff Management", font=('Arial', 14, 'bold')).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text="Add Staff", padding=20)
        frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='w', pady=5)
        self.staff_name = tk.Entry(frame, width=40)
        self.staff_name.grid(row=0, column=1, padx=10)
        
        tk.Label(frame, text="Age:").grid(row=1, column=0, sticky='w', pady=5)
        self.staff_age = tk.Entry(frame, width=40)
        self.staff_age.grid(row=1, column=1, padx=10)
        
        tk.Label(frame, text="Position:").grid(row=2, column=0, sticky='w', pady=5)
        self.staff_position = tk.Entry(frame, width=40)
        self.staff_position.grid(row=2, column=1, padx=10)
        
        tk.Label(frame, text="Department (optional):").grid(row=3, column=0, sticky='w', pady=5)
        self.staff_dept = tk.Entry(frame, width=40)
        self.staff_dept.grid(row=3, column=1, padx=10)
        
        ttk.Button(frame, text="Add Staff", command=self.add_staff).grid(row=4, column=1, pady=10)
        
        remove_frame = ttk.LabelFrame(tab, text="Remove Staff", padding=20)
        remove_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(remove_frame, text="Staff ID:").grid(row=0, column=0, sticky='w', pady=5)
        self.staff_id_remove = tk.Entry(remove_frame, width=20)
        self.staff_id_remove.grid(row=0, column=1, padx=10)
        
        ttk.Button(remove_frame, text="Remove", command=self.remove_staff).grid(row=0, column=2, padx=10)
        
        list_frame = ttk.LabelFrame(tab, text="All Staff", padding=20)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.staff_listbox = tk.Listbox(list_frame, font=('Arial', 10), height=10)
        self.staff_listbox.pack(fill='both', expand=True)
        
        ttk.Button(tab, text="Refresh", command=self.refresh_staff).pack(pady=5)
        
        self.refresh_staff()
    
    def create_view_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="View All")
        
        tk.Label(tab, text="Hospital Overview", font=('Arial', 14, 'bold')).pack(pady=10)
        
        text_frame = ttk.Frame(tab)
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.view_text = tk.Text(text_frame, font=('Arial', 10), yscrollcommand=scrollbar.set)
        self.view_text.pack(fill='both', expand=True)
        scrollbar.config(command=self.view_text.yview)
        
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Refresh All", command=self.refresh_all).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Save Data", command=self.save_data).pack(side='left', padx=5)
        
        self.refresh_all()
    
    def add_department(self):
        name = self.dept_name.get().strip()
        if name:
            self.manager.add_department(name)
            messagebox.showinfo("Success", f"Department '{name}' added!")
            self.dept_name.delete(0, tk.END)
            self.refresh_departments()
        else:
            messagebox.showwarning("Warning", "Please enter department name.")
    
    def refresh_departments(self):
        self.dept_listbox.delete(0, tk.END)
        for dept in self.manager.get_all_departments():
            self.dept_listbox.insert(tk.END, str(dept))
    
    def add_patient(self):
        name = self.patient_name.get().strip()
        age = self.patient_age.get().strip()
        record = self.patient_record.get().strip()
        dept = self.patient_dept.get().strip()
        
        if name and age:
            try:
                patient_id = self.manager.add_patient(name, int(age), record)
                if dept:
                    self.manager.assign_patient_to_department(patient_id, dept)
                messagebox.showinfo("Success", f"Patient added with ID: {patient_id}")
                self.patient_name.delete(0, tk.END)
                self.patient_age.delete(0, tk.END)
                self.patient_record.delete(0, tk.END)
                self.patient_dept.delete(0, tk.END)
                self.refresh_patients()
            except:
                messagebox.showerror("Error", "Invalid age.")
        else:
            messagebox.showwarning("Warning", "Please enter name and age.")
    
    def remove_patient(self):
        patient_id = self.patient_id_remove.get().strip()
        if patient_id:
            try:
                self.manager.remove_patient(int(patient_id))
                messagebox.showinfo("Success", "Patient removed!")
                self.patient_id_remove.delete(0, tk.END)
                self.refresh_patients()
            except:
                messagebox.showerror("Error", "Invalid ID.")
        else:
            messagebox.showwarning("Warning", "Please enter patient ID.")
    
    def refresh_patients(self):
        self.patient_listbox.delete(0, tk.END)
        for patient in self.manager.get_all_patients():
            self.patient_listbox.insert(tk.END, str(patient))
    
    def add_staff(self):
        name = self.staff_name.get().strip()
        age = self.staff_age.get().strip()
        position = self.staff_position.get().strip()
        dept = self.staff_dept.get().strip()
        
        if name and age and position:
            try:
                staff_id = self.manager.add_staff(name, int(age), position)
                if dept:
                    self.manager.assign_staff_to_department(staff_id, dept)
                messagebox.showinfo("Success", f"Staff added with ID: {staff_id}")
                self.staff_name.delete(0, tk.END)
                self.staff_age.delete(0, tk.END)
                self.staff_position.delete(0, tk.END)
                self.staff_dept.delete(0, tk.END)
                self.refresh_staff()
            except:
                messagebox.showerror("Error", "Invalid age.")
        else:
            messagebox.showwarning("Warning", "Please fill all fields.")
    
    def remove_staff(self):
        staff_id = self.staff_id_remove.get().strip()
        if staff_id:
            try:
                self.manager.remove_staff(int(staff_id))
                messagebox.showinfo("Success", "Staff removed!")
                self.staff_id_remove.delete(0, tk.END)
                self.refresh_staff()
            except:
                messagebox.showerror("Error", "Invalid ID.")
        else:
            messagebox.showwarning("Warning", "Please enter staff ID.")
    
    def refresh_staff(self):
        self.staff_listbox.delete(0, tk.END)
        for staff in self.manager.get_all_staff():
            self.staff_listbox.insert(tk.END, str(staff))
    
    def refresh_all(self):
        self.view_text.delete(1.0, tk.END)
        
        output = "="*60 + "\n"
        output += "HOSPITAL OVERVIEW\n"
        output += "="*60 + "\n\n"
        
        output += f"Hospital: {self.manager.hospital.name}\n"
        output += f"Location: {self.manager.hospital.location}\n\n"
        
        output += "DEPARTMENTS:\n"
        output += "-"*60 + "\n"
        for dept in self.manager.get_all_departments():
            output += str(dept) + "\n"
        
        output += "\nPATIENTS:\n"
        output += "-"*60 + "\n"
        for patient in self.manager.get_all_patients():
            output += str(patient) + "\n"
        
        output += "\nSTAFF:\n"
        output += "-"*60 + "\n"
        for staff in self.manager.get_all_staff():
            output += str(staff) + "\n"
        
        self.view_text.insert(1.0, output)
    
    def save_data(self):
        if self.manager.save_data():
            messagebox.showinfo("Success", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "Failed to save data!")
    
    def on_closing(self):
        """Handle window closing - auto save."""
        if messagebox.askokcancel("Quit", "Save data before closing?"):
            self.manager.save_data()
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()


def run_gui():
    """Run the GUI interface."""
    app = HospitalGUI()
    app.run()
