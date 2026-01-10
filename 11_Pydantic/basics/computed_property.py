from pydantic  import BaseModel, Field
class Product(BaseModel):
    
    price: float
    quantity: int

    @computed_property
    @property
    def total_price(self) -> float:
     return self.price * self.quantity
  
class Booking(BaseModel):
   User_id: int
   room_id: int
   nights:int = Field(ge=0)
   rate_per_night: float


   @computed_property
   @property
   def total_cost(self) -> float:
        return self.nights * self.rate_per_night
booking=Booking(User_id=1, room_id=101, nights=3, rate_per_night=150.0)   
print(f"Total booking cost: {booking.total_cost}")
print(booking.model.dumps())