from fastapi import Depends, Path, APIRouter
from typing import Annotated


from app.transform import Transform
from app.utils import *
from app.models import *
from app.schemas import *
from app.http_requisition import *
from app.routes.login import *
from app.schemas.processing_schema import *


router = APIRouter()
request = Requisition()
transform = Transform()


@router.get(
    "/consulta/processamento/{subarea}/{year}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Quantidade de uvas processadas no Rio Grande do Sul por ano",
    tags=["Processamento"],
    summary="Obter dados de Pocessamento",
    response_model=ProcessingDataComposition,
)
async def get_data(
    year: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ProcessingSubModel | None), Path(title="Selecione a subárea de interessse")
    ],
):
    """
    Rota protegida que irá retornar os dados de Processamento
    """

    area = return_name_from_model(Model=ProcessingModel)
    subarea = return_name_from_model(Model=ProcessingSubModel)
    url = request.create_url_link(year=year, area=area, subarea=subarea)
    data = await request.get_requisition(url=url)
    data = transform.format_data(data)

    return data


@router.get(
    "/consulta/processamento/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Processamento de <b>todos os anos</b>",
    tags=["Processamento"],
    summary="Obter dados de todos os anos de Processamento",
    response_model=ProcessingResponseModel,
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Processamento
    """
    area = return_name_from_model(Model=ProcessingModel)
    resultados = await transform.get_data_from_all_areas(
        area=area, SubModel=ProcessingSubModel
    )

    return resultados
