from pydantic import BaseModel, EmailStr
from datetime import date

class UserRequest(BaseModel):
    name: str
    dob: date
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    dob: date
    email: EmailStr
    image_url: str | None=None

    class Config:
        from_attributes = True