from pydantic import BaseModel, RootModel, Field
from typing import Dict, Optional


class ProductionDataComposition(BaseModel):
    product: Dict[int, Optional[str]] = Field(alias="Produto")
    quantity: Dict[int, Optional[str]] = Field(alias="Quantidade (L.)")


class ProductionResponseModel(RootModel):
    root: Dict[str, ProductionDataComposition]
