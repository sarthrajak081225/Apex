from sqlalchemy.orm import Session
import schemas
import models

def get_student(db:Session):
    students = db.query(models.Student).all()
    return students


def make_update(db:Session,info):
    obj = db.query(models.Student).filter(models.Student.id == info['id']).first()
    if obj:
        print(info)
        obj.name   =  info['name']
        obj.age    =  info['age']
        obj.branch =  info['branch']
        db.commit()
        db.refresh(obj)
        return obj
    else:
        print("Student not found")
       
    return "Something went wrong" 

def make_delete(db: Session, id: int):
    obj = db.query(models.Student).filter(models.Student.id == id).first()
    # print(obj.name,obj.id)
    if obj:
        data = {
                "Name"   : obj.name,
                "age"    : obj.age,
                "branch" : obj.branch,           
        }
        db.delete(obj)
        db.commit()
        return {"Data Deleted": data}
    else:
        return None
