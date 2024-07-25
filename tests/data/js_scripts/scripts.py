# Element Interaction
def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)


def js_scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


def js_get_element_text(driver, element):
    return driver.execute_script("return arguments[0].textContent;", element)


def js_set_focus_to_element(driver, element):
    driver.execute_script("arguments[0].focus();", element)


def js_insert_text(driver, element, text):
    driver.execute_script("arguments[0].value = arguments[1];", element, text)


def js_right_click(driver, element):
    driver.execute_script("""
            var evt = document.createEvent('MouseEvents');
            evt.initEvent('contextmenu', true, true);
            arguments[0].dispatchEvent(evt);
        """, element)


# Element State Manipulation
def js_set_value(driver, element, value):
    driver.execute_script("arguments[0].value = arguments[1];", element, value)


def js_show_element(driver, element):
    driver.execute_script("arguments[0].style.visibility='visible';", element)


def js_set_attribute(driver, element, attribute_name, value):
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", element, attribute_name, value)


def js_get_attribute_value(driver, element, attribute_name):
    driver.execute_script("return arguments[0].getAttribute(arguments[1]);", element, attribute_name)


def js_hide_element(driver, element):
    driver.execute_script("arguments[0].style.display='none';", element)


def js_illuminate_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)


def js_set_checkbox_value(driver, element):
    driver.execute_script("arguments[0].checked = arguments[1];", element, True)


# Page Interaction
def js_scroll_to(driver, x, y):
    driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)


def js_alert(driver, message):
    driver.execute_script("alert(arguments[0]);", message)


def js_scroll_element_to_center_of_screen(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def js_scroll_element_to_top_of_screen(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)


def js_scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def js_scroll_to_top(driver):
    driver.execute_script("window.scrollTo(0, 0);")


def js_get_current_url(driver):
    return driver.execute_script("return window.location.href;")


def js_reload_page(driver):
    driver.execute_script("location.reload();")


def js_hide_all_popups(driver):
    driver.execute_script("""
            var modals = document.querySelectorAll('.modal');
            modals.forEach(function(modal) {
                modal.style.display = 'none';
            });
        """)


# Utility Functions
def js_wait(driver, milliseconds):
    driver.execute_script("setTimeout(function(){}, arguments[0]);", milliseconds)


def js_is_visible_on_screen(driver, element):
    return driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)


def js_get_page_html(driver):
    return driver.execute_script("return document.documentElement.outerHTML;")


def js_get_element_size(driver, element):
    return driver.execute_script(
        "return {width: arguments[0].offsetWidth, height: arguments[0].offsetHeight};",
        element
    )


def js_deselect_text(driver):
    driver.execute_script(
        "if (window.getSelection) {window.getSelection().removeAllRanges();} "
        "else if (document.selection) {document.selection.empty();}"
    )


def js_check_if_element_is_enabled(driver, element):
    return driver.execute_script("return !arguments[0].disabled;", element)


def js_check_if_element_exists(driver, css_selector):
    return driver.execute_script("return document.querySelector(arguments[0]) !== null;", css_selector)
