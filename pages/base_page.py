import selenium.common.exceptions

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from tests.data.js_scripts.scripts_page_interaction import *
from tests.data.js_scripts.scripts_utility_functions import *
from tests.data.js_scripts.scripts_element_interaction import *

from tests.data.selectors.common_selectors import img_carousel_items, collapse_cards_active


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    # Browser Control
    def open(self, url: str) -> None:
        """Open the specified URL in the browser"""
        self.driver.get(url)

    def open_in_new_tab(self, url: str) -> None:
        """Open the specified URL in a new tab and switch to it"""
        self.driver.get(url)
        self.switch_to_new_tab()

    def close_current_tab(self) -> None:
        """Close the current tab"""
        self.driver.close()

    def close_current_tab_and_switch_back(self) -> None:
        """Close the current tab and switch to the last opened tab"""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit(self) -> None:
        """Quit the browser session"""
        self.driver.quit()

    # Element Interaction
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

    # Element State Checking
    def is_current_url(self, url: str) -> bool:
        """Check if the current URL matches the specified URL"""
        return self.driver.current_url == url

    def is_element_enabled(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is enabled"""
        return self.find_element(locator).is_enabled()

    def is_element_selected(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is selected"""
        return self.find_element(locator).is_selected()

    def is_element_visible(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is visible"""
        try:
            return self.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_element_not_visible(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is not visible"""
        try:
            return not self.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return True

    def is_element_in_viewport(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is within the viewport"""
        element = self.find_element(locator)
        return js_is_visible_on_screen(self.driver, element)

    @staticmethod
    def is_length_of_elements(elements: list[WebElement], length: int) -> bool:
        """Check if the number of elements matches the expected length"""
        return len(elements) == length

    def is_element_text_contains_expected_text(self, locator: tuple, text: str) -> bool:
        """Check if the text of an element specified by the locator contains the specified text"""
        element = self.find_element(locator)
        return text in element.text

    # Frame Handling
    def switch_to_frame(self, locator: tuple) -> None:
        """Switch to the frame specified by the locator"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self) -> None:
        """Switch back to the default content from an iframe"""
        self.driver.switch_to.default_content()

    # Waiting for Conditions
    def wait_for_element_visible_by_locator(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """Wait for an element specified by the locator to be visible"""
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_visible_by_element(self, element: WebElement, timeout: int = 10) -> WebElement:
        """Wait for an element to be visible"""
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of(element))

    def wait_for_element_clickable(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """Wait for an element specified by the locator to be clickable"""
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """Wait for an element specified by the locator to disappear"""
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def wait_and_click(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """Wait for an element specified by the locator to be clickable and click it"""
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def wait_for_scroll_to_element(self, locator: tuple, timeout: int = 10) -> None:
        """Wait for an element to be in the viewport after scrolling to it"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.is_element_in_viewport(locator),
            message=f"Timed out waiting for element {locator} to be in viewport"
        )

    # Utility Functions
    def scroll_to_element_center_of_screen(self, locator: tuple) -> None:
        """Scroll to the center of the screen for the element specified by the locator"""
        element = self.find_element(locator)
        js_scroll_element_to_center_of_screen(self.driver, element)

    def scroll_to_element_top_of_screen(self, locator: tuple) -> None:
        """Scroll to the top of the screen for the element specified by the locator"""
        element = self.find_element(locator)
        js_scroll_element_to_top_of_screen(self.driver, element)

    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll to the element specified by the locator"""
        element = self.find_element(locator)
        js_scroll_to_element(self.driver, element)
        self.wait_for_scroll_to_element(locator)

    def execute_script(self, script: str, *args) -> None:
        """Execute the specified JavaScript script"""
        return self.driver.execute_script(script, *args)

    def select_by_value(self, locator: tuple, value: str) -> None:
        """Select an option by value from a dropdown element specified by the locator"""
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def select_by_visible_text(self, locator: tuple, text: str) -> None:
        """Select an option by visible text from a dropdown element specified by the locator"""
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def hover_over_element(self, locator: tuple) -> None:
        """Hover over an element specified by the locator"""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot and save it to the specified filename"""
        self.driver.get_screenshot_as_file(filename)

    def switch_to_new_tab(self) -> None:
        """Switch to the newly opened tab"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_all_carousel_elements(self, locator: tuple) -> None:
        elements = self.find_elements(locator)
        target = self.find_elements(img_carousel_items)
        assert self.is_length_of_elements(elements, len(target)), (f"Expected {len(elements)} elements, "
                                                                   + f"but found {len(target)} elements")

        for index, element in enumerate(elements):
            element.click()
            self.wait_for_element_visible_by_element(target[index])
            assert target[index].is_displayed(), f"Element at index {index} is not displayed after clicking"

    def click_all_collapse_elements(self, locator: tuple, text: str) -> None:
        elements = self.find_elements(locator)

        for element in elements:
            element.click()
            assert text not in element.get_attribute("class"), f"Expected '{text}' to not be in class after first click"
            self.wait_for_element_visible_by_locator(collapse_cards_active)
            element.click()
            assert text in element.get_attribute("class"), f"Expected '{text}' to be in class after second click"
            self.wait_for_element_to_disappear(collapse_cards_active)
