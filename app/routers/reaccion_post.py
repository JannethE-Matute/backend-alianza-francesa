from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/reaccion_post"
)

@router.post("/crear")
def create_reaccion_Post(reaccion_Post: schemas.reaccion_Post) -> schemas.reaccion_Post:
    return func.create_reaccion_Post_sql(reaccion_Post)

@router.get("/listar")
def get_reaccion_Post() -> list[schemas.reaccion_Post]:
    return func.get_reaccion_Post_sql()

@router.get("/{reaccion_Post_id}/buscar")
def buscar_reaccion_Post(reaccion_Post_id: str) -> list[schemas.reaccion_Post]:
    res = func.buscar_reaccion_Post_sql(reaccion_Post_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Reaccion_Post not found")

@router.put("/{reaccion_Post_id}/editar")
def update_reaccion_Post(reaccion_Post_id: str, pos_reaccion_Post: schemas.reaccion_Post) -> schemas.reaccion_Post:
    res = func.update_reaccion_Post_sql(reaccion_Post_id,pos_reaccion_Post)
    if res:
        return res
    return HTTPException(status_code=404, detail="Reaccion_Post not found")

@router.delete("/{reaccion_Post_id}/eliminar")
def delete_reaccion_Post(reaccion_Post_id: str) -> schemas.reaccion_Post:
    res = func.delete_reaccion_Post_sql(reaccion_Post_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Reaccion_Post not found")