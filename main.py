import json

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"\nName: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print("-" * 30)

def find_student(roll_no, students):
    for s in students:
        if s.roll_no == roll_no:
            return s
    return None

def save_students(students):
    with open("students.json", "w") as f:
        data = []

        for s in students:
            data.append({
                "name": s.name,
                "roll_no": s.roll_no,
                "marks": s.marks
            })

        json.dump(data, f, indent=4)


def load_students():
    students = []

    try:
        with open("students.json", "r") as f:
            data = json.load(f)

            for d in data:
                s = Student(d["name"], d["roll_no"], d["marks"])
                students.append(s)

    except FileNotFoundError:
        pass

    return students

students = load_students()

while True:
    print("\n===== Academic Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = int(input("Enter roll number: "))
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))

        marks = {
            "Math": math,
            "Science": science
        }

        s = Student(name, roll_no, marks)
        students.append(s)

        save_students(students)

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        roll = int(input("Enter roll number to search: "))

        student = find_student(roll, students)

        if student:
            student.display()
        else:
            print("Student not found")

    elif choice == "4":
        roll = int(input("Enter roll number to update: "))

        student = find_student(roll, students)

        if student:
            math = int(input("Enter new Math marks: "))
            science = int(input("Enter new Science marks: "))

            student.marks["Math"] = math
            student.marks["Science"] = science

            save_students(students)

            print("Marks updated successfully!")
        else:
            print("Student not found")

    elif choice == "5":
        roll = int(input("Enter roll number to delete: "))

        student = find_student(roll, students)

        if student:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
        else:
            print("Student not found")
    
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")