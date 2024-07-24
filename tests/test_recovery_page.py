from utils.client import RESET


def test_recovery_page(driver, recovery_page):
    recovery_page.open(RESET)
