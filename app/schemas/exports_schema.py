from pydantic import BaseModel, RootModel
from typing import Dict, Any


class ExportsDataComposition(BaseModel):
    Paises: Dict[str, Any]
    Quantidade_Kg: Dict[str, Any]
    Valor_USD: Dict[str, Any]


class ExportsResponseModel(RootModel):
    Dict[str, ExportsDataComposition]  # Mapeia cada ano aos dados anuais
