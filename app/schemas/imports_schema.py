from pydantic import BaseModel, RootModel
from typing import Dict, Any


class ImportsDataComposition(BaseModel):
    Paises: Dict[str, Any]
    Quantidade_Kg: Dict[str, Any]  # Permite qualquer tipo de valor
    Valor_USD: Dict[str, Any]  # Permite qualquer tipo de valor


class ImportsResponseModel(RootModel):
    Dict[str, ImportsDataComposition]  # Mapeia cada ano aos dados anuais
