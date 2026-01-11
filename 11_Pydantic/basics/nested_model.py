from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address
address=Address(
    street="123 Main St",
    city="Agra",
    postal_code="12345"
)    
user=User(
    id=1,
    name="Ayush",
    address=address
)

user_data={
    "id": 2,
    "name": "Rahul",
    "address": {
        "street": "123 abc",
        "city": "Delhi",
        "postal_code": "2004"
    }   
}
user=User(**user_data)
print(user)