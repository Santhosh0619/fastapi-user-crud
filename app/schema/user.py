from pydantic import BaseModel
from datetime import date

class UserRequest(BaseModel):
    name: str
    dob: date

class UserResponse(BaseModel):
    id: int
    name: str
    dob: date
    image_url: str | None=None

    class Config:
        from_attributes = True