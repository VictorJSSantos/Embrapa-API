from pydantic import BaseModel, RootModel, Field
from typing import Dict, Optional


class ExportsDataComposition(BaseModel):
    countries: Dict[int, Optional[str]] = Field(alias="Países")
    quantity: Dict[int, Optional[str]] = Field(alias="Quantidade (Kg)")
    value: Dict[int, Optional[str]] = Field(alias="Valor (US$)")


class SubareaData(RootModel):
    root: Dict[int, ExportsDataComposition]


class ExportsResponseModel(RootModel):
    root: Dict[str, SubareaData]
