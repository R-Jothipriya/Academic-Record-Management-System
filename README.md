📘 Academic Record Management System (CLI - Python)
----------------------------------------------------------------------------------------
Project Overview
This is a CLI-based Academic Record Management System built using Python OOP and JSON file handling.
It allows users to manage student records with full CRUD operations (Create, Read, Update, Delete) and ensures data persistence using a JSON file.

Features
➕ Add new student records
📄 Display all students
🔍 Search student by roll number
✏️ Update student marks
❌ Delete student record
💾 Persistent storage using JSON file
🧠 Object-Oriented Programming (OOP) design
🖥️ Simple command-line interface (CLI)

Technologies Used
Python 3
Object-Oriented Programming (OOP)
File Handling
JSON module

Project Structure
academic-record-system/
│
├── main.py              # Main program (CLI menu)
├── students.json        # Data storage file (auto-created)
└── README.md            # Project documentation

How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/academic-record-system.git
2. Navigate to project folder
cd academic-record-system
3. Run the program
python main.py

Menu Options
1. Add Student
2. Display Students
3. Exit
4. Search Student
5. Update Marks
6. Delete Student

Key Concepts Used
1. Object-Oriented Programming (OOP)
Class and Objects
Constructor (__init__)
Methods (display)
2. File Handling
Save data to JSON file
Load data from JSON file
3. Data Structures
List (to store students)
Dictionary (to store marks)

Data Flow
User Input → Student Object → List → JSON File
JSON File → List → Student Object → Display

Learning Outcome
This project helped in understanding:
Real-world application of OOP
File persistence using JSON
CRUD operations in Python
CLI application development
