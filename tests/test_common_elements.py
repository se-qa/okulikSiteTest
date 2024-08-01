import pytest

from utils.client import PRACTICAL_TASK

from tests.data.selectors.common_selectors import *
from tests.data.selectors.home_page_selectors import button_get_a_practical_task
from tests.data.selectors.practical_task_page_selectors import title_practical_task
from tests.data.tests_data.parametrize_home_page import class_pages_list_ids, class_pages_list


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_button_get_practical_task_click(testing_page):
    testing_page.scroll_to_element(button_get_a_practical_task)
    testing_page.wait_for_scroll_to_element(button_get_a_practical_task)
    testing_page.click_element(button_get_a_practical_task)
    testing_page.wait_for_element_visible_by_locator(title_practical_task)
    assert testing_page.is_current_url(PRACTICAL_TASK)
    assert testing_page.is_element_in_viewport(title_practical_task)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_carousel_previous_button_click(testing_page):
    testing_page.scroll_to_element_top_of_screen(div_carousel)
    testing_page.wait_for_scroll_to_element(div_carousel)
    testing_page.click_element(button_carousel_previous)
    testing_page.wait_for_element_visible_by_locator(img_carousel_item_7)
    assert testing_page.is_element_in_viewport(img_carousel_item_7)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_carousel_next_button_click(testing_page):
    testing_page.scroll_to_element_top_of_screen(div_carousel)
    testing_page.wait_for_scroll_to_element(div_carousel)
    testing_page.click_element(button_carousel_next)
    testing_page.wait_for_element_visible_by_locator(img_carousel_item_2)
    assert testing_page.is_element_in_viewport(img_carousel_item_2)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_all_carousel_pages_click(testing_page):
    testing_page.scroll_to_element_top_of_screen(div_carousel)
    testing_page.wait_for_scroll_to_element(div_carousel)
    testing_page.click_all_carousel_elements(buttons_carousel)


@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_button_open_chat_click(testing_page):
    testing_page.scroll_to_element(button_open_chat)
    testing_page.wait_for_scroll_to_element(button_open_chat)
    testing_page.click_element(button_open_chat)
    testing_page.wait_for_element_visible_by_locator(opened_chat)
    assert testing_page.is_element_visible(opened_chat)
