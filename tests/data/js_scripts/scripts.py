# Element Interaction
def js_click(self, element):
    self.execute_script("arguments[0].click();", element)


def js_scroll_to_element(self, element):
    self.execute_script("arguments[0].scrollIntoView(true);", element)


def js_get_element_text(self, element):
    return self.driver.execute_script("return arguments[0].textContent;", element)


def js_set_focus_to_element(self, element):
    self.driver.execute_script("arguments[0].focus();", element)


def js_insert_text(self, element, text):
    self.driver.execute_script("arguments[0].value = arguments[1];", element, text)


def js_right_click(self, element):
    self.driver.execute_script("""
            var evt = document.createEvent('MouseEvents');
            evt.initEvent('contextmenu', true, true);
            arguments[0].dispatchEvent(evt);
        """, element)


# Element State Manipulation
def js_set_value(self, element, value):
    self.driver.execute_script("arguments[0].value = arguments[1];", element, value)


def js_show_element(self, element):
    self.driver.execute_script("arguments[0].style.visibility='visible';", element)


def js_set_attribute(self, element, attribute_name, value):
    self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", element, attribute_name, value)


def js_get_attribute_value(self, element, attribute_name):
    self.driver.execute_script("return arguments[0].getAttribute(arguments[1]);", element, attribute_name)


def js_hide_element(self, element):
    self.driver.execute_script("arguments[0].style.display='none';", element)


def js_illuminate_element(self, element):
    self.driver.execute_script("arguments[0].style.border='3px solid red'", element)


def js_set_checkbox_value(self, element):
    self.driver.execute_script("arguments[0].checked = arguments[1];", element, True)


# Page Interaction
def js_scroll_to(self, x, y):
    self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)


def js_alert(self, message):
    self.driver.execute_script("alert(arguments[0]);", message)


def js_scroll_element_to_center_of_screen(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def js_scroll_element_to_top_of_screen(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)


def js_scroll_to_bottom(self):
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def js_scroll_to_top(self):
    self.driver.execute_script("window.scrollTo(0, 0);")


def js_get_current_url(self):
    return self.driver.execute_script("return window.location.href;")


def js_reload_page(self):
    self.driver.execute_script("location.reload();")


def js_hide_all_popups(self):
    self.driver.execute_script("""
            var modals = document.querySelectorAll('.modal');
            modals.forEach(function(modal) {
                modal.style.display = 'none';
            });
        """)


# Utility Functions
def js_wait(self, milliseconds):
    self.driver.execute_script("setTimeout(function(){}, arguments[0]);", milliseconds)


def js_check_if_element_is_visible_on_screen(self, element):
    return self.driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)


def js_get_page_html(self):
    return self.driver.execute_script("return document.documentElement.outerHTML;")


def js_get_element_size(self, element):
    return self.driver.execute_script(
        "return {width: arguments[0].offsetWidth, height: arguments[0].offsetHeight};",
        element
    )


def js_deselect_text(self):
    self.driver.execute_script(
        "if (window.getSelection) {window.getSelection().removeAllRanges();} "
        "else if (document.selection) {document.selection.empty();}"
    )


def js_check_if_element_is_enabled(self, element):
    return self.driver.execute_script("return !arguments[0].disabled;", element)


def js_check_if_element_exists(self, css_selector):
    return self.driver.execute_script("return document.querySelector(arguments[0]) !== null;", css_selector)
