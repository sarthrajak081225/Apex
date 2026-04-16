from pydantic import BaseModel
class student(BaseModel):
    name : str
    class Config:
        from_attributes = True

    