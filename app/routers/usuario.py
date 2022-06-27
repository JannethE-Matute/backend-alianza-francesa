from re import U
from fastapi import APIRouter, HTTPException
# from app import database as db
# from app.models import LibroModel

import app.models as models, app.schemas as schemas
import app.methods.cuentas as func

router = APIRouter()

@router.post("/cuenta/crear")
def create_cuenta(cuenta: schemas.Cuenta) -> schemas.Cuenta:
    return func.create_cuenta_sql(cuenta)

@router.get("/cuenta/listar")
def get_cuentas() -> list[schemas.Cuenta]:
    return func.get_cuentas_sql()

@router.get("/{cuenta_id}/buscar")
def buscar_cuenta(cuenta_id: str) -> list[schemas.Cuenta]:
    res = func.buscar_cuenta_sql(cuenta_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Cuenta not found")

@router.put("/{cuenta_id}/editar")
def update_cuenta(cuenta_id: str, up_cuenta: schemas.Cuenta) -> schemas.Cuenta:
    res = func.update_cuenta_sql(cuenta_id,up_cuenta)
    if res:
        return res
    return HTTPException(status_code=404, detail="Cuenta not found")

@router.delete("/{cuenta_id}/eliminar")
def delete_cuenta(cuenta_id: str) -> schemas.Cuenta:
    res = func.delete_cuenta_sql(cuenta_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Cuenta not found")   



  













