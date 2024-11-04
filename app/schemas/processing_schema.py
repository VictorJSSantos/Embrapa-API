from pydantic import BaseModel, RootModel, Field
from typing import Dict, Optional


class ProcessingDataComposition(BaseModel):
    cultivate: Dict[int, Optional[str]] = Field(alias="Cultivar", default=None)
    quantity: Dict[int, Optional[str]] = Field(alias="Quantidade (Kg)")


class SubareaData(RootModel):
    root: Dict[int, ProcessingDataComposition]


class ProcessingResponseModel(RootModel):
    root: Dict[str, SubareaData]
