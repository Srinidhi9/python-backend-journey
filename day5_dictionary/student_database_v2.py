students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif choice == "2":
        name = input("Enter name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Student updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No students available.")
        else:
            for name, marks in students.items():
                print(name, "->", marks)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")