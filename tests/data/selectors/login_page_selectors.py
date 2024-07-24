from selenium.webdriver.common.by import By

# inputs
input_username = (By.XPATH, '//input[@id="id_username"]')
input_password = (By.XPATH, '//input[@id="id_password"]')

# buttons
button_login = (By.XPATH, '//input[@id="submit-id-submit"]')

# links
link_recover = (By.XPATH, '//a[text()="Восстановить"]')
link_register = (By.XPATH, '//a[text()="Зарегистрироваться"]')

message_error = (By.XPATH, '//div[@class="alert alert-block alert-danger"]/descendant::li')