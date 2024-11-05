from fastapi.security import (
    OAuth2PasswordRequestForm,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from fastapi import HTTPException, Depends, APIRouter
from typing import Annotated


from app.utils import *
from app.schemas.login_schema import *
import os

router = APIRouter()


# Classe para autenticação Bearer
class BearerToken(HTTPBearer):
    def __init__(self):
        super().__init__()


# Rota para login que retorna o token JWT
@router.post(
    "/token",
    description="Enviar dados para obter o Token do Usuário",
    tags=["Login"],
    summary="Enviar dados de usuário para fazer login",
    response_model=TokenResponse,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Rota de login que valida as credenciais e retorna um token JWT.
    """
    # Obtenha as credenciais do ambiente
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    # Verifique as credenciais
    if form_data.username != username or form_data.password != password:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos.")

    token = create_jwt_token(username, password)
    return {"access_token": token, "token_type": "bearer"}


# Rota protegida que retorna informações do usuário com base no token JWT
@router.get(
    "/users/login/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados sobre o Token do Usuário validado",
    tags=["Login"],
    summary="Obter dados do token do usuário validado",
    response_model=UserPayload,
)
async def read_users_me(
    credentials: HTTPAuthorizationCredentials = Depends(BearerToken()),
):
    """
    Rota protegida que retorna as informações do usuário com base no token JWT.
    """
    token = credentials.credentials  # Extraí o token do cabeçalho
    payload = verify_jwt_token(token)  # Verifica e decodifica o token JWT

    return payload
