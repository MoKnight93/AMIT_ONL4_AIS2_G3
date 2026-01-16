# 🏥 Hospital Management System - Complete Documentation

The **SIMPLEST** hospital management system with Console, GUI, Dashboard and **DATA PERSISTENCE**!

## 📁 Final Project Structure

```
hospital_management/
├── main.py                      # Main entry point (choose interface)
├── data/                        # Auto-created folder for data storage
│   ├── departments.csv
│   ├── patients.csv
│   ├── staff.csv
│   ├── assignments.csv
│   └── counters.csv
├── model/                       # OOP Classes
│   ├── __init__.py
│   ├── person.py
│   ├── patient.py
│   ├── staff.py
│   ├── department.py
│   └── hospital.py
├── core/                        # Business Logic
│   ├── __init__.py
│   └── hospital_manager.py     # Main manager with save/load
└── ui/                          # User Interfaces
    ├── __init__.py
    ├── console_ui.py            # Console interface
    ├── gui.py                   # Tkinter GUI
    └── dashboard.py             # Streamlit Dashboard
```

## 🚀 Complete Setup (Step-by-Step)

### Step 1: Create Project Structure

```bash
# Create main folder
mkdir hospital_management
cd hospital_management

# Create subfolders
mkdir model
mkdir core
mkdir ui
```

### Step 2: Create __init__.py Files

**For Windows (Command Prompt):**
```bash
type nul > model\__init__.py
type nul > core\__init__.py
type nul > ui\__init__.py
```

**For Mac/Linux (Terminal):**
```bash
touch model/__init__.py
touch core/__init__.py
touch ui/__init__.py
```

### Step 3: Install Dependencies

```bash
pip install streamlit pandas plotly
```

### Step 4: Create All Python Files

Copy code from the artifact above to create these files:

#### 📄 model/person.py
```python
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
```

#### 📄 model/patient.py
```python
from model.person import Person

class Patient(Person):
    """Patient class."""
    
    def __init__(self, name, age, medical_record=""):
        super().__init__(name, age)
        self.medical_record = medical_record
    
    def __str__(self):
        return f"Patient ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Record: {self.medical_record}"
```

#### 📄 model/staff.py
```python
from model.person import Person

class Staff(Person):
    """Staff class."""
    
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def __str__(self):
        return f"Staff ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Position: {self.position}"
```

#### 📄 model/department.py
```python
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
```

#### 📄 model/hospital.py
```python
class Hospital:
    """Hospital class."""
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)
```

#### 📄 core/hospital_manager.py
**Copy from artifact** - Contains all business logic + save/load methods

#### 📄 ui/console_ui.py
**Copy from artifact** - Contains console interface

#### 📄 ui/gui.py
**Copy from artifact** - Contains Tkinter GUI

#### 📄 ui/dashboard.py
**Copy from artifact** - Contains Streamlit dashboard

#### 📄 main.py
**Copy from artifact** - Main entry point

## ▶️ How to Run

### Method 1: Using main.py (Easiest)
```bash
python main.py
```
Then choose:
- 1 = Console interface
- 2 = GUI interface
- 3 = Instructions for dashboard

### Method 2: Run Console Directly
```bash
python -c "from ui.console_ui import run_console; run_console()"
```

### Method 3: Run GUI Directly
```bash
python -c "from ui.gui import run_gui; run_gui()"
```

### Method 4: Run Dashboard
```bash
streamlit run ui/dashboard.py
```

## 💾 Data Persistence Features

### ✅ AUTO-SAVE & AUTO-LOAD:
- Data **automatically loads** when you start any interface
- Console: Auto-saves on exit (option 12)
- GUI: Auto-saves when closing window (asks confirmation)
- Dashboard: Manual save button in sidebar
- All data saved to `data/` folder in CSV files

### 📂 Data Files Created:
1. **departments.csv** - All departments
2. **patients.csv** - All patients
3. **staff.csv** - All staff
4. **assignments.csv** - Department assignments
5. **counters.csv** - ID counters (maintains ID sequence)

### 🔄 How It Works:
```
START → Load data from CSV files
  ↓
WORK → Add/modify/remove data
  ↓
SAVE → Write to CSV files
  ↓
EXIT → Data persists!
  ↓
RESTART → Data loads automatically!
```

## 📖 Usage Examples

### Example 1: First Time Use
```bash
python main.py
# Choose 1 (Console)
# 1. Add Department "Cardiology"
# 2. Add Patient "John Doe" age 45
# 3. Add Staff "Dr. Smith" position "Doctor"
# 7. Assign Patient ID 1 to "Cardiology"
# 8. Assign Staff ID 1 to "Cardiology"
# 11. Save Data
# 12. Exit
```

### Example 2: Second Time (Data Loads!)
```bash
python main.py
# Choose 1 (Console)
# "Data loaded successfully!" appears
# 4. View All Departments (shows Cardiology!)
# 5. View All Patients (shows John Doe!)
# 6. View All Staff (shows Dr. Smith!)
```

### Example 3: Using GUI
```bash
python main.py
# Choose 2 (GUI)
# Window opens with existing data loaded
# Add more data using tabs
# Click "Save Data" button
# Close window (auto-save confirmation)
```

### Example 4: Using Dashboard
```bash
streamlit run ui/dashboard.py
# Browser opens
# All existing data loaded
# Add data in any page
# Click "💾 Save Data" in sidebar
# Charts update automatically!
```

## ✅ Complete Features List

### Core Features:
- ✅ Add/Remove Departments
- ✅ Add/Remove Patients
- ✅ Add/Remove Staff
- ✅ Assign to Departments
- ✅ View All Data

### Data Persistence:
- ✅ **Save data to CSV files**
- ✅ **Load data automatically on startup**
- ✅ **Maintain ID counters across sessions**
- ✅ **Preserve all relationships**

### User Interfaces:
- ✅ Console (text-based, simple)
- ✅ GUI (desktop app with tabs)
- ✅ Dashboard (web-based with charts)

### Dashboard Features:
- ✅ Live statistics cards
- ✅ Bar charts (patients/staff per department)
- ✅ Pie charts (distribution)
- ✅ Age distribution histogram
- ✅ Position breakdown chart
- ✅ Interactive tables

## 🎯 Key Improvements in Final Version

### ✅ Checked & Fixed:
1. **main.py** - Now only entry point, no business logic
2. **core/hospital_manager.py** - Contains ALL business logic + save/load
3. **ui folder** - All UI files in ui/ folder
4. **Imports** - All imports checked and correct
5. **Data persistence** - Save/load implemented
6. **Auto-load** - Data loads on startup
7. **Simplest code** - Clean and simple
8. **Documentation** - Complete README

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'model'"
**Solution:** 
- Make sure you're in the `hospital_management` folder when running
- Check that `__init__.py` files exist in all folders

### Issue: "No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit pandas plotly
```

### Issue: Data not loading
**Solution:**
- Check that `data/` folder exists
- Check that CSV files are in `data/` folder
- Check file permissions

### Issue: Tkinter not working
**Solution:**
- **Windows:** Usually pre-installed
- **Mac:** Usually pre-installed
- **Linux:** Run `sudo apt-get install python3-tk`

## 📊 File Size Reference

Approximate lines of code:
- model/ files: ~100 lines total
- core/hospital_manager.py: ~300 lines (with save/load)
- ui/console_ui.py: ~150 lines
- ui/gui.py: ~300 lines
- ui/dashboard.py: ~250 lines
- main.py: ~30 lines

**Total: ~1,130 lines of simple, clean code!**

## 🎓 What You Learn

### OOP Concepts:
- ✅ **Inheritance** (Patient/Staff inherit from Person)
- ✅ **Encapsulation** (Each class manages its data)
- ✅ **Composition** (Hospital has Departments)
- ✅ **Abstraction** (Simple interfaces hide complexity)

### Python Skills:
- ✅ File I/O (CSV read/write)
- ✅ Module imports
- ✅ Project structure
- ✅ Error handling
- ✅ GUI development (Tkinter)
- ✅ Web apps (Streamlit)
- ✅ Data visualization (Plotly)

## 📝 Quick Start Checklist

- [ ] Created `hospital_management/` folder
- [ ] Created `model/`, `core/`, `ui/` folders
- [ ] Created all `__init__.py` files
- [ ] Installed streamlit, pandas, plotly
- [ ] Copied all model files (5 files)
- [ ] Copied `core/hospital_manager.py`
- [ ] Copied all ui files (3 files)
- [ ] Copied `main.py`
- [ ] Tested: `python main.py`
- [ ] Tested: Console interface works
- [ ] Tested: GUI interface works
- [ ] Tested: Data saves and loads
- [ ] Tested: Dashboard works

## 🎉 You're Done!

Your hospital management system is complete with:
- ✅ Clean OOP structure
- ✅ 3 user interfaces
- ✅ Data persistence (save/load)
- ✅ Professional organization
- ✅ Beautiful charts
- ✅ Simple & maintainable code

**Start using it now:**
```bash
python main.py
```

---

**Need help?** Check that:
1. All files are in correct folders
2. All `__init__.py` files exist
3. You're running from `hospital_management/` folder
4. Dependencies are installed

**Happy Hospital Managing! 🏥**
