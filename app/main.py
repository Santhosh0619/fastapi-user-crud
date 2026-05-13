from fastapi import FastAPI
from app.db import database
from app.db.database import engine, Base
from app.models import user
from app.crud.user import router

#Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(router)

