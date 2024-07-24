from selenium.webdriver.common.by import By

# buttons
button_get_access = (By.XPATH, '//a[text()="Получить доступ"]')
button_pay_access = (By.XPATH, '(//a[text()="Оплатить доступ"])[1]')
button_pay_access_without_home_tasks = (By.XPATH, '(//a[text()="Оплатить доступ"])[2]')
button_get_a_practical_assignment = (By.XPATH, '//a[text()="Получить практическое задание"]')

# anchors
anchor_learning_process = (By.XPATH, '//a[text()="Процесс обучения"]')
anchor_join_a_group = (By.XPATH, '//a[text()="группу"]')
