from typing import Tuple

from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field


class Regular(BaseModel):
    float: str = r"\d+\.\d{2}"


class Default(BaseModel):
    url: str = "https://naveenautomationlabs.com/opencart/"
    driver: str = "chrome"
    timeout: int = 10
    options_filter_in_show: Tuple = ("20", "25", "50", "75", "100")
    options_filter_in_sort_by: Tuple = (
        "Default",
        "Name (A - Z)",
        "Name (Z - A)",
        "Price (Low > High)",
        "Price (High > Low)",
        "Rating (Highest)",
        "Rating (Lowest)",
        "Model (A - Z)",
        "Model (Z - A)",
    )


class Settings(BaseSettings):
    debug: bool = False
    default: Default = Field(default_factory=Default)
    reg: Regular = Field(default_factory=Regular)


settings = Settings()
