from pydantic import BaseModel, RootModel
from typing import Dict, Any


class ProductionDataComposition(BaseModel):
    Produto: Dict[str, Any]  # Permite qualquer tipo de valor
    Quantidade_Litros: Dict[str, Any]  # Permite qualquer tipo de valor


class ProductionResponseModel(RootModel):
    Dict[str, ProductionDataComposition]  # Mapeia cada ano aos dados anuais
