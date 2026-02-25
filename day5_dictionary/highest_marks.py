students = {
    "A": 80,
    "B": 95,
    "C": 88
}

highest_student = max(students, key=students.get)

print("Topper:", highest_student)
print("Marks:", students[highest_student])