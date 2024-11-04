from fastapi import FastAPI, HTTPException, Depends, Path

from app.transform import Transform
from app.http_requisition import Requisition
from app.models import *
from app.utils import *


from app.routes.home import router as home
from app.routes.login import router as login
from app.routes.production import router as production
from app.routes.sales import router as sales
from app.routes.processing import router as processing
from app.routes.imports import router as imports
from app.routes.exports import router as exports


# Inicializando o FastAPI
app = FastAPI()
transform = Transform()
request = Requisition()

# Importando as rotas dos seus respectivos arquivos e adicionando no app.
routers = [home, login, production, sales, processing, imports, exports]
for router in routers:
    app.include_router(router)
