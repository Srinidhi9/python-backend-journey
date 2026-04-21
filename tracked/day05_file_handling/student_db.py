FILE_NAME = "students.txt"

def save_student(name, age, course):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{course}\n")


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, age, course = line.strip().split(",")
                students.append((name, age, course))
    except FileNotFoundError:
        pass

    return students