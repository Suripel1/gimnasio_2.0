from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from saqlachemy.orm import Session
from jwt_config import valida_token
import crud.users, config.db, models.users

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = congif.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class Portador(HTTPBearer):
    async def __call__(self,request:Request, db: Session =Dependes(get_db)):
        autorizacion = await super().__call__(request)
        dato=valida_token(autorizacion.credentials)
        db_userlogin= crud.users.get_user_by_credentials(db, username=dato["Nombre_Usuario"],
                                                         correo=dato["Correo_Electronico"],
                                                         telefono=dato["Numero_Telefonico_movil"],
                                                         password=dato["Contrasena"])
        
        if db_userlogin is None:
            raise HTTPException(status_code=403, detail ='Login no autorizzado')
        return db_userlogin