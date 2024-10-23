from fastapi import Depends, Path, APIRouter
from typing import Annotated


from app.transformar import Transform
from app.utils import *
from app.models import *
from app.schemas import *
from app.requisicao_http import *
from app.routes.login import *


router = APIRouter()
requisitar = Requisition()
transformar = Transform()


@router.get(
    "/consulta/processamento/{subarea}/{ano}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Quantidade de uvas processadas no Rio Grande do Sul por ano",
    tags=["Processamento"],
    summary="Obter dados de Pocessamento",
)
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ProcessamentoSubModelo | None), Path(title="Selecione a subárea de interessse")
    ],
):
    """
    Rota protegida que irá retornar os dados de Processamento
    """

    area = retornar_name_do_model(Model=ProcessamentoModelo)
    url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
    data = await requisitar.requisicao_get(url=url)
    data = transformar.formatar_dados(data)

    return data


@router.get(
    "/consulta/processamento/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Processamento de <b>todos os anos</b>",
    tags=["Processamento"],
    summary="Obter dados de todos os anos de Processamento",
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Processamento
    """
    area = retornar_name_do_model(Model=ProcessamentoModelo)
    resultados = await transformar.consultar_todas_as_areas(
        area=area, Model=ProcessamentoSubModelo
    )

    return resultados
