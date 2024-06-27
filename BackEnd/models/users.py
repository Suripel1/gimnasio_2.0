from sqlalchemy import  Column, Interger, String, DateTime, Boolean
from config.db import Base

class users(Base):
    __tablename__ = 'users'

    id = Column(Interger, primary_key=True, index=True)
    usuario = Column(String(255), index=True)
    password = Column(String(255), index=True)
    status = Column(Boolean, index=True)
    
