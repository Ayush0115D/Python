from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime
# Example of serialization and deserialization with Pydantic
class Address(BaseModel):
    street: str
    city: str
    postal_code: str
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime 
    address: Address
    tags: List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')}
    )
user=User(
    id=1,  
    name="AYUSH",
    email="dhakreayush@gmail.com",
    createdAt=datetime(2024,3,15,14,30),
    address=Address(
        street="123 Main St",
        city="Metropolis",
        postal_code="12345"
    ),
    is_active=True,
    tags=["premium","subscriber"]
)       
python_dict=user.model_dump()#used to convert pydantic model to python dict
print(user)
print("="*30)#separator
print(python_dict)

json_str=user.model_dump_json()#used to convert pydantic model to json string
print("="*30)
print(json_str)