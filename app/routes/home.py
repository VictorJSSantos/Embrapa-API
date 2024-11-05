from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


"""
Rota da Home
"""


@router.get("/", tags=["Default"], summary="Página Inicial")
async def route_default():
    return "<html><body><h1>Hello, World!</h1></body></html>"
    # return RedirectResponse(url="/docs")
