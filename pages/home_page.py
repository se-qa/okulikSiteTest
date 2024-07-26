from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests.data.selectors.common_selectors import collapse_cards_active
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_all_elements_with_class(self, locator, text):
        elements = self.find_elements(locator)
        for element in elements:
            element.click()
            assert text not in element.get_attribute("class")
            self.wait_for_element_visible(collapse_cards_active)
            element.click()
            assert text in element.get_attribute("class")
            self.wait_for_element_to_disappear(collapse_cards_active)
            # sleep(1)
