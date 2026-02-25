students = {}

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

students[name] = marks

print(students)


# Update marks
students = {"Srinidhi": 85}

name = input("Enter student name to update: ")

if name in students:
    new_marks = int(input("Enter new marks: "))
    students[name] = new_marks
    print("Updated:", students)
else:
    print("Student not found")

# Print all students and marks
students = {"A": 80, "B": 90, "C": 75}

for name, marks in students.items():
    print(name, "->", marks)