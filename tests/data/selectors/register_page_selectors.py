from selenium.webdriver.common.by import By

# inputs
input_username = (By.XPATH, '//input[@id="id_username"]')
input_email = (By.XPATH, '//input[@id="id_email"]')
input_first_name = (By.XPATH, '//input[@id="id_first_name"]')
input_last_name = (By.XPATH, '//input[@id="id_last_name"]')
input_password = (By.XPATH, '//input[@id="id_password1"]')
input_confirm_password = (By.XPATH, '//input[@id="id_password2"]')

# buttons
button_register = (By.XPATH, '//input[@id="submit-id-submit"]')

span_error_username = (By.XPATH, '//span[contains(@id, "username")]')
span_error_email = (By.XPATH, '//span[contains(@id, "email")]')
span_error_password = (By.XPATH, '//span[contains(@id, "password")]')
