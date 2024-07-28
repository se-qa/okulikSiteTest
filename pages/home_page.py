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
            assert text not in element.get_attribute("class")
            self.wait_for_element_visible_by_locator(collapse_cards_active)
            element.click()
            assert text in element.get_attribute("class")
            self.wait_for_element_to_disappear(collapse_cards_active)
            # sleep(1)

    def click_all_carousel_elements(self, locator: tuple) -> None:
        elements = self.find_elements(locator)
        elements2 = self.find_elements(img_carousel_items)
        assert self.is_length_of_elements(elements, len(elements2))
        index = 0
        for element in elements:
            element.click()
            self.wait_for_element_visible_by_element(elements2[index])
            assert elements2[index].is_displayed()
            index += 1
