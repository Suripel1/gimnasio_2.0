from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime


user = APIRouter()
users = []

# @userModel
class models_users(BaseModel):
    id:str
    usuarios:str
    contrasena:str
    created_at:datetime = datetime.now()
    estatus:bool=False

@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

@user.get('/users')
def get_usuarios():
    return users

@user.post('/users')
def save_users(insert_users:models_users):
    users.append(insert_users)
    print(users)
    return 'Datos guardados'

# Obtener un usuario por su ID
@user.get('/users/{usuario_id}')
def get_usuarios(usuario_id: int):
    for usuario in users:
        if usuario['id'] == usuario_id:
            return users


# Actualizar datos de un usuario por su ID
@user.put('/users/{usuario_id}')
def update_usuarios(usuario_id: int, usuario: models_users):
    for index, user in enumerate(users):
        if user['id'] == usuario_id:
            users[index] = usuario.dict()
            return "Usuario actualizado correctamente"

# Eliminar un usuario por su ID
@user.delete('/users/{usuario_id}')
def delete_user(usuario_id: int):
    for index, user in enumerate(users):
        if user['id'] == usuario_id:
            del users[index]
            return "Usuario eliminado correctamente"

