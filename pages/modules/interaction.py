import selenium.common.exceptions

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement

from tests.data.js_scripts.scripts_element_interaction import js_click


class ElementInteraction:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def find_element(self, locator: tuple) -> WebElement:
        """Find a single element by locator"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Find multiple elements by locator"""
        return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple) -> None:
        """Click on an element specified by the locator"""
        self.find_element(locator).click()

    def send_keys(self, locator: tuple, text: str) -> None:
        """Send keys to an element specified by the locator"""
        self.find_element(locator).send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text of an element specified by the locator"""
        return self.find_element(locator).text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Get attribute value of an element specified by the locator"""
        return self.find_element(locator).get_attribute(attribute)

    def clear_and_send_keys(self, locator: tuple, text: str) -> None:
        """Clear the element's content and send keys"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def native_click_except_js_click(self, locator: tuple) -> None:
        """Attempt to click the element natively, fallback to JS click if it fails"""
        element = self.find_element(locator)
        try:
            element.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            js_click(self.driver, element)
