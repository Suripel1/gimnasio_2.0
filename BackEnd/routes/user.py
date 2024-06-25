from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

user = APIRouter()
users = []

# @userModel
class ModelsUsers(BaseModel):
    id: str
    usuarios: str
    contrasena: str
    created_at: datetime = Field(default_factory=datetime.now)
    estatus: bool = False

@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

@user.get('/users', tags=["Usuarios"])
def get_usuarios():
    return users

@user.post('/users', tags=["Usuarios"])
def save_users(insert_users: ModelsUsers):
    users.append(insert_users.dict())
    return 'Datos guardados'

# Obtener un usuario por su ID
@user.get('/users/{usuario_id}', tags=["Usuarios"])
def get_usuario(usuario_id: str):
    for usuario in users:
        if usuario['id'] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Actualizar datos de un usuario por su ID
@user.put('/users/{usuario_id}', tags=["Usuarios"])
def update_usuario(usuario_id: str, usuario: ModelsUsers):
    for index, user in enumerate(users):
        if user['id'] == usuario_id:
            users[index] = usuario.dict()
            return "Usuario actualizado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Eliminar un usuario por su ID
@user.delete('/users/{usuario_id}', tags=["Usuarios"])
def delete_usuario(usuario_id: str):
    for index, user in enumerate(users):
        if user['id'] == usuario_id:
            del users[index]
            return "Usuario eliminado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
