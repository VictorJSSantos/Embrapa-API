from pydantic import BaseModel


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
