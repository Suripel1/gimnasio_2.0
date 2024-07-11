from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum

class MyEstatus(enum.Enum):
   Activo = "Activo"
   Inactivo = "Inactivo"
   Suspendido = "Suspendido"
   Bloqueado = "Bloqueado"

class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Nombre_usuario = Column(String(255))
    Correo_Electronico= Column(String(255))
    Contrasena = Column(LONGTEXT)
    Numero_Telefonico_Movil = Column(Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    
 
   
