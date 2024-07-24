from selenium.webdriver.common.by import By

# buttons
button_open_chat = (By.XPATH, '//a[text()="Открыть чат"]')

buttons_carousel = (By.XPATH, '//button[@data-bs-target="#carouselExampleIndicators"][@aria-label]')
button_carousel_previous = (By.XPATH, '//button[@class="carousel-control-prev"]')
button_carousel_next = (By.XPATH, '//button[@class="carousel-control-next"]')

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

link_copyright = (By.XPATH, '(//a[text()="www.okulik.by"]')
link_payment_rules = (By.XPATH, '//a[contains(text(), "Правила оплаты")]')
link_offer = (By.XPATH, '//a[contains(text(), "оферты")]')
link_telegram_bottom = (By.XPATH, '(//a[text()="t.me/okulikby"]')

# collapses
collapses_block = (By.XPATH, '//h2[contains (text(), "Программирование на Python")]/ancestor::div[4]')
collapse_cards = (By.XPATH, '//a[@data-bs-toggle="collapse"]')
# collapse_automation_of_backend_testing = (By.XPATH, '//h2[contains (text(), "backend ")]/ancestor::a[1]')
# collapse_automation_of_ui_testing = (By.XPATH, '//h2[contains (text(), "UI ")]/ancestor::a[1]')
# collapse_tools = (By.XPATH, '//h2[contains (text(), "Инструменты")]/ancestor::a[1]')
# collapse_final_block = (By.XPATH, '//h2[contains (text(), "Итоговый блок")]/ancestor::a[1]')


def button_carousel_page(page: int) -> (By, str):
    return By.XPATH, f'//button[@data-bs-target="#carouselExampleIndicators"][@data-bs-slide-to="{page}"]'
