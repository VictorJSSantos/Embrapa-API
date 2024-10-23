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

"""
Rota de API que coleta dados de um ano específico os anos
"""


@router.get(
    "/consulta/producao/{ano}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Produção de vinhos, sucos e derivados do Rio Grande do Sul por ano",
    tags=["Produção"],
    summary="Obter dados de Produção",
)
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):
    """
    Rota protegida que irá retornar os dados de Produção
    """

    area = retornar_name_do_model(Model=ProducaoModelo)
    url = requisitar.criar_link(ano=ano, area=area)
    data = requisitar.requisicao_get(url=url)
    data = transformar.formatar_dados(data)

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
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Produção
    """
    area = retornar_name_do_model(Model=ProducaoModelo)
    response = await transformar.consultar_todo_periodo(
        area=area,
    )

    return response
