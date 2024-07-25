from selenium.webdriver.common.by import By

from tests.data.selectors import part_price_page_selectors, full_price_page_selectors, video_page_selectors, \
    outdoor_page_selectors
from tests.data.selectors.common_selectors import link_about_me_youtube
from utils.client import FULL_PRICE, PART_PRICE, VIDEO

# buttons
button_sign_up_top = (By.XPATH, '//a[text()="Запишись в ближайшую группу"]')
button_sign_up_middle = (By.XPATH, '//a[text()="Запишись в нужную группу"]')
button_sign_up = (By.XPATH, '//input[@class="btn btn-primary w-100 btn-lg"]')
button_get_a_practical_assignment = (By.XPATH, '//a[text()="Получить практическое задание"]')
button_pay_first_step = (By.XPATH, '//a[text()="Оплатить первый этап"]')
button_pay_entirely = (By.XPATH, '//a[text()="Оплатить целиком"]')

# links
link_logo = (By.XPATH, '//a[@class="logo nav-link link-dark px-2 active"]')
link_video_course = (By.XPATH, '//a[text()="видеокурс"]')
link_full_price = (By.XPATH, '(//a[contains(text(), "Весь курс за")])[1]')
link_part_price = (By.XPATH, '(//a[contains(text(), "за часть")])[1]')
link_video_price = (By.XPATH, '(//a[contains(text(), "за курс")])[1]')
link_full_price_middle = (By.XPATH, '(//a[contains(text(), "Весь курс за")])[2]')
link_part_price_middle= (By.XPATH, '(//a[contains(text(), "за часть")])[2]')
link_video_price_middle = (By.XPATH, '(//a[contains(text(), "за курс")])[2]')
link_telegram_step_by_step_radio = (By.XPATH, '((//a[text()="телеграм"])[1]')
link_telegram_entire_amount_radio = (By.XPATH, '((//a[text()="телеграм"])[2]')

# anchors
anchor_course_program = (By.XPATH, '//a[text()="Программа курса"]')  # Target is title_course_program
anchor_nearest_course = (By.XPATH, '//a[text()="Ближайший курс"]')  # Target is title_start_group
anchor_price = (By.XPATH, '//a[text()="Цены"]')  # Target is title_price
anchor_booking = (By.XPATH, '//a[text()="Забронировать"]')  # Target is title_booking
anchor_learning_process = (By.XPATH, '//a[text()="Процесс обучения"]')  # Target is title_learning_process

# titles
title_what_is_in_the_end = (By.XPATH, '//h1[contains (text(), "Что в итоге")]')
title_booking = (By.XPATH, '//h1[text()="Бронирование"]')
title_any_questions = (By.XPATH, '//h1[text()="Остались вопросы?"]')
title_course_program = (By.XPATH, '//h1[text()="Программа курса"]')
title_start_group = (By.XPATH, '//h1[text()="Старт группы"]')
title_price = (By.XPATH, '//h1[text()="Цены"]')
title_learning_process = (By.XPATH, '//h1[text()="Процесс обучения"]')

# inputs
input_full_name = (By.XPATH, '//input[@placeholder="Как тебя зовут?"]')
input_email = (By.XPATH, '//input[@placeholder="user@mail.com"]]')
input_contact = (By.XPATH, '//input[contains(@placeholder,"Например")]')
input_comment = (By.XPATH, '//textarea[contains(@placeholder, "дополнительные сведения")]')

anchors_top_list = [
    (anchor_course_program, title_course_program),
    (anchor_nearest_course, title_start_group),
    (anchor_price, title_price),
    (anchor_booking, title_booking)
]

anchors_top_list_ids = ["Course program", "Nearest course", "Price", "Booking"]

buy_links_list = [
    (link_full_price, full_price_page_selectors.title_full_price, FULL_PRICE),
    (link_part_price, part_price_page_selectors.title_part_price, PART_PRICE),
    (link_video_price, video_page_selectors.paragraph_study_whenever_you_want, VIDEO)
]

buy_links_list_ids = ["Full price",
                      "Part price",
                      "Video price"
                      ]

other_links_list = [
    (link_about_me_youtube, outdoor_page_selectors.youtube_channel_title, "https://www.youtube.com/@SeniorTester"),
    (link_video_course, video_page_selectors.paragraph_study_whenever_you_want, VIDEO),
    (link_full_price_middle, full_price_page_selectors.title_full_price, FULL_PRICE),
    (link_part_price_middle, part_price_page_selectors.title_part_price, PART_PRICE),
    (link_video_price_middle, video_page_selectors.paragraph_study_whenever_you_want, VIDEO),
    (link_telegram_step_by_step_radio, outdoor_page_selectors.telegram_channel_title, "https://t.me/okulikby")
]

other_links_list_ids = ["Senior Tester",
                        "video course",
                        "Full price middle",
                        "Part price middle",
                        "Video price middle",
                        "telegram"
                        ]
