from fastapi import Depends, Path, APIRouter
from typing import Annotated


from app.transform import TransformRequisition
from app.utils import *
from app.models import *
from app.http_requisition import *
from app.routes.login import *
from app.schemas.production_schema import *


router = APIRouter()
request = Requisition()
transform = TransformRequisition()

"""
Rota de API que coleta dados de um ano específico os anos
"""


@router.get(
    "/consulta/producao/{year}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Produção de vinhos, sucos e derivados do Rio Grande do Sul por ano",
    tags=["Produção"],
    summary="Obter dados de Produção",
    response_model=ProductionDataComposition,
)
async def get_data(
    year: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):
    """
    Rota protegida que irá retornar os dados de Produção
    """

    area = return_name_from_model(Model=ProductionModel)
    url = request.create_url_link(year=year, area=area)
    data = await request.get_requisition(url=url)
    data = transform.format_data(data)

    return data


"""
Rota de API que coleta dados de TODOS os anos - Foi limitado por causa da consante queda da API Embrapa.
"""


@router.get(
    "/consulta/producao/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Produção de <b>todos os anos</b>",
    tags=["Produção"],
    summary="Obter dados de todos os anos de Produção",
    response_model=ProductionResponseModel,
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de todos os anos da subárea Produção.
    """
    area = return_name_from_model(Model=ProductionModel)
    response = await transform.get_all_data(
        area=area,
    )

    return response
