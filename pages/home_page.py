from pages.base_page import BasePage

from selenium.webdriver.chrome import webdriver

from tests.data.selectors.common_selectors import collapse_cards_active, img_carousel_items


class HomePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
