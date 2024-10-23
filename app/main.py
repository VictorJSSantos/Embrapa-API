# from utils.functions import *
import jwt
import datetime
import yaml
from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer
from bs4 import BeautifulSoup

from typing import Optional
import requests
from fastapi.responses import HTMLResponse
from app.transformar import Transform
from app.requisicao_http import Requisition
from app.models import *
from app.schemas import *
from app.utils import *
from typing import Annotated

from app.routes.home import router as home
from app.routes.login import router as login
from app.routes.production import router as production
from app.routes.sales import router as sales
from app.routes.imports import router as imports
from app.routes.exports import router as exports


# Inicializando o FastAPI
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
transformar = Transform()
requisitar = Requisition()

# Importando as rotas dos seus respectivos arquivos e adicionando no app.
routers = [home, login, production, sales, imports, exports]  #   ]
for router in routers:
    app.include_router(router)


# """
# Rotas de Autorização
# """

# credentials = load_credentials()
# SECRET_KEY = credentials["SECRET_KEY"]


# # Classe para autenticação Bearer
# class BearerToken(HTTPBearer):
#     def __init__(self):
#         super().__init__()


# @app.get("/", tags=["Default"], summary="Página Inicial")
# async def route_default():
#     return "Aqui é a API Embrapa"


# # Rota para login que retorna o token JWT
# @app.post(
#     "/token",
#     tags=["Login"],
#     summary="Enviar dados de usuário para fazer login",
#     response_model=TokenResponse,
# )
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     """
#     Rota de login que valida as credenciais e retorna um token JWT.
#     """
#     user_data = next(
#         (
#             user
#             for user in credentials["users"]
#             if user["username"] == form_data.username
#             and user["password"] == form_data.password
#         ),
#         None,
#     )

#     if not user_data:
#         raise HTTPException(status_code=400, detail="Usuário ou senha inválidos.")

#     token = create_jwt_token(user_data["username"], user_data["password"])
#     return {"access_token": token, "token_type": "bearer"}


# # Rota protegida que retorna informações do usuário com base no token JWT
# @app.get(
#     "/users/login/token",
#     dependencies=[Depends(BearerToken())],
#     tags=["Login"],
#     summary="Obter dados do usuário validado",
#     response_model=UserPayload,
# )
# async def read_users_me():  # token: str = Depends(BearerToken())
#     """
#     Rota protegida que retorna as informações do usuário.
#     """
#     token = BearerToken()
#     payload = verify_jwt_token(token.credentials)  # Aqui pegamos o token correto

#     return {
#         "payload": payload,
#     }


# """
# Rotas da API
# """


# @app.get(
#     "/consulta/producao/{ano}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Produção de vinhos, sucos e derivados do Rio Grande do Sul por ano",
#     tags=["Produção"],
#     summary="Obter dados de Produção",
# )
# async def get_data(
#     ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
# ):
#     """
#     Rota protegida que irá retornar os dados de Produção
#     """

#     area = ProducaoModelo("Produção")
#     area = str(area.name)
#     subarea = None
#     ano = str(ano)

#     url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
#     data = requisitar.requisicao_get(url=url)
#     data = transformar.formatar_dados(data)

#     return data


# @app.get(
#     "/consulta/comercializacao/{ano}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Comercialização de vinhos e derivados no Rio Grande do Sul por ano",
#     tags=["Comercialização"],
#     summary="Obter dados de Comercialização",
# )
# async def get_data(
#     ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
# ):
#     """
#     Rota protegida que irá retornar os dados de Comercialização
#     """
#     area = ComercializacaoModelo("Comercialização")
#     area = str(area.name)
#     subarea = None
#     ano = str(ano)

#     url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
#     data = requisitar.requisicao_get(url=url)
#     data = transformar.formatar_dados(data)

#     return data


# @app.get(
#     "/consulta/processamento/{subarea}/{ano}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Quantidade de uvas processadas no Rio Grande do Sul por ano",
#     tags=["Processamento"],
#     summary="Obter dados de Pocessamento",
# )
# async def get_data(
#     ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
#     subarea: Annotated[
#         (ProcessamentoSubModelo | None), Path(title="Selecione a subárea de interessse")
#     ],
# ):
#     """
#     Rota protegida que irá retornar os dados de Processamento
#     """

#     area = retornar_name_do_model(Model=ProcessamentoModelo)
#     url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
#     data = requisitar.requisicao_get(url=url)
#     data = transformar.formatar_dados(data)

#     return data


# @app.get(
#     "/consulta/importacao/{subarea}/{ano}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Importação de derivados de uva por ano",
#     tags=["Importação"],
#     summary="Obter dados de Importação",
# )
# async def get_data(
#     ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
#     subarea: Annotated[
#         (ImportacaoSubModelo | None), Path(title="Selecione a subárea de interessse")
#     ],
# ):
#     """
#     Rota protegida que irá retornar os dados de Importação
#     """
#     area = retornar_name_do_model(Model=ProcessamentoModelo)
#     url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
#     data = requisitar.requisicao_get(url=url)
#     data = transformar.formatar_dados(data)

#     return data


# @app.get(
#     "/consulta/exportacao/{subarea}/{ano}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Exportação de derivados de uva por ano",
#     tags=["Exportação"],
#     summary="Obter dados de Exportação",
# )
# async def get_data(
#     ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
#     subarea: Annotated[
#         (ExportacaoSubModelo | None), Path(title="Selecione a subárea de interessse")
#     ],
# ):
#     """
#     Rota protegida que irá retornar os dados de Exportação
#     """
#     processamento = ExportacaoModelo("Exportação")
#     processamento = str(processamento.name)
#     subarea = str(subarea.name)
#     ano = str(ano)

#     url = requisitar.criar_link(ano=ano, area=processamento, subarea=subarea)
#     data = requisitar.requisicao_get(url=url)
#     data = transformar.formatar_dados(data)

#     return data


# """
# Rotas de API que coletam dados de TODOS os anos
# """


# @app.get(
#     "/consulta/producao/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Produção de <b>todos os anos</b>",
#     tags=["Produção"],
#     summary="Obter dados de todos os anos de Produção",
# )
# async def get_data():
#     """
#     Rota protegida que irá retornar todos os dados de Produção
#     """
#     area = ProducaoModelo("Produção")
#     area = str(area.name)
#     # subarea = str(subarea.name)
#     response = await transformar.consultar_todo_periodo(
#         area=area,
#     )

#     return response


# @app.get(
#     "/consulta/comercializacao/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Comercialização de <b>todos os anos</b>",
#     tags=["Comercialização"],
#     summary="Obter dados de todos os anos de Comercialização",
# )
# async def get_data():
#     """
#     Rota protegida que irá retornar todos os dados de Comercialização
#     """
#     area = ComercializacaoModelo("Comercialização")
#     area = str(area.name)
#     resultados = transformar.consultar_todo_periodo(
#         area=area,
#     )

#     return resultados


# @app.get(
#     "/consulta/processamento/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Processamento de <b>todos os anos</b>",
#     tags=["Processamento"],
#     summary="Obter dados de todos os anos de Processamento",
# )
# async def get_data():
#     """
#     Rota protegida que irá retornar todos os dados de Processamento
#     """
#     area = ProcessamentoModelo("Processamento")
#     area = str(area.name)
#     resultados = transformar.consultar_todas_as_areas(
#         area=area, Model=ProcessamentoSubModelo
#     )

#     return resultados


# @app.get(
#     "/consulta/importacao/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Importação de <b>todos os anos</b>",
#     tags=["Importação"],
#     summary="Obter dados de todos os anos de Importação",
# )
# async def get_data():
#     """
#     Rota protegida que irá retornar todos os dados de Importação
#     """
#     area = ImportacaoModelo("Importação")
#     area = str(area.name)
#     resultados = transformar.consultar_todas_as_areas(
#         area=area, Model=ImportacaoSubModelo
#     )

#     return resultados


# @app.get(
#     "/consulta/exportacao/{subarea}/token",
#     dependencies=[Depends(BearerToken())],
#     description="Requisitar dados de Exportação de <b>todos os anos</b> para uma das subareas.",
#     tags=["Exportação"],
#     summary="Obter dados de todos os anos de Exportação",
# )
# async def get_data():
#     """
#     Rota protegida que irá retornar todos os dados de Exportação
#     """
#     area = ExportacaoModelo("Exportação")
#     area = str(area.name)
#     resultados = await transformar.consultar_todas_as_areas(
#         area=area, Model=ExportacaoSubModelo
#     )

#     return resultados
