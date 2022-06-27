from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/archivo"
)

@router.post("/crear")
def create_archivo(archivo: schemas.Archivo) -> schemas.Archivo:
    return func.create_archivo_sql(archivo)

@router.get("/listar")
def get_archivo() -> list[schemas.Archivo]:
    return func.get_archivo_sql()

@router.get("/{archivo_id}/buscar")
def buscar_archivo(archivo_id: str) -> list[schemas.Archivo]:
    res = func.buscar_archivo_sql(archivo_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Archivo not found")

@router.put("/{archivo_id}/editar")
def update_archivo(archivo_id: str, arh_archivo: schemas.Archivo) -> schemas.Archivo:
    res = func.update_archivo_sql(archivo_id,arh_archivo)
    if res:
        return res
    return HTTPException(status_code=404, detail="Archivo not found")

@router.delete("/{archivo_id}/eliminar")
def delete_archivo(archivo_id: str) -> schemas.Archivo:
    res = func.delete_archivo_sql(archivo_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Archivo not found")