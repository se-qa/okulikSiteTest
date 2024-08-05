import allure
import selenium.common.exceptions

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.modules.interaction import ElementInteraction

from tests.data.js_scripts.scripts_utility_functions import js_is_visible_on_screen


class ElementStateChecking:
    def __init__(self, driver: webdriver, element_interaction: ElementInteraction) -> None:
        self.driver = driver
        self.element_interaction = element_interaction

    @allure.step("Check if the current URL matches the specified '{url}'")
    def is_current_url(self, url: str) -> bool:
        """Check if the current URL matches the specified URL"""
        return self.driver.current_url == url

    @allure.step("Checking that the element by locator {locator} is enabled")
    def is_element_enabled(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is enabled"""
        return self.element_interaction.find_element(locator).is_enabled()

    @allure.step("Checking that the element by locator {locator} is selected")
    def is_element_selected(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is selected"""
        return self.element_interaction.find_element(locator).is_selected()

    @allure.step("Checking that the element by locator {locator} is visible")
    def is_element_visible(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is visible"""
        try:
            return self.element_interaction.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return False

    @staticmethod
    @allure.step("Checking that the found element is visible")
    def is_found_element_visible(element: WebElement) -> bool:
        """Check if the found item is visible"""
        return element.is_displayed()

    @allure.step("Checking that the element by locator {locator} is not visible")
    def is_element_not_visible(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is not visible"""
        try:
            return not self.element_interaction.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return True

    @allure.step("Checking that the element by locator {locator} is in viewport")
    def is_element_in_viewport(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is within the viewport"""
        element = self.element_interaction.find_element(locator)
        return js_is_visible_on_screen(self.driver, element)

    @staticmethod
    @allure.step("Check if the number of elements matches the expected length")
    def is_length_of_elements(elements: list[WebElement], length: int) -> bool:
        """Check if the number of elements matches the expected length"""
        return len(elements) == length

    @allure.step("Check if the text of an element specified by the locator contains the specified text")
    def is_element_text_contains_expected_text(self, locator: tuple, text: str) -> bool:
        """Check if the text of an element specified by the locator contains the specified text"""
        element = self.element_interaction.find_element(locator)
        return text in element.text
    