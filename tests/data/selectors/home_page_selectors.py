from selenium.webdriver.common.by import By

# buttons
button_sign_up_top = (By.XPATH, '//a[text()="Запишись в ближайшую группу"]')
button_sign_up_middle = (By.XPATH, '//a[text()="Запишись в нужную группу"]')
button_sign_up = (By.XPATH, '//input[@class="btn btn-primary w-100 btn-lg"]')
button_get_a_practical_assignment = (By.XPATH, '//a[text()="Получить практическое задание"]')
button_pay_first_step = (By.XPATH, '//a[text()="Оплатить первый этап"]')
button_pay_entirely = (By.XPATH, '//a[text()="Оплатить целиком"]')

# links
link_full_price = (By.XPATH, '(//a[contains(text(), "Весь курс за")])[1]')
link_part_price = (By.XPATH, '(//a[contains(text(), "за часть")])[1]')
link_video_price = (By.XPATH, '(//a[contains(text(), "за часть")])[1]')
link_telegram_step_by_step_radio = (By.XPATH, '((//a[text()="телеграм"])[1]')
link_telegram_entire_amount_radio = (By.XPATH, '((//a[text()="телеграм"])[2]')

# anchors
anchor_course_program = (By.XPATH, '//a[text()="Программа курса"]')
anchor_nearest_course = (By.XPATH, '//a[text()="Ближайший курс"]')
anchor_price = (By.XPATH, '//a[text()="Цены"]')
anchor_booking = (By.XPATH, '//a[text()="Забронировать"]')
anchor_learning_process = (By.XPATH, '//a[text()="Процесс обучения"]')
anchor_video_course = (By.XPATH, '//a[text()="видеокурс"]')

# titles
title_what_is_in_the_end = (By.XPATH, '//h1[contains (text(), "Что в итоге")]')

# inputs
input_full_name = (By.XPATH, '//input[@placeholder="Как тебя зовут?"]')
input_email = (By.XPATH, '//input[@placeholder="user@mail.com"]]')
input_contact = (By.XPATH, '//input[contains(@placeholder,"Например")]')
input_comment = (By.XPATH, '//textarea[contains(@placeholder, "дополнительные сведения")]')
