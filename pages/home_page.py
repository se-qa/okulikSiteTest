from pages.base_page import BasePage

from selenium.webdriver.chrome import webdriver

from tests.data.selectors.common_selectors import collapse_cards_active, img_carousel_items


class HomePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)

    def click_all_collapse_elements_with_class(self, locator: tuple, text: str) -> None:
        elements = self.find_elements(locator)

        for element in elements:
            element.click()
            assert text not in element.get_attribute("class"), f"Expected '{text}' to not be in class after first click"
            self.wait_for_element_visible_by_locator(collapse_cards_active)
            element.click()
            assert text in element.get_attribute("class"), f"Expected '{text}' to be in class after second click"
            self.wait_for_element_to_disappear(collapse_cards_active)
            # sleep(1)

    def click_all_carousel_elements(self, locator: tuple) -> None:
        elements = self.find_elements(locator)
        target = self.find_elements(img_carousel_items)
        assert self.is_length_of_elements(elements, len(target)), (f"Expected {len(elements)} elements, "
                                                                   + f"but found {len(target)} elements")

        for index, element in enumerate(elements):
            element.click()
            self.wait_for_element_visible_by_element(target[index])
            assert target[index].is_displayed(), f"Element at index {index} is not displayed after clicking"
