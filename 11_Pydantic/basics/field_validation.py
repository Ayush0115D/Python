from pydantic import BaseModel, field_validator
#field validator
class User(BaseModel):
    username: str
  
    @field_validator('username')
    def validate_username(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return v
    #model validator
class SignUpData(BaseModel):
    
    password: str
    confirm_password: str

    @field_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values   