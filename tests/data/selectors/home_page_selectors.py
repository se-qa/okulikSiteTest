from selenium.webdriver.common.by import By

# buttons
button_sign_up_top = (By.XPATH, '//a[text()="Запишись в ближайшую группу"]')
button_sign_up_right_group = (By.XPATH, '//a[text()="Запишись в нужную группу"]')
button_sign_up = (By.XPATH, '//input[@class="btn btn-primary w-100 btn-lg"]')
button_get_a_practical_task = (By.XPATH, '//a[text()="Получить практическое задание"]')
button_pay_first_step = (By.XPATH, '//a[text()="Оплатить первый этап"]')
button_pay_entirely = (By.XPATH, '//a[text()="Оплатить целиком"]')

# links
link_logo = (By.XPATH, '//a[@class="logo nav-link link-dark px-2 active"]')
link_video_course = (By.XPATH, '//a[text()="видеокурс"]')
link_full_price = (By.XPATH, '(//a[contains(text(), "Весь курс за")])[1]')
link_part_price = (By.XPATH, '(//a[contains(text(), "за часть")])[1]')
link_video_price = (By.XPATH, '(//a[contains(text(), "за курс")])[1]')
link_full_price_middle = (By.XPATH, '(//a[contains(text(), "Весь курс за")])[2]')
link_part_price_middle = (By.XPATH, '(//a[contains(text(), "за часть")])[2]')
link_video_price_middle = (By.XPATH, '(//a[contains(text(), "за курс")])[2]')
link_telegram_step_by_step_radio = (By.XPATH, '(//a[text()="телеграм"])[1]')
link_telegram_entire_amount_radio = (By.XPATH, '(//a[text()="телеграм"])[2]')

# anchors
anchor_course_program = (By.XPATH, '//a[text()="Программа курса"]')  # Target is title_course_program
anchor_nearest_course = (By.XPATH, '//a[text()="Ближайший курс"]')  # Target is title_start_group
anchor_price = (By.XPATH, '//a[text()="Цены"]')  # Target is title_price
anchor_booking = (By.XPATH, '//a[text()="Забронировать"]')  # Target is title_booking

# titles
title_what_is_in_the_end = (By.XPATH, '//h1[contains (text(), "Что в итоге")]')
title_booking = (By.XPATH, '//h1[text()="Бронирование"]')
title_any_questions = (By.XPATH, '//h1[text()="Остались вопросы?"]')
title_course_program = (By.XPATH, '//h1[text()="Программа курса"]')
title_start_group = (By.XPATH, '//h1[text()="Старт группы"]')
title_price = (By.XPATH, '//h1[text()="Цены"]')
title_staged_payment = (By.XPATH, '//h4[@class="my-0 fw-normal" and text()="Поэтапная оплата"]')
title_payment_whole_course = (By.XPATH, '//h4[@class="my-0 fw-normal" and contains (text(), "Оплата за весь")]')

# inputs
input_full_name = (By.XPATH, '//input[@placeholder="Как тебя зовут?"]')
input_email = (By.XPATH, '//input[@placeholder="user@mail.com"]')
input_contact = (By.XPATH, '//input[contains(@placeholder,"Например")]')
input_comment = (By.XPATH, '//textarea[contains(@placeholder, "дополнительные сведения")]')

# switchers
switcher_stages = (By.XPATH, '//label[@for="stages"]')
switcher_entire_amount = (By.XPATH, '//label[@for="full"]')

# paragraphs
paragraph_successful_alert = (By.XPATH, '(//*[@class="alert alert-success"]/p[contains(text(), "Привет")])[1]')
