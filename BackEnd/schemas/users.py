from typing import List, Union, optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    Nombre_Usuario: optional[str] = None
    Correo_electronico: optional[str] = None
    Contrasena: str
    Numero_Telefonico_Movil: optional[str] = None