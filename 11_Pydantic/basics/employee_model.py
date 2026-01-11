#adding validation with fields
from pydantic import BaseModel, Field
from typing import Optional
class Employee(BaseModel):
    id: int
    name:str = Field(..., min_length=2, max_length=50,description="Name of the employee",example="AYUSH")
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000)
class User(BaseModel):
    email:str=Field(...,regex=r'')
    phone:str=Field(..., regex =r'')  
    age:int =Field(...,ge=0,le=150,description="Age must be between 18 and 65")
    discount:float=Field(...,ge=0.0,le=100,description="Discount percentage")