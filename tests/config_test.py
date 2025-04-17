from pydantic import BaseModel, Field
from typing import List


class Zero(BaseModel):
    url_contains: str = "route=product/manufacturer"
    expected_brands: List[str] = [
        "Apple",
        "Canon",
        "Hewlett-Packard",
        "HTC",
        "Palm",
        "Sony",
    ]
    css_selector: str = ".col-sm-3 a"


class Numbers(BaseModel):
    zero: Zero = Field(default_factory=Zero)
