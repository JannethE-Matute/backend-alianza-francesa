from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/post"
)

@router.post("/crear")
def create_post(post: schemas.Post) -> schemas.Post:
    return func.create_post_sql(post)

@router.get("/listar")
def get_post() -> list[schemas.Post]:
    return func.get_post_sql()

@router.get("/{post_id}/buscar")
def buscar_post(post_id: str) -> list[schemas.Post]:
    res = func.buscar_post_sql(post_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Post not found")

@router.put("/{post_id}/editar")
def update_post(post_id: str, pt_post: schemas.Post) -> schemas.Post:
    res = func.update_post_sql(post_id,pt_post)
    if res:
        return res
    return HTTPException(status_code=404, detail="Post not found")

@router.delete("/{post_id}/eliminar")
def delete_post(post_id: str) -> schemas.Post:
    res = func.delete_post_sql(post_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Post not found") 