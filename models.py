from sqlalchemy import Column, Integer, String
from database import Base   # (agar ye code database.py me hai)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    branch = Column(String, nullable=True)
    # email = Column(String, unique=True, nullable=True)

class Teacher(Base):

    __tablename__ = "Teacher"

    id = Column(Integer, primary_key=True, index=True)
    namme = Column(String)
    age = Column(Integer)
    Subject = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)  
        