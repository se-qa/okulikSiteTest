from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def js_set_value(driver: WebDriver, element: WebElement, value: str) -> None:
    driver.execute_script("arguments[0].value = arguments[1];", element, value)


def js_show_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].style.visibility='visible';", element)


def js_set_attribute(driver: WebDriver, element: WebElement, attribute_name: str, value: str) -> None:
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", element, attribute_name, value)


def js_get_attribute_value(driver: WebDriver, element: WebElement, attribute_name: str) -> str:
    return driver.execute_script("return arguments[0].getAttribute(arguments[1]);", element, attribute_name)


def js_hide_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].style.display='none';", element)


def js_illuminate_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].style.border='3px solid red'", element)


def js_set_checkbox_value(driver: WebDriver, element: WebElement, value: bool) -> None:
    driver.execute_script("arguments[0].checked = arguments[1];", element, value)
