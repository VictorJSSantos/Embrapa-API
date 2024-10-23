import datetime
from fastapi import HTTPException
import jwt
import yaml


from app.models import *


# Carregar as credenciais dos usuários do arquivo tokens.yaml
def load_credentials():
    try:
        with open("./data/tokens.yaml", "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao carregar credenciais: {e}"
        )


CREDENTIALS = load_credentials()
SECRET_KEY = CREDENTIALS["SECRET_KEY"]


# Função para criar o token JWT
def create_jwt_token(username: str, password: str):
    payload = {
        "sub": username,
        "pass": password,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=30),  # Expira em 30 minutos
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# Função para verificar o token JWT
def verify_jwt_token(token: str):
    try:
        # print(f"Verificando token: {token}")  # Para debugging
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # ["sub"]  # Retorna o username do token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado.")
    except jwt.InvalidTokenError as e:
        print(f"Erro ao validar token: {e}")  # Para debugging
        raise HTTPException(status_code=401, detail="Token inválido.")


def retornar_name_do_model(Model):
    model_names = [opt.name for opt in Model]
    return model_names[0]


def transformar_dados_de_url_em_string(ano, area, subarea=None):
    if subarea:
        return str(ano), str(area), str(subarea)
    else:
        return str(ano), str(area), None
