from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter(
    prefix="/contacto"
)

@router.post("/crear")
def create_contacto(contacto: schemas.Contacto) -> schemas.Contacto:
    return func.create_contacto_sql(contacto)

@router.get("/listar")
def get_contacto() -> list[schemas.Contacto]:
    return func.get_contacto_sql()

@router.get("/{contacto_id}/buscar")
def buscar_contacto(contacto_id: str) -> list[schemas.Contacto]:
    res = func.buscar_contacto_sql(contacto_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Contacto not found")

@router.put("/{contacto_id}/editar")
def update_contacto(contacto_id: str, cot_contacto: schemas.Contacto) -> schemas.Contacto:
    res = func.update_contacto_sql(contacto_id,cot_contacto)
    if res:
        return res
    return HTTPException(status_code=404, detail="Contacto not found")

@router.delete("/{contacto_id}/eliminar")
def delete_contacto(contacto_id: str) -> schemas.Contacto:
    res = func.delete_contacto_sql(contacto_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Contacto not found")