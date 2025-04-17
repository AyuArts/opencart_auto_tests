from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field




class Default(BaseModel):
    url: str = "https://naveenautomationlabs.com/opencart/"
    driver: str = "chrome"
    timeout: int = 10


class Settings(BaseSettings):
    default: Default = Field(default_factory=Default)



settings = Settings()
