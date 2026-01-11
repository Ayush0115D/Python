from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
class Person(BaseModel):# Example of field-level validation
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, v):  
        if not v.istitle():
            raise ValueError('must be capitalized')
        return v
        # Example of field transformation
class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
  # Example of pre-processing input data    
class Product(BaseModel):
    price:str #$4.47
    @field_validator('price',mode='before')
    def parse_price(cls,v):
      if isinstance(v,str):
          return float(v.replace('$',''))
      return v    
# Example of cross-field validation
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator( mode='after')
    def validate_date_range(cls, values):
        if values.start >= values.end:
            raise ValueError("end date must be after start date")
        return values