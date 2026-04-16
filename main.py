from fastapi import FastAPI, Depends, HTTPException
from database import engine, Base
import models
from database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/students")
@app.post("/create_students")
def insert_student(name: str, age: int, branch: str, db: Session = Depends(get_db)):
    new_student = models.Student(name=name, age=age, branch=branch)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

import schemas
import crud

@app.get("/all_stu/", response_model=list[schemas.student])
async def all_students(db: Session = Depends(get_db)):
    return crud.get_student(db) 

@app.get("/update/")
async def update_student(id : int, name : str, branch : str, age : int, db: Session = Depends(get_db)):
    info = {"id" : id , "name": name, "branch": branch, "age": age}   
    return crud.make_update(db, info)



@app.delete("/delete_data/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    deleted = crud.make_delete(db, id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted