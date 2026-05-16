from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message": "Student API"}

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(student: dict):
    students.append(student)
    return {"message": "Student added"}

@app.put("/students/{index}")
def update_student(index: int, student: dict):
    students[index] = student
    return {"message": "Student updated"}

@app.delete("/students/{index}")
def delete_student(index: int):
    students.pop(index)
    return {"message": "Student deleted"}