# ==========================================================
# PATIENT RECORD MANAGEMENT SYSTEM
# Python Object-Oriented Programming Assignment
# Domain: Health
# ==========================================================

# CLASS 1: PATIENT
class Patient:
    def __init__(self, patient_id, name, age, gender, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition

    # Instance method
    def display_info(self):
        print("--------------------------------")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Medical Condition:", self.condition)

    # Instance method for updating patient condition
    def update_condition(self, new_condition):
        self.condition = new_condition
        print("Patient condition updated successfully.")

# CLASS 2: DOCTOR
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.assigned_patients = []

    # Instance method
    def display_info(self):
        print("--------------------------------")
        print("Doctor ID:", self.doctor_id)
        print("Doctor Name:", self.name)
        print("Specialization:", self.specialization)

    # Instance method for assigning a patient
    def assign_patient(self, patient):
        self.assigned_patients.append(patient)
        print(
            patient.name,
            "has been assigned to Dr.",
            self.name
        )


# CLASS 3: PATIENT RECORD SYSTEM-
class PatientRecordSystem:

    system_name = "Digital Patient Record Management System"

    def __init__(self):
        self.patients = []

    # Instance method
    def add_patient(self, patient):
        self.patients.append(patient)
        print(
            "Patient",
            patient.name,
            "was added successfully."
        )

    # Instance method
    def display_patients(self):
        print("\n===== ALL PATIENT RECORDS =====")

        if len(self.patients) == 0:
            print("No patient records available.")
            return

        for patient in self.patients:
            patient.display_info()

    # Instance method
    def find_patient(self, patient_id):

        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

        return None

    # Instance method
    def patient_count(self):
        return len(self.patients)

    # Class method
    @classmethod
    def create_system(cls):
        print("\nStarting:", cls.system_name)
        return cls()

# MAIN PROGRAM
print("==============================================")
print(" PATIENT RECORD MANAGEMENT SYSTEM")
print("==============================================")

# Create the system using the class method
system = PatientRecordSystem.create_system()

# CREATE PATIENT OBJECTS
patient1 = Patient(
    "P001",
    "Kemoh Wisdom Conteh",
    19,
    "Male",
    "Malaria"
)

patient2 = Patient(
    "P002",
    "Bernard Boyce Johnson",
    31,
    "Female",
    "Hypertension"
)

patient3 = Patient(
    "P003",
    "Franklina Lil",
    19,
    "Male",
    "Fever"
)

# ADD PATIENTS TO THE SYSTEM

system.add_patient(patient1)
system.add_patient(patient2)
system.add_patient(patient3)

# DISPLAY ALL PATIENTS
system.display_patients()

# CREATE DOCTOR OBJECT-
doctor1 = Doctor( "D001","Dr. Amadu Amkam Kamara","General Medicine")

# Display doctor information
print("\n===== DOCTOR INFORMATION =====")
doctor1.display_info()

# ASSIGN PATIENTS TO DOCTOR

doctor1.assign_patient(patient1)
doctor1.assign_patient(patient2)

# SEARCH FOR A PATIEN

print("\n===== PATIENT SEARCH =====")

search_id = "P002"

found_patient = system.find_patient(search_id)

if found_patient:
    print("Patient found:")
    found_patient.display_info()
else:
    print("Patient not found.")

# UPDATE PATIENT CONDITION

print("\n===== UPDATING PATIENT =====")

patient1.update_condition("Recovered")

patient1.display_info()

# DISPLAY TOTAL PATIENTS

print("\n===== SYSTEM STATISTICS =====")

print( "Total number of patients:", system.patient_count())

print("\nProgram completed successfully.")