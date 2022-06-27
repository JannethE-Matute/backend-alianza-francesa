from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/rol"
)

@router.post("/crear")
def create_rol(rol: schemas.Rol) -> schemas.Rol:
    return func.create_rol_sql(rol)

@router.get("/listar")
def get_rol() -> list[schemas.Rol]:
    return func.get_rol_sql()

@router.get("/{rol_id}/buscar")
def buscar_rol(rol_id: str) -> list[schemas.Rol]:
    res = func.buscar_rol_sql(rol_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Rol not found")

@router.put("/{rol_id}/editar")
def update_rol(rol_id: str, rro_rol: schemas.Rol) -> schemas.Rol:
    res = func.update_rol_sql(rol_id,rro_rol)
    if res:
        return res
    return HTTPException(status_code=404, detail="Rol not found")

@router.delete("/{rol_id}/eliminar")
def delete_rol(rol_id: str) -> schemas.Rol:
    res = func.delete_rol_sql(rol_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Rol not found")