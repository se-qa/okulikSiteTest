from pages.base_page import BasePage

from selenium.webdriver.chrome import webdriver


class HomePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
