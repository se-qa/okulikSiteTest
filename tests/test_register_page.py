from utils.client import REGISTER


def test_register_page(driver, register_page):
    register_page.open(REGISTER)
