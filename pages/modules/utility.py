from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select

from pages.modules.interaction import ElementInteraction

from tests.data.js_scripts.scripts_element_interaction import js_scroll_to_element
from tests.data.js_scripts.scripts_page_interaction import js_scroll_element_to_center_of_screen, \
    js_scroll_element_to_top_of_screen


class UtilityFunctions:
    def __init__(self, driver: webdriver, element_interaction: ElementInteraction) -> None:
        self.driver = driver
        self.element_interaction = element_interaction

    def scroll_to_element_center_of_screen(self, locator: tuple) -> None:
        """Scroll to the center of the screen for the element specified by the locator"""
        element = self.element_interaction.find_element(locator)
        js_scroll_element_to_center_of_screen(self.driver, element)

    def scroll_to_element_top_of_screen(self, locator: tuple) -> None:
        """Scroll to the top of the screen for the element specified by the locator"""
        element = self.element_interaction.find_element(locator)
        js_scroll_element_to_top_of_screen(self.driver, element)

    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll to the element specified by the locator"""
        element = self.element_interaction.find_element(locator)
        js_scroll_to_element(self.driver, element)

    def execute_script(self, script: str, *args) -> None:
        """Execute the specified JavaScript script"""
        return self.driver.execute_script(script, *args)

    def select_by_value(self, locator: tuple, value: str) -> None:
        """Select an option by value from a dropdown element specified by the locator"""
        select_element = self.element_interaction.find_element(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def select_by_visible_text(self, locator: tuple, text: str) -> None:
        """Select an option by visible text from a dropdown element specified by the locator"""
        select_element = self.element_interaction.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def hover_over_element(self, locator: tuple) -> None:
        """Hover over an element specified by the locator"""
        element = self.element_interaction.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot and save it to the specified filename"""
        self.driver.get_screenshot_as_file(filename)
