from fastapi import APIRouter, Depends
from config.db import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session
from routes.user import user
from cruds import crud
from sqlalchemy.orm import sessiomaker


user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

@user.get('/users',response_model=list[schemas.User], tags=["Usuarios"])
def get_usuarios(skip: int = 0 , limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users





