from selenium.webdriver.chrome import webdriver


class BrowserControl:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

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

    def switch_to_new_tab(self) -> None:
        """Switch to the newly opened tab"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_tab_and_switch_back(self) -> None:
        """Close the current tab and switch to the last opened tab"""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit(self) -> None:
        """Quit the browser session"""
        self.driver.quit()
