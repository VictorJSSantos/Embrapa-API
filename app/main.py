from fastapi import FastAPI, HTTPException, Depends, Path

# from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# from app.transform import TransformRequisition
# from app.http_requisition import Requisition

# from models import *
# from utils import *


from app.routes.home import router as home
from app.routes.login import router as login
from app.routes.production import router as production
from app.routes.sales import router as sales
from app.routes.processing import router as processing
from app.routes.imports import router as imports
from app.routes.exports import router as exports


# Inicializando o FastAPI
app = FastAPI(openapi_url="/openapi.json")
# transform = TransformRequisition()
# request = Requisition()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Altere isso para permitir apenas os domínios desejados
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importando as rotas dos seus respectivos arquivos e adicionando no app.
routers = [home, login, production, sales, processing, imports, exports]
for router in routers:
    app.include_router(router)
