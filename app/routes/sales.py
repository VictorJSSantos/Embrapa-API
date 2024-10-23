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
    "/consulta/comercializacao/{ano}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Comercialização de vinhos e derivados no Rio Grande do Sul por ano",
    tags=["Comercialização"],
    summary="Obter dados de Comercialização",
)
async def get_data(
    ano: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):
    """
    Rota protegida que irá retornar os dados de Comercialização
    """

    area = retornar_name_do_model(Model=ComercializacaoModelo)
    url = requisitar.criar_link(
        ano=ano,
        area=area,
    )
    data = requisitar.requisicao_get(url=url)
    data = transformar.formatar_dados(data)

    return data


@router.get(
    "/consulta/comercializacao/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Comercialização de <b>todos os anos</b>",
    tags=["Comercialização"],
    summary="Obter da   dos de todos os anos de Comercialização",
)
async def get_data():
    """
    Rota protegida que irá retornar todos os dados de Comercialização
    """
    area = retornar_name_do_model(Model=ComercializacaoModelo)
    resultados = await transformar.consultar_todo_periodo(
        area=area,
    )

    return resultados
