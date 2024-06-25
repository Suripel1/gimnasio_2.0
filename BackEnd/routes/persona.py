from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

persona = APIRouter()
personas=[]

class model_personas(BaseModel):
    id:str
    nombre:str
    primer_apellido:str
    segundo_apellido:Optional[str]
    titulo:str
    fecha_nacimiento: datetime
    genero: str
    tipo_sangre: str
    created_at: datetime = datetime.now()
    estatus: bool = False

# Obtener todas las personas
@persona.get('/personas', tags=["Personas"])
def getPersonas():
    return personas

# Obtener una persona por su ID
@persona.get('/personas/{persona_id}', tags=["Personas"])
def getPersona(persona_id: int):
    for persona in personas:
        if persona['id'] == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Guardar una nueva persona
@persona.post('/personas', tags=["Personas"])
def save_persona(datos_persona: model_personas):
    personas.append(datos_persona.dict())
    return "Datos guardados correctamente"

# Actualizar datos de una persona por su ID
@persona.put('/personas/{persona_id}', tags=["Personas"])
def updatePersona(persona_id: int, datos_persona: model_personas):
    for index, persona in enumerate(personas):
        if persona['id'] == persona_id:
            personas[index] = datos_persona.dict()
            return "Datos actualizados correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Eliminar una persona por su ID
@persona.delete('/personas/{persona_id}', tags=["Personas"])
def deletePersona(persona_id: int):
    for index, persona in enumerate(personas):
        if persona['id'] == persona_id:
            del personas[index]
            return "Persona eliminada correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Buscar personas por criterios específicos, incluyendo por ID
@persona.get('/buscar-personas', tags=["Personas"])
def buscar_personas(id: Optional[int] = None,
                    nombre: Optional[str] = None,
                    primer_apellido: Optional[str] = None,
                    segundo_apellido: Optional[str] = None,
                    fecha_nacimiento: Optional[datetime] = None):
    if id is not None:
        resultados = [persona for persona in personas if persona['id'] == id]
    else:
        resultados = personas.copy()  # Copia de la lista original

        if nombre:
            resultados = [persona for persona in resultados if persona['nombre'] == nombre]

        if primer_apellido:
            resultados = [persona for persona in resultados if persona['primer_apellido'] == primer_apellido]

        if segundo_apellido:
            resultados = [persona for persona in resultados if persona.get('segundo_apellido') == segundo_apellido]

        if fecha_nacimiento:
            resultados = [persona for persona in resultados if persona['fecha_nacimiento'] == fecha_nacimiento]

        if not any([nombre, primer_apellido, segundo_apellido, fecha_nacimiento]):
            raise HTTPException(status_code=400, detail="Debe proporcionar al menos un criterio de búsqueda")

    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron personas con los criterios de búsqueda proporcionados")

    return resultados