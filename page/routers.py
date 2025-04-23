from pydantic_settings import BaseSettings


class Routers(BaseSettings):
    BRANDS_URL: str = "route=product/manufacturer"
    IPHONE_URL: str = "route=product/product&product_id=40"
    CAMERAS_URL: str = "route=product/category&path=33"
    SHOW_ALL_URL: str = "route=product/category&path=20"
    REGISTER_URL: str = "route=account/register"
    SUBMIT_REGISTER_URL: str = "route=account/success"


routers = Routers()
