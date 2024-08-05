from selenium.webdriver.chrome import webdriver

from pages.modules.interaction import ElementInteraction


class FrameHandling:
    def __init__(self, driver: webdriver, element_interaction: ElementInteraction) -> None:
        self.driver = driver
        self.element_interaction = element_interaction

    def switch_to_frame(self, locator: tuple) -> None:
        """Switch to the frame specified by the locator"""
        frame = self.element_interaction.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self) -> None:
        """Switch back to the default content from an iframe"""
        self.driver.switch_to.default_content()
