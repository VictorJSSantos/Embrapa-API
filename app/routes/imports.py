from fastapi import Depends, Path, APIRouter

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
    "/consulta/importacao/{subarea}/{ano}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Importação de derivados de uva por ano",
    tags=["Importação"],
    summary="Obter dados de Importação",
)
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)],
    subarea: Annotated[
        (ImportacaoSubModelo | None), Path(title="Selecione a subárea de interessse")
    ],
):
    """
    Rota protegida que irá retornar os dados de Importação
    """
    area = retornar_name_do_model(Model=ImportacaoModelo)
    subarea = retornar_name_do_model(Model=ImportacaoSubModelo)
    url = requisitar.criar_link(ano=ano, area=area, subarea=subarea)
    data = requisitar.requisicao_get(url=url)
    data = transformar.formatar_dados(data)

    return data


@router.get(
    "/consulta/importacao/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Importação de <b>todos os anos</b>",
    tags=["Importação"],
    summary="Obter dados de todos os anos de Importação",
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Importação
    """
    area = retornar_name_do_model(Model=ImportacaoModelo)
    resultados = await transformar.consultar_todas_as_areas(
        area=area, SubModel=ImportacaoSubModelo
    )

    return resultados