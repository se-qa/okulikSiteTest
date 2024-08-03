import pytest

from utils.client import PRACTICAL_TASK

from tests.data.selectors.common_selectors import *
from tests.data.selectors.home_page_selectors import button_get_a_practical_task
from tests.data.selectors.practical_task_page_selectors import title_practical_task
from tests.data.tests_data.parametrize_common import class_pages_list_ids, class_pages_list, \
    pages_and_common_elements_list, pages_and_common_elements_list_ids, pages_and_carousel_buttons_list, \
    pages_and_carousel_buttons_list_ids


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_anchor_learning_process_click(testing_page):
    testing_page.scroll_wait_click_element_by_locator(anchor_learning_process)
    testing_page.wait_for_scroll_to_element(title_learning_process)
    assert testing_page.is_element_in_viewport(title_learning_process)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_button_get_practical_task_click(testing_page):
    testing_page.scroll_wait_click_element_by_locator(button_get_a_practical_task)
    testing_page.wait_for_element_visible_by_locator(title_practical_task)
    assert testing_page.is_current_url(PRACTICAL_TASK)
    assert testing_page.is_element_in_viewport(title_practical_task)


@pytest.mark.parametrize("testing_page, button_to_click, img_to_check", pages_and_carousel_buttons_list,
                         ids=pages_and_carousel_buttons_list_ids, indirect=["testing_page"])
def test_carousel_button_click(testing_page, button_to_click, img_to_check):
    testing_page.scroll_wait_click_element_by_locator(div_carousel, button_to_click, scroll_option='top')
    testing_page.wait_for_element_visible_by_locator(img_to_check)
    assert testing_page.is_element_in_viewport(img_to_check)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_all_carousel_pages_click(testing_page):
    testing_page.scroll_to_element_top_of_screen(div_carousel)
    testing_page.wait_for_scroll_to_element(div_carousel)
    testing_page.click_all_carousel_elements(buttons_carousel)


@pytest.mark.parametrize("testing_page, locator_to_click, locator_to_check", pages_and_common_elements_list,
                         ids=pages_and_common_elements_list_ids, indirect=["testing_page"])
def test_multiple_elements_click(testing_page, locator_to_click, locator_to_check):
    testing_page.scroll_wait_click_element_by_locator(locator_to_click)
    testing_page.wait_for_element_visible_by_locator(locator_to_check)
    assert testing_page.is_element_visible(locator_to_check)
