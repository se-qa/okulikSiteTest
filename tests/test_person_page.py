from utils.client import PERSON


def test_person_page(driver, person_page):
    person_page.open(PERSON)
    