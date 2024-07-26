from selenium.webdriver.common.by import By

# inputs
input_reset_password = (By.XPATH, '//input[@id="id_email"]')

# buttons
button_reset_password = (By.XPATH, '//input[@id="submit-id-submit"]')

# span
span_error_email = (By.XPATH, '//span[contains(@id, "email")]')

# titles
h1_reset_password_done = (By.XPATH, '//h1')
