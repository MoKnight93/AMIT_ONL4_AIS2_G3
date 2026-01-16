import streamlit as st
import pandas as pd
import plotly.express as px
from core.hospital_manager import HospitalManager

# Page config
st.set_page_config(page_title="Hospital Dashboard", page_icon="🏥", layout="wide")

# Initialize
if 'manager' not in st.session_state:
    st.session_state.manager = HospitalManager()

manager = st.session_state.manager

# Title
st.title("🏥 Hospital Management Dashboard")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Menu")
    page = st.radio("Select", ["Dashboard", "Departments", "Patients", "Staff"])
    st.markdown("---")
    if st.button("💾 Save Data"):
        if manager.save_data():
            st.success("Data saved!")
        else:
            st.error("Error saving data!")

# ============================================================================
# DASHBOARD
# ============================================================================
if page == "Dashboard":
    st.header("📊 Overview")
    
    # Stats
    departments = manager.get_all_departments()
    patients = manager.get_all_patients()
    staff = manager.get_all_staff()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🏢 Departments", len(departments))
    col2.metric("🛏️ Patients", len(patients))
    col3.metric("👨‍⚕️ Staff", len(staff))
    
    st.markdown("---")
    
    # Charts
    if departments:
        # Prepare data
        dept_data = []
        for dept in departments:
            dept_data.append({
                'Department': dept.name,
                'Patients': len(dept.patients),
                'Staff': len(dept.staff)
            })
        df = pd.DataFrame(dept_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Patients by Department")
            fig1 = px.bar(df, x='Department', y='Patients', color='Patients')
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.subheader("Staff by Department")
            fig2 = px.bar(df, x='Department', y='Staff', color='Staff')
            st.plotly_chart(fig2, use_container_width=True)
        
        # Pie charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Patient Distribution")
            fig3 = px.pie(df, values='Patients', names='Department')
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            st.subheader("Staff Distribution")
            fig4 = px.pie(df, values='Staff', names='Department')
            st.plotly_chart(fig4, use_container_width=True)
        
        # Table
        st.subheader("📋 Department Details")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No departments. Add departments to see charts.")

# ============================================================================
# DEPARTMENTS
# ============================================================================
elif page == "Departments":
    st.header("🏢 Departments")
    
    # Add department
    with st.expander("➕ Add Department", expanded=True):
        dept_name = st.text_input("Department Name")
        if st.button("Add"):
            if dept_name:
                manager.add_department(dept_name)
                st.success(f"Added: {dept_name}")
                st.rerun()
            else:
                st.warning("Enter name")
    
    # List departments
    st.subheader("All Departments")
    departments = manager.get_all_departments()
    
    if departments:
        for dept in departments:
            st.write(f"**{dept.name}** - Patients: {len(dept.patients)}, Staff: {len(dept.staff)}")
    else:
        st.info("No departments")

# ============================================================================
# PATIENTS
# ============================================================================
elif page == "Patients":
    st.header("🛏️ Patients")
    
    # Add patient
    with st.expander("➕ Add Patient"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            age = st.number_input("Age", 0, 150, 30)
        with col2:
            record = st.text_input("Medical Record")
            departments = manager.get_all_departments()
            dept_names = [d.name for d in departments]
            dept = st.selectbox("Department", ["None"] + dept_names)
        
        if st.button("Add Patient"):
            if name:
                patient_id = manager.add_patient(name, age, record)
                if dept != "None":
                    manager.assign_patient_to_department(patient_id, dept)
                st.success(f"Added patient ID: {patient_id}")
                st.rerun()
            else:
                st.warning("Enter name")
    
    # List patients
    st.subheader("All Patients")
    patients = manager.get_all_patients()
    
    if patients:
        data = []
        for p in patients:
            data.append({
                'ID': p.person_id,
                'Name': p.name,
                'Age': p.age,
                'Record': p.medical_record
            })
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Age chart
        st.subheader("📊 Age Distribution")
        ages = [p.age for p in patients]
        fig = px.histogram(x=ages, nbins=20, title='Patient Ages')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No patients")
    
    # Remove patient
    with st.expander("🗑️ Remove Patient"):
        patient_id = st.number_input("Patient ID", 1, 1000, 1)
        if st.button("Remove"):
            manager.remove_patient(patient_id)
            st.success("Removed!")
            st.rerun()

# ============================================================================
# STAFF
# ============================================================================
elif page == "Staff":
    st.header("👨‍⚕️ Staff")
    
    # Add staff
    with st.expander("➕ Add Staff"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            age = st.number_input("Age", 18, 100, 30)
        with col2:
            position = st.selectbox("Position", ["Doctor", "Nurse", "Surgeon", "Pharmacist"])
            departments = manager.get_all_departments()
            dept_names = [d.name for d in departments]
            dept = st.selectbox("Department", ["None"] + dept_names)
        
        if st.button("Add Staff"):
            if name:
                staff_id = manager.add_staff(name, age, position)
                if dept != "None":
                    manager.assign_staff_to_department(staff_id, dept)
                st.success(f"Added staff ID: {staff_id}")
                st.rerun()
            else:
                st.warning("Enter name")
    
    # List staff
    st.subheader("All Staff")
    staff = manager.get_all_staff()
    
    if staff:
        data = []
        for s in staff:
            data.append({
                'ID': s.person_id,
                'Name': s.name,
                'Age': s.age,
                'Position': s.position
            })
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Position chart
        st.subheader("📊 Staff by Position")
        positions = {}
        for s in staff:
            positions[s.position] = positions.get(s.position, 0) + 1
        
        if positions:
            fig = px.pie(values=list(positions.values()), names=list(positions.keys()))
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No staff")
    
    # Remove staff
    with st.expander("🗑️ Remove Staff"):
        staff_id = st.number_input("Staff ID", 1, 1000, 1)
        if st.button("Remove"):
            manager.remove_staff(staff_id)
            st.success("Removed!")
            st.rerun()

# Footer
st.markdown("---")
st.caption("🏥 Hospital Management System - Data auto-loads on startup")