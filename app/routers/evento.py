from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/evento"
)

@router.post("/crear")
def create_evento(evento: schemas.Evento) -> schemas.Evento:
    return func.create_evento_sql(evento)

@router.get("/listar")
def get_evento() -> list[schemas.Evento]:
    return func.get_evento_sql() 

@router.get("/{evento_id}/buscar")
def buscar_evento(evento_id: str) -> list[schemas.Evento]:
    res = func.buscar_evento_sql(evento_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Evento not found")

@router.put("/{evento_id}/editar")
def update_evento(evento_id: str, evn_evento: schemas.Evento) -> schemas.Evento:
    res = func.update_evento_sql(evento_id,evn_evento)
    if res:
        return res
    return HTTPException(status_code=404, detail="Evento not found")

@router.delete("/{evento_id}/eliminar")
def delete_evento(evento_id: str) -> schemas.Evento:
    res = func.delete_evento_sql(evento_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Evento not found")