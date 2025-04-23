from abc import ABC

from selenium.webdriver.common.by import By


class Locators(ABC):
    VALID_BY_VALUES = {
        By.ID,
        By.XPATH,
        By.LINK_TEXT,
        By.PARTIAL_LINK_TEXT,
        By.NAME,
        By.TAG_NAME,
        By.CLASS_NAME,
        By.CSS_SELECTOR,
    }

    def __init_subclass__(cls):
        for attr_name, value in cls.__dict__.items():
            if attr_name.startswith("__") or callable(value):
                continue

            if not isinstance(value, tuple):
                raise ValueError(f"Locator '{attr_name}' is not a tuple: {value}")

            if len(value) != 2:
                raise ValueError(f"Locator '{attr_name}' must have 2 elements: {value}")

            by, selector = value
            if by not in cls.VALID_BY_VALUES:
                raise ValueError(f"Locator '{attr_name}' has invalid By method: {by}")

            if not isinstance(selector, str) or not selector.strip():
                raise ValueError(
                    f"Locator '{attr_name}' has invalid selector: {selector}"
                )
