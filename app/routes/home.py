from fastapi import APIRouter

router = APIRouter()


"""
Rota da Home
"""


@router.get("/", tags=["Default"], summary="Página Inicial")
async def route_default():
    return "Bem vindo à API da Embrapa! Acesse /docs para a documentação!"
