from pydantic import BaseModel, RootModel, Field
from typing import Dict, Optional


class SalesDataComposition(BaseModel):
    Product: Dict[int, Optional[str]] = Field(alias="Produto")
    Quantity: Dict[int, Optional[str]] = Field(alias="Quantidade (L.)")


class SalesResponseModel(RootModel):
    root: Dict[str, SalesDataComposition]  # Mapeia cada ano aos dados anuais
