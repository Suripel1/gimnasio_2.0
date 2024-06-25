from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

tb_users = Table("users", meta ,
                 Column("id", Integer, primary_key=True),
                 Column("usuario", String(255)),
                 Column("password", String(255)),
                 Column("estatus", bool=False),
                 Column("id_persona",Integer)
                 )


meta.create_all(engine)