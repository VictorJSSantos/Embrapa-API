from fastapi import Depends, Path, APIRouter

from app.transform import Transform
from app.utils import *
from app.models import *
from app.schemas import *
from app.http_requisition import *
from app.routes.login import *


router = APIRouter()
request = Requisition()
transform = Transform()


@router.get(
    "/consulta/comercializacao/{year}/token",
    dependencies=[Depends(BearerToken())],
    description="Requisitar dados de Comercialização de vinhos e derivados no Rio Grande do Sul por ano",
    tags=["Comercialização"],
    summary="Obter dados de Comercialização",
)
async def get_data(
    year: Annotated[int, Path(title="Selecione o ano de interesse", ge=1970, le=2022)]
):
    """
    Rota protegida que irá retornar os dados de Comercialização
    """

    area = return_name_from_model(Model=ComercializacaoModelo)
    url = request.create_url_link(
        year=year,
        area=area,
    )
    data = await request.get_requisition(url=url)
    data = transform.format_data(data)

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
    area = return_name_from_model(Model=ComercializacaoModelo)
    resultados = await transform.get_all_data(
        area=area,
    )

    return resultados
