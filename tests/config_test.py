from pydantic import BaseModel, Field
from typing import List, Dict


from core.random_user import user


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


class One(BaseModel):
    dropdown: str = '//*[@id="top-links"]/ul/li[2]/a/span[2]'
    element_reg: str = '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
    url_reg: str = "route=account/register"
    fields_regs: Dict[str, str] = {
        "input-firstname": user.first_name,
        "input-lastname": user.last_name,
        "input-email": user.email,
        "input-telephone": user.phone,
        "input-password": user.password,
        "input-confirm": user.password,
    }

    check_box: str = '//*[@id="content"]/form/div/div/input[1]'
    button_continue: str = '//*[@id="content"]/form/div/div/input[2]'
    url_approve_reg: str = "route=account/success"
    text_correct: str = "h1"
    text_expected: str = "Your Account Has Been Created!"


class Numbers(BaseModel):
    zero: Zero = Field(default_factory=Zero)
    one: One = Field(default_factory=One)
