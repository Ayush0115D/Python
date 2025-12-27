#adding validation with fields

from pydantic import BaseModel, Field
from typing import Optional
class Employee(BaseModel):
    id: int
    name:str = Field(..., min_length=2, max_length=50,description="Name of the employee",example="AYUSH")
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000)