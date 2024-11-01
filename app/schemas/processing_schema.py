from pydantic import BaseModel, RootModel
from typing import Dict, Any


class ProcessingDataComposition(BaseModel):
    Cultivar: Dict[str, Any]  # Permite qualquer tipo de valor
    Quantidade_Kg: Dict[str, Any]  # Permite qualquer tipo de valor


class ProcessingResponseModel(RootModel):
    Dict[str, ProcessingDataComposition]  # Mapeia cada ano aos dados anuais
