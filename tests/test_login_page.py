from utils.client import LOGIN


def test_login_page(driver, login_page):
    login_page.open(LOGIN)
