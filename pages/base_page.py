import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from tests.data.js_scripts.scripts import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Browser Control
    def open(self, url):
        self.driver.get(url)

    def open_in_new_tab(self, url):
        self.driver.get(url)
        self.switch_to_new_tab()

    def close_current_tab(self):
        self.driver.close()

    def close_current_tab_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit(self):
        self.driver.quit()

    # Element Interaction
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def clear_and_send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def native_click_except_js_click(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            js_click(self.driver, element)

    # Element State Checking
    def is_current_url(self, url):
        return self.driver.current_url == url

    def is_element_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def is_element_selected(self, locator):
        return self.find_element(locator).is_selected()

    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_element_in_viewport(self, locator):
        element = self.find_element(locator)
        return js_is_visible_on_screen(self.driver, element)

    # Frame Handling
    def switch_to_frame(self, locator):
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # Waiting for Conditions
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def wait_and_click(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def wait_for_scroll_to_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.is_element_in_viewport(locator),
            message=f"Timed out waiting for element {locator} to be in viewport"
        )

    # Utility Functions
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        js_scroll_to_element(self.driver, element)
        self.wait_for_element_visible(locator)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def select_by_value(self, locator, value):
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def select_by_visible_text(self, locator, text):
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def hover_over_element(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
