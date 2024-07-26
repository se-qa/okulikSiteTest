from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


# Element Interaction
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


# Element State Manipulation
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


# Page Interaction
def js_scroll_to(driver: WebDriver, x: int, y: int) -> None:
    driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)


def js_alert(driver: WebDriver, message: str) -> None:
    driver.execute_script("alert(arguments[0]);", message)


def js_scroll_element_to_center_of_screen(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def js_scroll_element_to_top_of_screen(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)


def js_scroll_to_bottom(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def js_scroll_to_top(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0, 0);")


def js_get_current_url(driver: WebDriver) -> str:
    return driver.execute_script("return window.location.href;")


def js_reload_page(driver: WebDriver) -> None:
    driver.execute_script("location.reload();")


def js_hide_all_popups(driver: WebDriver) -> None:
    driver.execute_script("""
        var modals = document.querySelectorAll('.modal');
        modals.forEach(function(modal) {
            modal.style.display = 'none';
        });
    """)


# Utility Functions
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
        "if (window.getSelection) {window.getSelection().removeAllRanges();} "
        "else if (document.selection) {document.selection.empty();}"
    )


def js_check_if_element_is_enabled(driver: WebDriver, element: WebElement) -> bool:
    return driver.execute_script("return !arguments[0].disabled;", element)


def js_check_if_element_exists(driver: WebDriver, css_selector: str) -> bool:
    return driver.execute_script("return document.querySelector(arguments[0]) !== null;", css_selector)
