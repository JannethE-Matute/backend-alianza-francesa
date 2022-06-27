from fastapi import APIRouter, HTTPException
import app.schemas as schemas
import app.methods.cuentas as func
router = APIRouter(
    prefix="/chat"
)

@router.post("/crear")
def create_chat(chat: schemas.Chat) -> schemas.Chat:
    return func.create_chat_sql(chat)

@router.get("/listar")
def get_chat() -> list[schemas.Chat]:
    return func.get_chat_sql()
    
@router.get("/{chat_id}/buscar")
def buscar_chat(chat_id: str) -> list[schemas.Chat]:
    res = func.buscar_chat_sql(chat_id)
    if res:
        return res
    return HTTPException(status_code=404, detail="Chat not found")

@router.put("/{chat_id}/editar")
def update_chat(chat_id: str, ch_chat: schemas.Chat) -> schemas.Chat:
    res = func.update_chat_sql(chat_id,ch_chat)
    if res:
        return res
    return HTTPException(status_code=404, detail="Chat not found")

@router.delete("/{chat_id}/eliminar")
def delete_chat(chat_id: str) -> schemas.Chat:
    res = func.delete_chat_sql(chat_id)
    if res:
        return True
    return HTTPException(status_code=404, detail="Chat not found")