import pytest

from utils.client import URL

from tests.data.tests_data.parametrize_home_page import *

from tests.data.selectors.full_price_page_selectors import title_full_price
from tests.data.selectors.part_price_page_selectors import title_part_price
from tests.data.selectors.common_selectors import collapse_cards, anchor_learning_process


def test_home_page_open(home_page):
    assert home_page.is_current_url(URL)
    home_page.wait_for_element_visible_by_locator(link_logo)
    assert home_page.is_element_visible(link_logo)


def test_logo_click(home_page):
    home_page.click_element(link_logo)
    assert home_page.is_current_url(URL)
    assert home_page.is_element_in_viewport(link_logo)


def test_button_sign_up_click(home_page):
    home_page.click_element(button_sign_up_top)
    home_page.wait_for_scroll_to_element(title_booking)
    assert home_page.is_element_in_viewport(title_booking)


@pytest.mark.parametrize("anchor, target", anchors_top_list, ids=anchors_top_list_ids)
def test_top_anchor_click(home_page, anchor, target):
    home_page.click_element(anchor)
    home_page.wait_for_scroll_to_element(target)
    assert home_page.is_element_in_viewport(target)


@pytest.mark.parametrize("link, target, url", buy_links_list, ids=buy_links_list_ids)
def test_buy_course_links_click(home_page, link, target, url):
    home_page.click_element(link)
    home_page.wait_for_element_visible_by_locator(target)
    assert home_page.is_current_url(url)
    assert home_page.is_element_visible(target)


@pytest.mark.parametrize("link, target, url", other_links_list, ids=other_links_list_ids)
def test_other_links_click(home_page, link, target, url):
    home_page.scroll_to_element(link)
    home_page.click_element(link)
    home_page.wait_for_element_visible_by_locator(target)
    assert home_page.is_current_url(url)
    assert home_page.is_element_visible(target)


def test_anchor_learning_process_click(home_page):
    home_page.scroll_to_element(anchor_learning_process)
    home_page.click_element(anchor_learning_process)
    home_page.wait_for_scroll_to_element(title_learning_process)
    assert home_page.is_element_in_viewport(title_learning_process)


def test_collapse_cards_click(home_page):
    home_page.scroll_to_element_top_of_screen(collapse_cards)
    home_page.wait_for_scroll_to_element(collapse_cards)
    home_page.click_all_collapse_elements(collapse_cards, "collapsed")


def test_button_sign_up_right_group_click(home_page):
    home_page.scroll_to_element(button_sign_up_right_group)
    home_page.wait_for_scroll_to_element(button_sign_up_right_group)
    home_page.click_element(button_sign_up_right_group)
    home_page.wait_for_scroll_to_element(title_booking)
    assert home_page.is_element_in_viewport(title_booking)


def test_switchers_click(home_page):
    home_page.scroll_to_element(switcher_stages)
    home_page.wait_for_scroll_to_element(switcher_stages)
    assert home_page.is_element_visible(title_staged_payment)
    home_page.click_element(switcher_entire_amount)
    assert home_page.is_element_visible(title_payment_whole_course)
    home_page.click_element(switcher_stages)
    assert home_page.is_element_not_visible(title_payment_whole_course)
    assert home_page.is_element_visible(title_staged_payment)


def test_button_pay_first_step_click(home_page):
    home_page.scroll_to_element(button_pay_first_step)
    home_page.wait_for_scroll_to_element(button_pay_first_step)
    home_page.click_element(button_pay_first_step)
    home_page.wait_for_element_visible_by_locator(title_part_price)
    assert home_page.is_current_url(PART_PRICE)
    assert home_page.is_element_in_viewport(title_part_price)


def test_button_pay_entirely_click(home_page):
    home_page.scroll_to_element(switcher_entire_amount)
    home_page.wait_for_scroll_to_element(switcher_entire_amount)
    home_page.click_element(switcher_entire_amount)
    home_page.scroll_to_element(button_pay_entirely)
    home_page.wait_for_scroll_to_element(button_pay_entirely)
    home_page.click_element(button_pay_entirely)
    home_page.wait_for_element_visible_by_locator(title_full_price)
    assert home_page.is_current_url(FULL_PRICE)
    assert home_page.is_element_in_viewport(title_full_price)


def test_booking_form_submit(home_page):
    home_page.scroll_to_element_top_of_screen(title_booking)
    home_page.wait_for_scroll_to_element(title_booking)
    home_page.send_keys(input_full_name, "Evgeny")
    home_page.send_keys(input_email, "test@test.com")
    home_page.send_keys(input_contact, "any text")
    home_page.send_keys(input_comment, "some text")
    home_page.click_element(button_sign_up)
    home_page.wait_for_element_visible_by_locator(paragraph_successful_alert)
    assert home_page.is_element_visible(paragraph_successful_alert)
    assert home_page.is_element_text_contains_expected_text(paragraph_successful_alert, "Evgeny")
