from pydantic import BaseModel
from typing import Optional, List


# Esquema para receber os dados de login
class TokenRequest(BaseModel):
    username: str
    password: str


# Esquema para retornar o token JWT
class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# Esquema para dados do usuário (payload)
class UserPayload(BaseModel):
    username: str
    roles: list[str]  # Exemplo de outras informações


# Esquema para criar um link (dados de entrada para a função criar_link)
class LinkCreationInput(BaseModel):
    ano: str
    area: str
    subarea: Optional[str] = None


# Esquema para saída da criação de link
class LinkCreationOutput(BaseModel):
    url: str


# Esquema para resposta da requisição HTTP
class RequisitionResponse(BaseModel):
    status: int
    response: Optional[str] = None


# Exemplo de esquema para erro (saída de exceções)
class ErrorResponse(BaseModel):
    detail: str
