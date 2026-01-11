from pydantic import BaseModel, Field, computed_field
class Product(BaseModel):
    
    price: float
    quantity: int

    @computed_field
   
    def total_price(self) -> float:
     return self.price * self.quantity
  
class Booking(BaseModel):
   User_id: int
   room_id: int
   nights:int = Field(ge=0)
   rate_per_night: float


   @computed_field
   
   def total_amount(self) -> float:
        return self.nights * self.rate_per_night
booking=Booking(User_id=1, room_id=101, nights=3, rate_per_night=150.0)   
print(booking.total_amount)
print(booking.model_dump())