from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Srinidhi"},
    {"id": 2, "name": "Ravi"}
]

@app.get("/")
def home():
    return {"message": "Student API"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"error": "Student not found"}