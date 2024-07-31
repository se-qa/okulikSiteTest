from selenium.webdriver.common.by import By

# buttons
button_get_access = (By.XPATH, '//a[text()="Получить доступ"]')
button_pay_access = (By.XPATH, '(//a[text()="Оплатить доступ"])[1]')
button_pay_access_without_home_tasks = (By.XPATH, '(//a[text()="Оплатить доступ"])[2]')
button_get_a_practical_assignment = (By.XPATH, '//a[text()="Получить практическое задание"]')

# titles
title_price = (By.XPATH, '//h1[text()="Цены"]')

# anchors
anchor_join_a_group = (By.XPATH, '//a[text()="группу"]')

# paragraph
paragraph_study_whenever_you_want = (By.XPATH, '//div[@class="col-lg-6 mx-auto"]/child::p[2]')

# links
link_join_a_group = (By.XPATH, '//a[text()="группу"]')
