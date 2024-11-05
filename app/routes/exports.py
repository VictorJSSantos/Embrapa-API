from fastapi import Depends, Path, APIRouter
from typing import Annotated

from app.transform import Transform
from app.utils import *
from app.models import *
from app.schemas import *
from app.http_requisition import *
from app.routes.login import *
from app.schemas.exports_schema import *


router = APIRouter()
request = Requisition()
transform = Transform()


@router.get(
    "/consulta/exportacao/{subarea}/{year}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Exportação de derivados de uva por ano",
    tags=["Exportação"],
    summary="Obter dados de Exportação",
    response_model=ExportsDataComposition,
)
async def get_data(
    year: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        ExportsSubModel, Path(title="Selecione a subárea de interessse")
    ],
):
    """
    Rota protegida que irá retornar os dados de Exportação
    """
    area = return_name_from_model(Model=ExportsModel)
    subarea = return_name_from_model(Model=ExportsSubModel)
    url = request.create_url_link(year=year, area=area, subarea=subarea)
    data = await request.get_requisition(url=url)
    data = transform.format_data(data)

    return data


@router.get(
    "/consulta/exportacao/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Exportação de <b>todos os anos</b> para uma das subareas.",
    tags=["Exportação"],
    summary="Obter dados de todos os anos de Exportação",
    response_model=ExportsResponseModel,
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Exportação
    """
    area = return_name_from_model(Model=ExportsModel)
    resultados = await transform.get_data_from_all_areas(
        area=area, SubModel=ExportsSubModel
    )

    return resultados
