from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def js_wait(driver: WebDriver, milliseconds: int) -> None:
    driver.execute_script("setTimeout(function(){}, arguments[0]);", milliseconds)


def js_is_visible_on_screen(driver: WebDriver, element: WebElement) -> bool:
    return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    """, element)


def js_get_page_html(driver: WebDriver) -> str:
    return driver.execute_script("return document.documentElement.outerHTML;")


def js_get_element_size(driver: WebDriver, element: WebElement) -> dict:
    return driver.execute_script(
        "return {width: arguments[0].offsetWidth, height: arguments[0].offsetHeight};",
        element
    )


def js_deselect_text(driver: WebDriver) -> None:
    driver.execute_script(
        "if (window.getSelection) {var sel = window.getSelection(); if (sel.rangeCount > 0) sel.removeAllRanges();} "
        "else if (document.selection) {document.selection.empty();}"
    )


def js_check_if_element_is_enabled(driver: WebDriver, element: WebElement) -> bool:
    return driver.execute_script("return !arguments[0].disabled;", element)


def js_check_if_element_exists(driver: WebDriver, css_selector: str) -> bool:
    return driver.execute_script("return document.querySelector(arguments[0]) !== null;", css_selector)
