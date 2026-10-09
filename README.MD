1. Introduction

Digital technology plays an important role in addressing problems affecting communities, including challenges in healthcare, education, agriculture, and public administration. When properly designed, digital solutions can help people organize information, improve access to services, and use available resources more effectively.

However, developing a digital solution involves more than writing code. Developers must also consider accessibility, privacy, security, transparency, reusability, and the potential benefits to the public.

The Patient Record Management System is a Python-based application developed as an educational prototype to demonstrate how technology can help organize basic patient information within a community healthcare setting.

The system uses Object-Oriented Programming (OOP) to organize patients, doctors, and patient records into separate classes. It allows users to add patient records, display stored information, search for a patient using a unique identification number, update a recorded condition, assign patients to a doctor, and count the total number of patients.

The project also considers selected principles associated with Digital Public Goods. These include open-source sharing, accessibility, modularity, privacy awareness, and documentation.

The Digital Public Goods Alliance provides a standard for evaluating digital solutions that seek recognition as Digital Public Goods. Although this project demonstrates some relevant principles, it has not undergone an official assessment or received DPG recognition.

Reference: Digital Public Goods Alliance — Digital Public Goods Standard

2.0 Community Problem Statement

In many communities, health workers need to maintain information about patients who visit local health facilities. Such information may include patient identification numbers, names, ages, and details recorded during visits.

When information is managed entirely through paper-based records, locating a particular patient's file can take time. Updating information may also become difficult when records are disorganized or stored in different locations.

These challenges demonstrate the potential value of a simple digital record-management system.

For this project, I assume the role of a developer working to address this community problem by creating a basic application that demonstrates how patient records can be organized electronically.

The application uses sample records for the following patients:

Kemoh Wisdom Conteh
Bernard Boyce Johnson
Franklina Lil

It also includes a doctor, Amadu Amkam Kamara, who can be assigned patients within the demonstration.

The application is intended to demonstrate record-management functionality. It does not establish that a digital system will automatically eliminate errors or improve healthcare outcomes, and it is not ready for use with real patient information.

3.0 Aim of the Project

The aim of this project is to develop a simple Python-based Patient Record Management System that demonstrates how Object-Oriented Programming and basic data structures can support the organization of community healthcare records while considering relevant Digital Public Goods principles.

4.0 Project Objectives

The specific objectives are to:

Develop a Patient class for storing and managing basic patient information.
Develop a Doctor class for storing doctor information and managing assigned patients.
Develop a PatientRecordSystem class for organizing patient records.
Use Python lists to store multiple patient objects.
Implement methods for adding, displaying, searching, updating, and counting patient records.
Demonstrate the use of a class method decorated with @classmethod.
Explain how the system could support a community healthcare information-management problem.
Demonstrate openness, modularity, accessibility, and privacy awareness.
Identify the limitations and improvements required before the system could be considered for practical healthcare use.
5.0 Overview of the Proposed Solution

The proposed solution is a simple patient record application developed using Python.

It contains three principal classes.

Class	Purpose
Patient	Stores patient information and provides methods to display and update it.
Doctor	Stores doctor information and provides a method for assigning patients.
PatientRecordSystem	Manages the collection of patient objects, including adding, searching, displaying, and counting records.

The application stores patient objects in a Python list. When the program starts, it creates the record-system object using the create_system() class method.

The main program then creates three patient objects and one doctor object.

The system demonstrates how patient records can be added, displayed, searched, and updated.

This design provides the foundation for discussing how a community-oriented digital solution could be developed with openness, accessibility, modularity, and privacy in mind.

6.0 How the Solution Aligns with the DPG Standard
6.1 Open-Source Software and Transparency
Meaning

Open-source software makes its source code available under a licence that permits activities such as studying, using, modifying, and redistributing the software according to that licence.

Openness can allow developers to examine how a system works, identify problems, learn from its design, and contribute improvements.

Application to this project

The Patient Record Management System is written in Python. Its source code can be published in a GitHub repository together with the README file and project report.

Making the source code available can allow other students and developers to:

Understand how the application works.
Study its classes and methods.
Reuse permitted parts of the code.
Suggest improvements.
Adapt the design for other educational record-management projects.

For example, a student developing a school attendance system could study the separation of responsibilities between the classes and apply similar OOP principles to that project.

Evidence from the project

The following elements can support openness and transparency:

patient_record_system.py
README.md
Project documentation
Testing documentation
An appropriate open-source licence
Limitation

Uploading code to GitHub does not automatically make a project open source. A suitable licence must be included.

Furthermore, publishing code does not automatically mean that the application meets every requirement of the DPG Standard.

Recommendation

The project should be published with an appropriate open-source licence, such as the MIT Licence if suitable for the assignment. The repository should also include clear documentation explaining the purpose, setup, functionality, and limitations of the program.

6.2 Accessibility and Inclusion
Meaning

Accessibility and inclusion involve designing digital systems so that people with different abilities, technical knowledge, and circumstances can use them.

A public-interest digital solution should consider whether its intended users can access and understand the system.

Application to this project

The Patient Record Management System uses basic Python syntax and a straightforward text-based interface.

The program does not require a paid specialist application to run. A user with a compatible computer and Python installation can execute the program.

Its output is also relatively easy to understand because it uses descriptive labels, including:

Patient ID
Name
Age
Gender
Medical Condition

This approach can make the prototype easier for students and beginner programmers to understand.

Example

When the program displays a patient record, the output is organized into clearly labelled fields.

This is easier to interpret than displaying an unexplained sequence of values.

Limitation

A simple text interface does not automatically make a program accessible to everyone.

The current prototype does not include a graphical interface, local-language support, or formal accessibility testing.

Recommendation

Future versions could include:

Clear menus and navigation.
Helpful error messages.
Readable output.
Support for appropriate local languages.
Accessibility testing with users who have different needs.

These improvements would help establish whether the system is genuinely usable by its intended audience.

6.3 Privacy and Data Protection
Meaning

Privacy is particularly important in healthcare because patient records may contain sensitive personal information.

A responsible digital solution should protect confidential information from unauthorized access, disclosure, alteration, or misuse.

Application to this project

The program stores patient information in objects and displays it when requested.

For this assignment, the records should be treated as demonstration data.

The project documentation acknowledges that personal medical information should not be published in a public GitHub repository without an appropriate legal basis and suitable safeguards.

This consideration is important because making software open source does not mean making its users' private information public.

The source code can be open while patient records remain private.

For example, other developers may be allowed to inspect the program's code without being permitted to access confidential patient information.

Limitation

The current program does not implement:

User authentication.
Role-based access controls.
Encryption.
Audit logs.
Secure database storage.
Secure backup and recovery.
Data-retention and deletion procedures.

Consequently, it should not be used to store real patient records.

Recommendation

Before any real-world healthcare deployment, the application would require a privacy and security assessment.

Appropriate safeguards would need to be implemented, including authentication, authorization, secure storage, audit logging, and suitable procedures for handling patient information.

The system would also need to comply with applicable data-protection and healthcare requirements.

For this academic assignment, sample data should be used instead.

6.4 Modularity and Reusability
Meaning

Modularity involves dividing a program into separate components, each with a clear responsibility.

Reusability means that software components can be used or adapted for other purposes without rebuilding everything from the beginning.

These qualities can make software easier to understand, maintain, test, and improve.

Application to this project

The program contains three separate classes.

The Patient class

This class represents an individual patient.

It stores attributes such as:

patient_id
name
age
gender
condition

Its methods include display_info() and update_condition().

The Doctor class

This class represents a doctor.

It stores the doctor's ID, name, specialization, and a list of assigned patients.

Its assign_patient() method associates a patient object with the doctor.

The PatientRecordSystem class

This class manages patient records.

Its methods include:

add_patient()
display_patients()
find_patient()
patient_count()
create_system()
Example of reusability

Suppose another student wants to develop a small school health-record application.

That student could study the Patient class and adapt its structure to represent students' basic health records.

The student could also develop new classes without necessarily rewriting every component of the original program.

Limitation

The current program is a small, single-file prototype. It stores data in memory and loses those records when the program ends.

It also lacks automated tests and a separate database layer.

Recommendation

Future versions could introduce a database, automated tests, and separate Python modules as the project grows.

These improvements would make the application easier to extend and maintain.

6.5 Public Benefit and Community Relevance
Meaning

Digital solutions intended for the public good should address a relevant need and provide a credible potential benefit to their intended users.

Application to this project

The selected problem concerns the organization of community healthcare records.

The prototype demonstrates several operations that could be useful in a record-management application:

Adding patient records.
Displaying stored records.
Searching by patient ID.
Updating a recorded condition.
Assigning patients to a doctor.
Counting the number of stored patients.

For example, the find_patient() method demonstrates how the system can search for patient ID P002 rather than requiring the user to inspect every record manually.

The program therefore illustrates how a digital approach could help organize information.

Limitation

The current program has not been evaluated in an actual healthcare setting.

It does not demonstrate that it reduces waiting times, prevents medical errors, or improves patient outcomes.

Recommendation

A future version could be evaluated through controlled usability testing with appropriate participants. Any real-world trial involving health information would require suitable approvals and privacy protections.

6.6 Documentation and Transparency
Meaning

Documentation explains how software works, how to run it, what it can do, and what limitations users should understand.

Clear documentation helps others reproduce, inspect, maintain, and improve a project.

Application to this project

The project includes a README file and a report explaining its purpose, design, classes, methods, and DPG-related considerations.

The documentation can also provide instructions for running the program and explain its limitations.

This makes it easier for a lecturer, student, or developer to understand the project without having to interpret the entire source code independently.

Recommendation

The documentation should be kept consistent with the actual program.

Testing results should reflect tests that have genuinely been performed, and screenshots should come from the student's own execution of the program.

7.0 Connection Between the Python Requirements and DPG Principles

The assignment's programming requirements contribute to the implementation, but they should not be confused with formal DPG eligibility requirements.

Assignment requirement	Implementation	Relevance to DPG principles
OOP classes	Patient, Doctor, PatientRecordSystem	Supports modularity and understandability.
Objects	Three patient objects and one doctor object	Demonstrates how real-world entities can be represented digitally.
Python lists	self.patients and self.assigned_patients	Demonstrates basic organization of multiple records.
Instance methods	add_patient(), display_info(), update_condition()	Separates operations into understandable and reusable methods.
Searching	find_patient()	Demonstrates how a record can be located using an ID.
Class method	create_system()	Demonstrates the required OOP concept, although a class method is not itself a DPG requirement.
GitHub	Repository containing code and documentation	Can support openness and transparency when appropriately licensed.
README and report	Instructions, design explanation, limitations	Supports transparency and reproducibility.
Privacy awareness	Sample data and explanation of security limitations	Demonstrates responsible consideration of sensitive information.

This table shows that the assignment's programming features provide the technical foundation for the prototype, while the DPG discussion addresses the wider principles that should guide its development and use.

8.0 Testing and Evaluation

The program should be tested to establish whether its main functions operate as intended.

The following table identifies the tests that should be performed.

Test ID	Function	Test procedure	Expected result
T01	System creation	Call PatientRecordSystem.create_system()	A system object is created.
T02	Add patients	Add the three patient objects	Three records are stored.
T03	Display records	Call display_patients()	All stored patient records are displayed.
T04	Search	Search for P002	The matching patient record is returned.
T05	Search failure	Search for a nonexistent ID	The program returns None and displays the not-found message in the main program.
T06	Update condition	Call update_condition()	The stored condition changes.
T07	Assign patient	Call assign_patient()	The patient is added to the doctor's assigned-patient list.
T08	Count records	Call patient_count()	The program returns the number of stored patients.

Note: These are planned test cases and expected results. Actual results should be recorded after running the tests.

Testing is important because a program's intended design does not guarantee that every function will work correctly in all situations.

9.0 Limitations of the Proposed Solution

Although the prototype demonstrates important programming concepts, it has several limitations.

First, the application stores records in memory rather than a permanent database. When the program closes, the records are lost.

Second, the system does not have authentication or role-based access controls. It cannot distinguish an authorized healthcare worker from another person using the application.

Third, it does not encrypt patient records or provide an audit trail of changes.

Fourth, the system does not validate the accuracy of medical information.

Finally, the application has not been assessed for compliance with healthcare regulations or the complete DPG Standard.

These limitations mean that the system should remain an educational prototype until the necessary technical, legal, privacy, and usability requirements have been addressed.

10.0 Recommendations

Based on the analysis, the following improvements are recommended:

Introduce database storage. A database such as SQLite could provide persistent storage for a more advanced prototype.
Implement access controls. A future version should distinguish authorized users and restrict access according to their responsibilities.
Strengthen privacy and security. Any real-world version would require an appropriate security design, secure storage, access logging, and data-protection procedures.
Improve accessibility. Clear menus, understandable messages, and appropriate language options should be considered.
Add automated testing. Tests should check the expected behavior of each class and method.
Publish appropriate documentation. The README and report should accurately explain the system's functions, setup instructions, and limitations.
Use an appropriate open-source licence. If the project is to be shared as open-source software, the repository should contain a licence that clearly establishes permitted reuse.
Conduct further assessment. Before real-world deployment, the application would require technical, privacy, accessibility, and regulatory review.
Avoid claims of certification. The project should be described as demonstrating selected DPG principles rather than as an officially recognized Digital Public Good.
11.0 Conclusion

The Patient Record Management System demonstrates how Python and Object-Oriented Programming can be used to develop a simple digital solution for a community healthcare record-management problem.

The Patient, Doctor, and PatientRecordSystem classes organize the program into understandable components. Python lists store multiple patient objects, while instance methods provide basic record-management functions. The class method demonstrates an additional OOP concept required by the assignment.

The project also illustrates how openness, accessibility, modularity, documentation, and privacy awareness can influence the design of a digital solution intended to address a public problem.

Publishing the source code with an appropriate open-source licence could allow others to study and adapt the program. Clear documentation could support transparency, while the use of sample data and discussion of security limitations demonstrate awareness of patient privacy.

However, the current prototype lacks important features required for real healthcare use, including persistent storage, authentication, and appropriate technical security controls. It has also not undergone formal assessment against the DPG Standard.

Therefore, the project demonstrates selected principles associated with Digital Public Goods, but it should not be described as an officially certified Digital Public Good.

The project provides a foundation for further learning and development, showing that a responsible digital solution should consider not only whether its code works, but also whether it can be understood, reused, accessed, and operated safely.



