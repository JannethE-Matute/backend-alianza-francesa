from datetime import datetime
from tkinter.messagebox import NO
from typing import List
from pydantic import BaseModel
from sqlalchemy import String


class Respuesta(BaseModel):
    name: str | None = None
    age: int | None = None


class Evento(BaseModel):
    id: int | None = None 
    nombre: str | None = None
    tipo_privacidad: str | None = None
    fecha_hora:datetime | None = None
    categoria_id:int | None = None

class Cuenta(BaseModel):
    id: int | None = None
    nombre: str | None = None
    apellido: str | None = None
    edad: int | None = None
    sexo: str | None = None
    direccion: str | None = None
    avatar: str | None = None
    email: str | None = None
    password: str | None = None
    estado: str | None = None
    rol_id: int | None = None
    #chat_id: int | None = None
    #eventos: List[Evento]=[]
    #grupos: List[Grupo]=[]
    #evento_id: int | None = None
    #grupo_id: int | None = None


class Grupo(BaseModel):
    id: str | None = None 
    nombre: str | None = None
    tipo: str | None = None
    cuentas: List[Cuenta]=[]
    class Config:
        orm_mode = True

class Rol(BaseModel):
    id: str | None = None 
    tipo: str | None = None
    #cuentas: List[Cuenta] = []

class Categoria(BaseModel):
    id: int | None = None 
    nombre: str | None = None

class Notificacion(BaseModel):
    id: int | None = None 
    mensaje: str | None = None
    fecha_hora: datetime | None = None
    post_id: int | None = None

class Chat(BaseModel):
    id: str | None = None 
    mensaje: str | None = None
    avatar: str | None = None
    estado: str | None = None
    cuenta_id: int | None = None
    cuenta_grupo_id: int | None = None

class Post(BaseModel):
    id: int | None = None 
    cuenta_id: int | None = None
    evento_id: int | None = None
    fecha_hora_create: datetime | None = None
    mensaje: str | None = None
    
class Archivo(BaseModel):
    id: str | None = None 
    tipo: str | None = None
    contenido: str | None = None
    url: str | None = None
    post_id: int | None = None

class reaccion_Post(BaseModel):
    id: str | None = None 
    tipo: str | None = None
    reaccion: str | None = None
    fecha_hora: datetime | None = None
    post_id: int | None = None
    cuenta_id: int | None = None

class Contacto(BaseModel):
    id: str | None = None 
    fecha_hora: datetime | None = None
    descripcion: str | None = None
    cuenta_id: int | None = None
    
class RespuestaAuth(BaseModel):
    status_code: int | None
    token: str | None
    usuario:Cuenta | None