from selenium.webdriver.chrome import webdriver

from pages.modules.frame import FrameHandling
from pages.modules.browser import BrowserControl
from pages.modules.utility import UtilityFunctions
from pages.modules.waiting import WaitingConditions
from pages.modules.checking import ElementStateChecking
from pages.modules.interaction import ElementInteraction


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.browser_control = BrowserControl(driver)
        self.element_interaction = ElementInteraction(driver)
        self.element_state_checking = ElementStateChecking(driver, self.element_interaction)
        self.frame_handling = FrameHandling(driver, self.element_interaction)
        self.waiting_conditions = WaitingConditions(driver, self.element_state_checking)
        self.utility_functions = UtilityFunctions(driver, self.element_interaction)

    def switch_to_new_tab(self) -> None:
        """Switch to the newly opened tab"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_all_carousel_elements(self, locator: tuple, img_locator: tuple) -> None:
        """
        Click all carousel elements and verify that the elements are displayed
        :param locator: Locator of the elements to click
        :param img_locator: Locator of the elements to wait for visibility after click
        """
        elements = self.element_interaction.find_elements(locator)
        target = self.element_interaction.find_elements(img_locator)
        assert self.element_state_checking.is_length_of_elements(elements, len(target)), (
            f"Expected {len(elements)} elements, but found {len(target)} elements"
        )

        for index, element in enumerate(elements):
            element.click()
            self.waiting_conditions.wait_for_element_visible_by_element(target[index])
            assert self.element_state_checking.is_found_element_visible(target[index]), (
                f"Element at index {index} not displayed after click"
            )

    def click_all_collapse_elements(self, locator: tuple, locator2: tuple[str:str], text: str) -> None:
        """
        Click all collapse elements and verify that the specified text is in the class attribute of the element
        :param locator: Locator of the elements to click
        :param locator2: Locator of the elements to wait for visibility after click
        :param text: Text to check in the class attribute
        """
        elements = self.element_interaction.find_elements(locator)

        for element in elements:
            element.click()
            assert text not in element.get_attribute("class"), f"Expected '{text}' to not be in class after first click"
            self.waiting_conditions.wait_for_element_visible_by_locator(locator2)
            element.click()
            assert text in element.get_attribute("class"), f"Expected '{text}' to be in class after second click"
            self.waiting_conditions.wait_for_element_to_disappear(locator2)

    # Combined methods
    def scroll_wait_click_element_by_locator(self, locator: tuple, locator2: tuple = None,
                                             scroll_option: str = 'default') -> None:
        """
        Scroll, wait for visibility, and click on the element specified by the locator.

        :param locator: The locator of the element to scroll to.
        :param locator2: Optional locator of the element to click. If None, locator will be used.
        :param scroll_option: Determines which scroll method to use.
                              'default' - scrolls directly to the element,
                              'top' - scrolls the element to the top of the screen,
                              'center' - scrolls the element to the center of the screen.
        """
        if scroll_option == 'top':
            self.utility_functions.scroll_to_element_top_of_screen(locator)
        elif scroll_option == 'center':
            self.utility_functions.scroll_to_element_center_of_screen(locator)
        else:
            self.utility_functions.scroll_to_element(locator)

        self.waiting_conditions.wait_for_scroll_to_element(locator)
        self.element_interaction.click_element(locator if locator2 is None else locator2)
