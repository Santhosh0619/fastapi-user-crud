from pydantic import BaseModel, EmailStr
from datetime import date

from enum import Enum

class Gender(str, Enum):
    male="male"
    female="female"

class UserRequest(BaseModel):
    name: str
    dob: date
    gender: Gender
    email: EmailStr
    

class UserResponse(BaseModel):
    id: int
    name: str
    dob: date
    gender: Gender
    email: EmailStr
    image_url: str | None=None

    class Config:
        from_attributes = True