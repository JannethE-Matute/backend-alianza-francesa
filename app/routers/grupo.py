from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/grupo"
)

@router.post("/crear")
def create_grupo(grupo: schemas.Grupo) -> schemas.Grupo:
    return func.create_grupo_sql(grupo)
    
@router.get("/listar")
def get_grupos() -> list[schemas.Grupo]:
    return func.get_grupos_sql()

@router.get("/{grupo_id}/buscar")
def buscar_grupo(grupo_id: str) -> list[schemas.Grupo]:
    res = func.buscar_grupo_sql(grupo_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Grupo not found")

@router.put("/{grupo_id}/editar")
def update_grupo(grupo_id: str, up_grupo: schemas.Grupo) -> schemas.Grupo:
    res = func.update_grupo_sql(grupo_id,up_grupo)
    if res:
        return res
    return HTTPException(status_code=404, detail="Grupo not found")

@router.delete("/{grupo_id}/eliminar")
def delete_grupo(grupo_id: str) -> schemas.Grupo:
    res = func.delete_grupo_sql(grupo_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Grupo not found")
