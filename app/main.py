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
from app.routes.manufacturing import router as manufacturing
from app.routes.imports import router as imports
from app.routes.exports import router as exports


# Inicializando o FastAPI
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
transformar = Transform()
requisitar = Requisition()

# Importando as rotas dos seus respectivos arquivos e adicionando no app.
routers = [home, login, production, sales, manufacturing, imports, exports]  #   ]
for router in routers:
    app.include_router(router)
