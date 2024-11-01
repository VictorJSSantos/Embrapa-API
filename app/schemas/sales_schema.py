from pydantic import BaseModel, RootModel
from typing import Dict, Any


class SalesDataComposition(BaseModel):
    Produto: Dict[str, Any]  # Permite qualquer tipo de valor
    Quantidade_Litros: Dict[str, Any]  # Permite qualquer tipo de valor


class SalesResponseModel(RootModel):
    Dict[str, SalesDataComposition]  # Mapeia cada ano aos dados anuais
