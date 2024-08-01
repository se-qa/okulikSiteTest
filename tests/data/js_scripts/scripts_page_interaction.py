from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def js_scroll_to(driver: WebDriver, x: int, y: int) -> None:
    driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)


def js_scroll_element_to_center_of_screen(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def js_scroll_element_to_top_of_screen(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("""
        var elementTop = arguments[0].getBoundingClientRect().top;
        var currentScroll = window.scrollY || document.documentElement.scrollTop;
        var targetScroll = currentScroll + elementTop - 50;
        window.scrollTo({ top: targetScroll, behavior: 'smooth' });
    """, element)


def js_scroll_to_bottom(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def js_scroll_to_top(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0, 0);")


def js_alert(driver: WebDriver, message: str) -> None:
    driver.execute_script("alert(arguments[0]);", message)


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
