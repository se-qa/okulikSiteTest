from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def js_click(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].click();", element)


def js_scroll_to_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


def js_get_element_text(driver: WebDriver, element: WebElement) -> str:
    return driver.execute_script("return arguments[0].textContent;", element)


def js_set_focus_to_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].focus();", element)


def js_insert_text(driver: WebDriver, element: WebElement, text: str) -> None:
    driver.execute_script("arguments[0].value = arguments[1];", element, text)


def js_right_click(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("""
        var evt = new MouseEvent('contextmenu', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        arguments[0].dispatchEvent(evt);
    """, element)
