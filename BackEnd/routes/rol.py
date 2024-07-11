from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.rols, config.db, schemas.rols, models.rols
from typing import List
key=Fernet.generate_key()
f = Fernet(key)
rol = APIRouter()
models.rols.Base.metadata.create_all(bind=config.db.engine)
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@rol.get("/rols/", response_model=List[schemas.rols.Rol], tags=["Roles"])
def read_rols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.rols.get_rols(db=db, skip=skip, limit=limit)
    return db_roles
@rol.post("/rol/{id}", response_model=schemas.rols.Rol, tags=["Roles"])
def read_rol(id: int, db: Session = Depends(get_db)):
    db_rol= crud.rols.get_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol
@rol.post("/rol/", response_model=schemas.rols.Rol, tags=["Roles"])
def create_rol(rol: schemas.rols.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.rols.get_rol_by_nombre(db, rol=rol.Nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="Rol existente")
    return crud.rols.create_rol(db=db, rol=rol)
@rol.put("/rol/{id}", response_model=schemas.rols.Rol, tags=["Roles"])
def update_rol(id: int, rol: schemas.rols.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.rols.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no existe ")
    return db_rol
@rol.delete("/rol/{id}", response_model=schemas.rols.Rol, tags=["Roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.rols.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no existe")
    return db_rol
