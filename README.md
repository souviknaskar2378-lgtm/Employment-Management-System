🏢 Employment Management System


📌 Overview

The Employment Management System is a Python-based application developed to manage and maintain employee information efficiently. It helps organizations simplify employee administration by providing a centralized system to store, update, view, and manage employee records.

The system reduces manual paperwork, improves data organization, and makes employee management easier and more efficient.

✨ Features
Add Employee: Add new employee details to the system.
View Employees: Display all registered employee information.
Update Employee: Modify existing employee details.
Delete Employee: Remove employee records from the system.
Search Employee: Search for employees using their ID or name.
Department Management: Manage employee department information.
Salary Management: Store and manage employee salary details.
Attendance Management: Maintain employee attendance records.
Data Storage: Store employee information in a database.
🛠️ Technologies Used
Programming Language: Python
Database: SQLite / MySQL (depending on implementation)
Frontend: Tkinter / HTML and CSS (if applicable)
IDE: Visual Studio Code / PyCharm
Version Control: Git and GitHub
📂 Project Structure
text
Employment-Management-System/
│
├── main.py                 # Main application file
├── employee.py             # Employee management operations
├── database.py             # Database connection and operations
├── requirements.txt        # Project dependencies
├── employee.db             # Database file (if using SQLite)
├── README.md               # Project documentation
└── assets/                 # Images and other resources


Note: This is a sample structure. Modify it according to your actual project files.

⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

1. Clone the Repository
bash
git clone https://github.com/your-username/employment-management-system.git

2. Navigate to the Project Directory
bash
cd Employment-Management-System

3. Install Python

Make sure Python 3.8 or above is installed on your system.

Check your Python version:

bash
python --version

4. Install Dependencies

If your project contains a requirements.txt file, run:

bash
pip install -r requirements.txt

5. Run the Application
bash
python main.py

💻 Application Usage
Run the Python application.
Open the application interface.
Add new employee information.
View all employee records.
Update employee details when necessary.
Search for specific employees.
Delete employee records when required.
🗄️ Database Management

The application uses a database to store employee information.

Employee records may include:

Employee ID
Employee Name
Email Address
Contact Number
Gender
Address
Department
Designation
Salary
Joining Date
🔮 Future Enhancements
User authentication and login system.
Admin and employee role management.
Automated payroll management.
Leave application and approval system.
Attendance tracking.
Employee performance reports.
Export employee details to Excel and PDF.
🔒 Security

The system is designed to maintain employee information in an organized manner. Authentication, input validation, and secure database handling can be implemented to improve data protection.

🤝 Contributing

Contributions are always welcome!

Fork this repository.
Create a new branch.
Make your changes.
Commit your changes.
Push your branch.
Create a Pull Request.

Output: 
1. Main Menu

==========================================
       EMPLOYMENT MANAGEMENT SYSTEM
==========================================
1. Add Employee
2. Display All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Salary Details
7. Department-wise Employees
8. Exit
==========================================
Enter your choice:
2. Add Employee (Option 1)

Enter your choice: 1

--- Add Employee ---
Enter Employee ID: 111
Enter Name: Suman Das
Enter Department: IT
Enter Designation: Developer
Enter Salary: 45000
Enter Phone Number: 9876543220

Employee added successfully.
3. Display All Employees (Option 2)

Enter your choice: 2

--- All Employees ---
-----------------------------------------------------------------------------------------------
ID        Name                Department        Designation       Salary      Phone
-----------------------------------------------------------------------------------------------
101       Rahul Sharma        IT                Developer         ₹45000.00   9876543210
102       Priya Singh         HR                Manager           ₹55000.00   9876543211
103       Amit Kumar          Finance           Accountant        ₹35000.00   9876543212
104       Neha Gupta          IT                Tester            ₹40000.00   9876543213
105       Rohit Das           Marketing         Executive         ₹30000.00   9876543214
106       Anjali Roy          HR                Recruiter         ₹32000.00   9876543215
107       Vikash Verma        IT                Team Lead         ₹65000.00   9876543216
108       Sneha Patel         Finance           Analyst           ₹42000.00   9876543217
109       Arjun Mehta         Marketing         Manager           ₹50000.00   9876543218
110       Kavita Sen          IT                Developer         ₹48000.00   9876543219
111       Suman Das           IT                Developer         ₹45000.00   9876543220
-----------------------------------------------------------------------------------------------
4. Search Employee (Option 3)

Enter your choice: 3

--- Search Employee ---
Enter Employee ID: 101

Employee Found
Employee ID : 101
Name        : Rahul Sharma
Department  : IT
Designation : Developer
Salary      : ₹45000.0
Phone       : 9876543210
5. Update Employee (Option 4)

Enter your choice: 4

--- Update Employee ---
Enter Employee ID: 101
Press Enter to keep the existing value.

Name [Rahul Sharma]: Rahul Sharma
Department [IT]: IT
Designation [Developer]: Senior Developer
Salary [45000]: 50000
Phone [9876543210]: 9876543210

Employee updated successfully.
6. Delete Employee (Option 5)

Enter your choice: 5

--- Delete Employee ---
Enter Employee ID: 111

Employee deleted successfully.
7. Salary Details (Option 6)
After updating Rahul Sharma's salary to ₹50,000:


Enter your choice: 6

--- Salary Details ---

Total Employees       : 10
Total Salary          : ₹452000.00
Average Salary        : ₹45200.00
Highest Salary        : ₹65000.00 (Vikash Verma)
Lowest Salary         : ₹30000.00 (Rohit Das)
8. Department-wise Employees (Option 7)

Enter your choice: 7

--- Department-wise Employees ---
Enter Department: IT

Employees:
------------------------------------------------------------
ID: 101 | Name: Rahul Sharma | Designation: Senior Developer
ID: 104 | Name: Neha Gupta | Designation: Tester
ID: 107 | Name: Vikash Verma | Designation: Team Lead
ID: 110 | Name: Kavita Sen | Designation: Developer
9. Exit (Option 8)

Enter your choice: 8

Thank you for using Employment Management System!
Additional test outputs
These are some other possible outputs when testing the program.

Duplicate Employee ID


--- Add Employee ---
Enter Employee ID: 101
Employee ID already exists.
Invalid Salary


Enter Salary: abc
Invalid salary.
Negative Salary


Enter Salary: -5000
Salary cannot be negative.
Employee Not Found


--- Search Employee ---
Enter Employee ID: 999

Employee not found.
Department Not Found


--- Department-wise Employees ---
Enter Department: Sales
No employees found in this department.
Invalid Menu Choice


Enter your choice: 9
Invalid choice. Please try again.
No Employee Records


--- All Employees ---
No employee records found.

👨‍💻 Author

Team leader: Souvik Naskar
Team Members: Purushottam Kumar
              Arka mondal
              Abhrojit Biswas

GitHub:


⭐ If you find this project useful, don't forget to give it a star!

Thank you for visiting the Employment Management System project!!!!
