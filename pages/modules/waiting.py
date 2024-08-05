from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

from pages.modules.checking import ElementStateChecking


class WaitingConditions:
    def __init__(self, driver: webdriver, element_state_checking: ElementStateChecking) -> None:
        self.driver = driver
        self.element_state_checking = element_state_checking

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
            lambda driver: self.element_state_checking.is_element_in_viewport(locator),
            message=f"Timed out waiting for element {locator} to be in viewport"
        )
