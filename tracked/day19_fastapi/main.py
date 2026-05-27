from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str


students = []


@app.get("/")
def home():
    return {"message": "FastAPI is working"}


@app.get("/students")
def get_students():
    return students


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return student


@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):

    if id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[id] = updated_student

    return {
        "message": "Student updated",
        "student": updated_student
    }


@app.delete("/students/{id}")
def delete_student(id: int):

    if id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(id)

    return {
        "message": "Student deleted",
        "student": deleted_student
    }