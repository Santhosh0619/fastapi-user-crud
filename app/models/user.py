from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50))
    dob=Column(Date)
    image_url=Column(String(200))