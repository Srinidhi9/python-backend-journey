from student_db import save_student, load_students


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")
        save_student(name, age, course)

    elif choice == "2":
        students = load_students()
        for student in students:
            print(student)

    elif choice == "3":
        break

    else:
        print("Invalid choice")