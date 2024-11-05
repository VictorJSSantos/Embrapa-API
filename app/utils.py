import datetime
from fastapi import HTTPException
import jwt
import json
import os


from app.models import *
from response_data import *


SECRET_KEY = os.environ["SECRET_KEY"]


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


def return_name_from_model(Model):
    model_names = [opt.name for opt in Model]
    return model_names[0]


def transform_input_into_string(year, area, subarea=None):
    if subarea:
        return str(year), str(area), str(subarea)
    else:
        return str(year), str(area), None


def offline_fallback_get_data(year, area, subarea=None):
    dict_of_files = {
        "Produção": "response_production.json",
        "Processamento": "response_processing.json",
        "Importação": "response_imports.json",
        "Exportação": "response_imports.json",
        "Comercialização": "response_sales.json",
    }
    file_path = f"response_data/{dict_of_files.get(area)}"
    try:
        # Carregar JSON do arquivo
        with open(file_path, "r") as f:
            json_data = json.load(f)

        # Verificar e acessar subarea e ano, se especificados
        if subarea:
            return json_data.get(subarea, {}).get(
                str(year), f"Dados para '{subarea}' no ano {year} não encontrados."
            )
        else:
            return json_data.get(str(year), f"Dados para o ano {year} não encontrados.")

    except (FileNotFoundError, KeyError) as e:
        return {"error": f"Erro ao carregar dados para '{area}': {str(e)}"}
