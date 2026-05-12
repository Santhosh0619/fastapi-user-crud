from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.user import UserRequest, UserResponse
from app.models.user import User
from fastapi import APIRouter, Depends
from fastapi import UploadFile, File, Form
from datetime import date
import os

router = APIRouter()

@router.post("/user", response_model=UserResponse)
def User_Create(
    name: str = Form(...),
    dob: date = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as file:
        file.write(image.file.read())

    new_user = User(
        name=name,
        dob=dob,
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
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return {"Error": "User Not Found"}

    if user.image_url and os.path.exists(user.image_url):
        os.remove(user.image_url)

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as file:
        file.write(image.file.read())

    user.name = name
    user.dob = dob
    user.image_url = file_path

    db.commit()
    db.refresh(user)

    return user


@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return {"Error": "User Not Found"}

    if user.image_url and os.path.exists(user.image_url):
        os.remove(user.image_url)

    db.delete(user)
    db.commit()

    return {"message": "User Deleted Successfully"}