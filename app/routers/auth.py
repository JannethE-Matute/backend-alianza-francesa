from fastapi import APIRouter, Header, Request
from pydantic import BaseModel, EmailStr
#from functions_jwt import validate_token, write_token
import app.methods.functions_jwt as fjwt
from fastapi.responses import JSONResponse

import app.database as db
import app.models as models
import app.schemas as schemas

router = APIRouter()


class User(BaseModel):
    email: EmailStr | None = None
    password: str | None = None


@router.post("/login")
def login(user: User) -> schemas.RespuestaAuth:
    cuenta = db.session.query(models.Cuenta).filter(
        models.Cuenta.email == user.email).first()
    if cuenta:
        return schemas.RespuestaAuth(status_code=200, usuario=schemas.Cuenta(id=cuenta.id), token=fjwt.write_token(cuenta))
        # return "Logeo exitoso"
    else:
        return schemas.RespuestaAuth(token=None,usuario=None, status_code=404)


@router.get("/verify/token")
def verify_token(request: Request):
    return fjwt.validate_token(request.headers['x-token'])
