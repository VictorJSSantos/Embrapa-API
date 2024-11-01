from fastapi.security import (
    OAuth2PasswordRequestForm,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from fastapi import HTTPException, Depends, APIRouter
from typing import Annotated


from app.utils import *  # create_jwt_token, verify_jwt_token,
from app.schemas.login_schema import *


router = APIRouter()


# Classe para autenticação Bearer
class BearerToken(HTTPBearer):
    def __init__(self):
        super().__init__()


# Rota para login que retorna o token JWT
@router.post(
    "/token",
    tags=["Login"],
    summary="Enviar dados de usuário para fazer login",
    response_model=TokenResponse,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Rota de login que valida as credenciais e retorna um token JWT.
    """
    user_data = next(
        (
            user
            for user in CREDENTIALS["users"]
            if user["username"] == form_data.username
            and user["password"] == form_data.password
        ),
        None,
    )

    if not user_data:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos.")

    token = create_jwt_token(user_data["username"], user_data["password"])
    return {"access_token": token, "token_type": "bearer"}


# Rota protegida que retorna informações do usuário com base no token JWT
@router.get(
    "/users/login/token",
    tags=["Login"],
    summary="Obter dados do usuário validado",
    # response_model=UserPayload,
)
async def read_users_me(
    credentials: HTTPAuthorizationCredentials = Depends(BearerToken()),
):
    """
    Rota protegida que retorna as informações do usuário com base no token JWT.
    """
    token = credentials.credentials  # Extraí o token do cabeçalho
    payload = verify_jwt_token(token)  # Verifica e decodifica o token JWT

    return {"payload": payload}
