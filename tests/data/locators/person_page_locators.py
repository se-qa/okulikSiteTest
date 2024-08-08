from selenium.webdriver.common.by import By


class PersonPageLocators:
    # links
    link_main = (By.XPATH, '//ul[@class="nav nav-pills flex-column mb-auto"]/descendant::a[1]')
    link_payment_page = (By.XPATH, '//a[text()="Страница оплаты"]')
    link_payment = (By.XPATH, '//ul[@class="nav nav-pills flex-column mb-auto"]/descendant::a[2]')
    link_groups = (By.XPATH, '//ul[@class="nav nav-pills flex-column mb-auto"]/descendant::a[3]')
    link_my_telegram = (By.XPATH, '//a[contains(text(), "@okulikby") and @target="_blank"]')
    link_users = (By.XPATH, '//a[@id="dropdownUser2"]')
    link_logout = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]')
