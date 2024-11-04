from pydantic import BaseModel, RootModel, Field
from typing import Dict, Optional


class ImportsDataComposition(BaseModel):
    countries: Dict[int, Optional[str]] = Field(alias="Países")
    quantity: Dict[int, Optional[str]] = Field(alias="Quantidade (Kg)")
    value: Dict[int, Optional[str]] = Field(alias="Valor (US$)")


class SubareaData(RootModel):
    root: Dict[int, ImportsDataComposition]


class ImportsResponseModel(RootModel):
    root: Dict[str, SubareaData]
