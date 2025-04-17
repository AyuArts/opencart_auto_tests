from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field
from tests.config_test import Numbers


class Default(BaseModel):
    url: str = "https://naveenautomationlabs.com/opencart/"
    driver: str = "chrome"
    timeout: int = 10
    debug: bool = True


class Settings(BaseSettings):
    default: Default = Field(default_factory=Default)
    tests: Numbers = Field(default_factory=Numbers)


settings = Settings()
