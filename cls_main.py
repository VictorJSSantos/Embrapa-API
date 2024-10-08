# from utils.functions import *
import jwt
import datetime
import yaml
from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer
from bs4 import BeautifulSoup

# from typing import Optional
# import requests
# from fastapi.responses import HTMLResponse
from utils.transformar import Extractor
from utils.extrair import Requisition
from utils.basemodel import *
from typing import Annotated

# Inicializando o FastAPI
app = FastAPI()
extrair = Extractor()  # ano=None, area=None, subarea=None, url=None
requisitar = Requisition()  # ano=None, area=None, subarea=None, url=None


# Carregar as credenciais dos usuários do arquivo tokens.yaml
def load_credentials():
    try:
        with open("./data/tokens.yaml", "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao carregar credenciais: {e}"
        )


"""
Rotas de Autorização
"""

credentials = load_credentials()
SECRET_KEY = credentials["SECRET_KEY"]


# Classe para autenticação Bearer
class BearerToken(HTTPBearer):
    def __init__(self):
        super().__init__()


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
        print(f"Verificando token: {token}")  # Para debugging
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # ["sub"]  # Retorna o username do token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado.")
    except jwt.InvalidTokenError as e:
        print(f"Erro ao validar token: {e}")  # Para debugging
        raise HTTPException(status_code=401, detail="Token inválido.")


@app.get("/")
async def route_default():
    return "Aqui é a API Embrapa"


# Rota para login que retorna o token JWT
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Rota de login que valida as credenciais e retorna um token JWT.
    """
    user_data = next(
        (
            user
            for user in credentials["users"]
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
@app.get("/users/login/token", dependencies=[Depends(BearerToken())])
def read_users_me(token: str = Depends(BearerToken())):
    """
    Rota protegida que retorna as informações do usuário.
    """
    payload = verify_jwt_token(token.credentials)  # Aqui pegamos o token correto

    # # Buscar os dados do usuário com base no nome de usuário do token
    # user_data = next(
    #     (user for user in credentials["users"] if user["username"] == username), None
    # )

    # if not user_data:
    #     raise HTTPException(status_code=400, detail="Usuário não encontrado.")

    return {
        "payload": payload,
    }  # "roles": user_data["roles"]}
    # return f"The user {username} is authenticated!"


"""
Rotas da API 
"""


@app.get("/consulta/producao/{ano}/token", dependencies=[Depends(BearerToken())])
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):

    area = ProducaoModelo("Produção")
    area = str(area.name)
    subarea = None
    ano = str(ano)

    url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = extrair.formatar_dados(data)

    return data


@app.get("/consulta/comercializacao/{ano}/token", dependencies=[Depends(BearerToken())])
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):

    area = ComercializacaoModelo("Comercialização")
    area = str(area.name)
    subarea = None
    ano = str(ano)

    url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = extrair.formatar_dados(data)

    return data


@app.get("/consulta/processamento/{subarea}/{ano}/token")  # response_class=HTMLResponse
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ProcessamentoSubModelo | None), Path(title="Selecione a subárea de interessse")
    ],
):

    processamento = ProcessamentoModelo("Processamento")
    processamento = str(processamento.name)
    subarea = str(subarea.name)
    ano = str(ano)

    url = requisitar.criar_link(ano=ano, area=processamento, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = extrair.formatar_dados(data)

    return data


@app.get("/consulta/importacao/{subarea}/{ano}/token")  # response_class=HTMLResponse
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ImportacaoSubModelo | None), Path(title="Selecione a subárea de interessse")
    ],
):

    processamento = ImportacaoModelo("Importação")
    processamento = str(processamento.name)
    subarea = str(subarea.name)
    ano = str(ano)

    url = requisitar.criar_link(ano=ano, area=processamento, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = extrair.formatar_dados(data)

    return data


@app.get("/consulta/exportacao/{subarea}/{ano}/token")  # response_class=HTMLResponse
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ExportacaoSubModelo | None), Path(title="Selecione a subárea de interessse")
    ],
):

    processamento = ExportacaoModelo("Exportação")
    processamento = str(processamento.name)
    subarea = str(subarea.name)
    ano = str(ano)

    url = requisitar.criar_link(ano=ano, area=processamento, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = extrair.formatar_dados(data)

    return data
