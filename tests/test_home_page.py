from time import sleep

from tests.data.selectors.home_page_selectors import title_what_is_in_the_end
from utils.client import URL


def test_home_page(driver, home_page):
    home_page.open(URL)
    home_page.scroll_to_element(title_what_is_in_the_end)
    sleep(5)
    home_page.quit()
