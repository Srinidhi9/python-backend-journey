students = []


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == name:
            new_marks = int(input("Enter new marks: "))
            student["marks"] = new_marks
            print("Student updated.")
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")


def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


menu()