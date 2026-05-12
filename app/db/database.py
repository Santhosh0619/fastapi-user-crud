from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.config import DATABASE_URL

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()