import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from tests.data.js_scripts.scripts import *


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    # Browser Control
    def open(self, url: str) -> None:
        self.driver.get(url)

    def open_in_new_tab(self, url: str) -> None:
        self.driver.get(url)
        self.switch_to_new_tab()

    def close_current_tab(self) -> None:
        self.driver.close()

    def close_current_tab_and_switch_back(self) -> None:
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit(self) -> None:
        self.driver.quit()

    # Element Interaction
    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple) -> None:
        self.find_element(locator).click()

    def send_keys(self, locator: tuple, text: str) -> None:
        self.find_element(locator).send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_element(locator).text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        return self.find_element(locator).get_attribute(attribute)

    def clear_and_send_keys(self, locator: tuple, text: str) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def native_click_except_js_click(self, locator: tuple) -> None:
        element = self.find_element(locator)
        try:
            element.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            js_click(self.driver, element)

    # Element State Checking
    def is_current_url(self, url: str) -> bool:
        return self.driver.current_url == url

    def is_element_enabled(self, locator: tuple) -> bool:
        return self.find_element(locator).is_enabled()

    def is_element_selected(self, locator: tuple) -> bool:
        return self.find_element(locator).is_selected()

    def is_element_visible(self, locator: tuple) -> bool:
        try:
            return self.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_element_not_visible(self, locator):
        try:
            return not self.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return True

    def is_element_in_viewport(self, locator: tuple) -> bool:
        element = self.find_element(locator)
        return js_is_visible_on_screen(self.driver, element)

    # Frame Handling
    def switch_to_frame(self, locator: tuple) -> None:
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    # Waiting for Conditions
    def wait_for_element_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, locator: tuple[str, str], timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def wait_and_click(self, locator: tuple[str, str], timeout: int = 10) -> None:
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def wait_for_scroll_to_element(self, locator: tuple, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.is_element_in_viewport(locator),
            message=f"Timed out waiting for element {locator} to be in viewport"
        )

    # Utility Functions
    def scroll_to_element_center_of_screen(self, locator: tuple) -> None:
        element = self.find_element(locator)
        js_scroll_element_to_center_of_screen(self.driver, element)

    def scroll_to_element_top_of_screen(self, locator: tuple) -> None:
        element = self.find_element(locator)
        js_scroll_element_to_top_of_screen(self.driver, element)

    def scroll_to_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        js_scroll_to_element(self.driver, element)
        self.wait_for_scroll_to_element(locator)

    def execute_script(self, script: str, *args) -> None:
        return self.driver.execute_script(script, *args)

    def select_by_value(self, locator: tuple, value: str) -> None:
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def select_by_visible_text(self, locator: tuple, text: str) -> None:
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def hover_over_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def take_screenshot(self, filename: str) -> None:
        self.driver.get_screenshot_as_file(filename)

    def switch_to_new_tab(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])
