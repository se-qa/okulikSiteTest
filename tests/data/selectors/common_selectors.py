from selenium.webdriver.common.by import By

# buttons
button_open_chat = (By.XPATH, '//a[text()="Открыть чат"]')

buttons_carousel = (By.XPATH, '//button[@data-bs-target="#carouselExampleIndicators"][@aria-label]')
button_carousel_previous = (By.XPATH, '//button[@class="carousel-control-prev"]')
button_carousel_next = (By.XPATH, '//button[@class="carousel-control-next"]')

# divs
div_carousel = (By.XPATH, '//div[@id="carouselExampleIndicators"]')
div_first_element_in_collapse_card = (By.XPATH, '(//*[@class="col d-flex align-items-start bon"])[1]')
div_payment_rules = (By.XPATH, '//div[@class="container  px-4 py-5"]')

# imgs
img_carousel_items = (By.XPATH, '//img[@class="img-circle"]')
img_carousel_item_1 = (By.XPATH, '(//img[@class="img-circle"])[1]')
img_carousel_item_2 = (By.XPATH, '(//img[@class="img-circle"])[2]')
img_carousel_item_4 = (By.XPATH, '(//img[@class="img-circle"])[4]')
img_carousel_item_7 = (By.XPATH, '(//img[@class="img-circle"])[7]')

# paragraphs
paragraph_carousel_items = (By.XPATH, '//p[@class="lead review"]')

# titles
title_learning_process = (By.XPATH, '//h1[text()="Процесс обучения"]')
title_offer = (By.XPATH, '//h2[text()="ПУБЛИЧНАЯ ОФЕРТА"]')

# anchors
anchor_learning_process = (By.XPATH, '//a[text()="Процесс обучения"]')

# links
link_about_me_youtube = (By.XPATH, '//a[@class="mylink" and text()="Senior Tester"]')

link_lk_top = (By.XPATH, '(//a[text()="Личный кабинет"])[1]')
link_lk_bottom = (By.XPATH, '(//a[text()="Личный кабинет"])[2]')
link_linkedin_top_icon = (By.XPATH, '(//*[@class="bi bi-linkedin"])[1]/parent::*')
link_linkedin_bottom_icon = (By.XPATH, '(//*[@class="bi bi-linkedin"])[2]/parent::*')
link_telegram_top_icon = (By.XPATH, '(//*[@class="bi bi-telegram"])[1]/parent::*')
link_telegram_bottom_icon = (By.XPATH, '(//*[@class="bi bi-telegram"])[2]/parent::*')
link_youtube_top_icon = (By.XPATH, '(//*[@class="bi bi-youtube"])[1]/parent::*')
link_youtube_bottom_icon = (By.XPATH, '(//*[@class="bi bi-youtube"])[2]/parent::*')

link_copyright = (By.XPATH, '//a[text()="www.okulik.by"]')
link_payment_rules = (By.XPATH, '//a[contains(text(), "Правила оплаты")]')
link_offer = (By.XPATH, '//a[contains(text(), "оферты")]')
link_telegram_bottom = (By.XPATH, '(//a[text()="t.me/okulikby"]')

# collapses
collapses_block = (By.XPATH, '//h2[contains (text(), "Программирование на Python")]/ancestor::div[4]')
collapse_cards = (By.XPATH, '//a[@data-bs-toggle="collapse"]')
collapse_cards_active = (By.XPATH, '//div[contains(@class, "collapse show")]')

collapse_automation_of_backend_testing = (By.XPATH, '//h2[contains (text(), "backend ")]/ancestor::a[1]')
collapse_automation_of_ui_testing = (By.XPATH, '//h2[contains (text(), "UI ")]/ancestor::a[1]')
collapse_tools = (By.XPATH, '//h2[contains (text(), "Инструменты")]/ancestor::a[1]')
collapse_final_block = (By.XPATH, '//h2[contains (text(), "Итоговый блок")]/ancestor::a[1]')


def button_carousel_page(page: int) -> (By, str):
    return By.XPATH, f'//button[@data-bs-target="#carouselExampleIndicators"][@data-bs-slide-to="{page}"]'


# chat
opened_chat = (By.XPATH, '//jdiv[@id="jcont"]')
