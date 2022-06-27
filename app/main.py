from fastapi import FastAPI
import uvicorn

from app.schemas import Respuesta
import app.routers.auth as auth
import app.routers.chat as chat
import app.routers.usuario as usuario
import app.routers.notificacion as notificacion
import app.routers.evento as evento
from app.database import Base as db
import app.routers.post as post
import app.routers.reaccion_post as reaccion_post
import app.routers.categoria as categoria
import app.routers.rol as rol
import app.routers.contacto as contacto
import app.routers.archivo as archivo
import app.routers.grupo as grupo
#from dotenv import load_dotenv

app = FastAPI()
#uvicorn.run(app, port=8000, host="0.0.0.0")
#load_dotenv()



@app.get("/")
def get_message() -> Respuesta:
    return Respuesta(age=20, name="Juan")

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router)
app.include_router(usuario.router)
app.include_router(notificacion.router)
app.include_router(evento.router)
app.include_router(post.router)
app.include_router(reaccion_post.router)
app.include_router(categoria.router)
app.include_router(rol.router)
app.include_router(contacto.router)
app.include_router(archivo.router)
app.include_router(grupo.router)


'''

if __name__=='__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
    '''