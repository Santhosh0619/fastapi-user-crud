from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.user import UserRequest, UserResponse, Gender
from app.models.user import User
from fastapi import APIRouter, Depends
from fastapi import UploadFile, File, Form
from datetime import date
import os

from pydantic import EmailStr
from fastapi import HTTPException

router = APIRouter()

@router.post("/user", response_model=UserResponse, status_code=201)
def User_Create(
    name: str = Form(...),
    dob: date = Form(...),
    gender: Gender = Form(...),
    email: EmailStr = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):


    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as file:
        file.write(image.file.read())
    
    new_user = User(
        name=name,
        dob=dob,
        gender=gender,
        email=email,
        image_url=file_path
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/user", response_model=list[UserResponse])
def get_user(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.put("/user/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    name: str = Form(...),
    dob: date = Form(...),
    gender: Gender = Form(...),
    email: EmailStr = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    

    existing_user = db.query(User).filter(User.email == email,User.id != user_id).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")


    if user.image_url and os.path.exists(user.image_url):
        os.remove(user.image_url)

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as file:
        file.write(image.file.read())

    user.name = name
    user.dob = dob
    user.gender=gender
    user.email=email
    user.image_url = file_path

    db.commit()
    db.refresh(user)

    return user


@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")

    if user.image_url and os.path.exists(user.image_url):
        os.remove(user.image_url)

    db.delete(user)
    db.commit()

    return {"message": "User Deleted Successfully"}