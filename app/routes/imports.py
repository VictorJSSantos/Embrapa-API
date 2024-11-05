from fastapi import Depends, Path, APIRouter
from typing import Annotated

from app.transform import Transform
from app.utils import *
from app.models import *
from app.schemas import *
from app.http_requisition import *
from app.routes.login import *
from app.schemas.imports_schema import *


router = APIRouter()
request = Requisition()
transform = Transform()


@router.get(
    "c",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Importação de derivados de uva por ano",
    tags=["Importação"],
    summary="Obter dados de Importação",
    response_model=ImportsDataComposition,
)
async def get_data(
    year: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        ImportsSubModel, Path(title="Selecione a subárea de interessse")
    ],
):
    """
    Rota protegida que irá retornar os dados de Importação
    """
    area = return_name_from_model(Model=ImportsModel)
    subarea = return_name_from_model(Model=ImportsSubModel)
    url = request.create_url_link(year=year, area=area, subarea=subarea)
    data = await request.get_requisition(url=url)
    data = transform.format_data(data)

    return data


@router.get(
    "/consulta/importacao/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Importação de <b>todos os anos</b>",
    tags=["Importação"],
    summary="Obter dados de todos os anos de Importação",
    response_model=ImportsResponseModel,
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Importação
    """
    area = return_name_from_model(Model=ImportsModel)
    resultados = await transform.get_data_from_all_areas(
        area=area, SubModel=ImportsSubModel
    )

    return resultados
