from fastapi import FastAPI
from routes.user import user
from routes.persona import person

app = FastAPI()
app.include_router(user)
app.include_router(person)


print("Hola bienvenido a mi backend")