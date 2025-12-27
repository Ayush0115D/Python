from pydantic import BaseModel
class product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool=True
product_one=product(id=1,name="Laptop",price=999.99,in_stock=True)
product_two=product(id=2,name="Mouse",price=25.50)
product_three=product(id=3,name="Keyboard")   