from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/notificacion"
)

@router.post("/crear")
def create_notificacion(notificacion: schemas.Notificacion) -> schemas.Notificacion:
    return func.create_notificacion_sql(notificacion)

@router.get("/listar")
def get_notificacion() -> list[schemas.Notificacion]:
    return func.get_notificacion_sql()

@router.get("/{notificacion_id}/buscar")
def buscar_notificacion(notificacion_id: str) -> list[schemas.Notificacion]:
    res = func.buscar_notificacion_sql(notificacion_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Notificacion not found")

@router.put("/{notificacion_id}/editar")
def update_notificacion(notificacion_id: str, not_notificacion: schemas.Notificacion) -> schemas.Notificacion:
    res = func.update_notificacion_sql(notificacion_id,not_notificacion)
    if res:
        return res
    return HTTPException(status_code=404, detail="Notificacion not found")

@router.delete("/{notificacion_id}/eliminar")
def delete_notificacion(notificacion_id: str) -> schemas.Notificacion:
    res = func.delete_notificacion_sql(notificacion_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Notificacion not found")