from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/categoria"
)

@router.post("/crear")
def create_categoria(categoria: schemas.Categoria) -> schemas.Categoria:
    return func.create_categoria_sql(categoria)

@router.get("/listar")
def get_categoria() -> list[schemas.Categoria]:
    return func.get_categoria_sql()

@router.get("/{categoria_id}/buscar")
def buscar_categoria(categoria_id: str) -> list[schemas.Categoria]:
    res = func.buscar_categoria_sql(categoria_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Categoria not found")

@router.put("/{categoria_id}/editar")
def update_categoria(categoria_id: str, ca_categoria: schemas.Categoria) -> schemas.Categoria:
    res = func.update_categoria_sql(categoria_id,ca_categoria)
    if res:
        return res
    return HTTPException(status_code=404, detail="Categoria not found")

@router.delete("/{categoria_id}/eliminar")
def delete_categoria(categoria_id: str) -> schemas.Categoria:
    res = func.delete_categoria_sql(categoria_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Categoria not found")