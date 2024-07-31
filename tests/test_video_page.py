from tests.data.selectors.common_selectors import div_carousel, button_carousel_previous, img_carousel_item_7, \
    button_carousel_next, img_carousel_item_2, buttons_carousel, button_open_chat, opened_chat, collapse_cards, \
    anchor_learning_process, link_about_me_youtube
from tests.data.selectors.home_page_selectors import button_sign_up_top
from tests.data.selectors.outdoor_page_selectors import youtube_channel_title
from tests.data.selectors.practical_task_page_selectors import title_practical_task
from tests.data.selectors.video_page_selectors import *
from tests.data.selectors.video_with_dz_page_selectors import title_access_to_video_dz_course
from tests.data.selectors.video_without_dz_page_selectors import title_access_to_video_no_dz_course
from utils.client import VIDEO, VIDEO_DZ, VIDEO_NO_DZ, PRACTICAL_TASK, URL


def test_video_page_open(video_page):
    assert video_page.is_current_url(VIDEO)
    video_page.wait_for_element_visible_by_locator(paragraph_study_whenever_you_want)
    assert video_page.is_element_visible(paragraph_study_whenever_you_want)


def test_button_get_access_click(video_page):
    video_page.click_element(button_get_access)
    video_page.wait_for_scroll_to_element(title_price)
    assert video_page.is_element_visible(title_price)


def test_anchor_learning_process_click(video_page):
    video_page.scroll_to_element(anchor_learning_process)
    video_page.click_element(anchor_learning_process)
    video_page.wait_for_scroll_to_element(anchor_learning_process)
    assert video_page.is_element_in_viewport(anchor_learning_process)


def test_link_about_me_youtube_click(video_page):
    video_page.scroll_to_element(link_about_me_youtube)
    video_page.click_element(link_about_me_youtube)
    video_page.wait_for_element_visible_by_locator(youtube_channel_title)
    assert video_page.is_element_in_viewport(youtube_channel_title)


def test_link_join_a_group_click(video_page):
    video_page.scroll_to_element(link_join_a_group)
    video_page.wait_for_scroll_to_element(link_join_a_group)
    video_page.click_element(link_join_a_group)
    video_page.wait_for_element_visible_by_locator(button_sign_up_top)
    assert video_page.is_element_visible(button_sign_up_top)
    assert video_page.is_current_url(URL)


def test_collapse_cards_click(video_page):
    video_page.scroll_to_element_top_of_screen(collapse_cards)
    video_page.wait_for_scroll_to_element(collapse_cards)
    video_page.click_all_collapse_elements(collapse_cards, "collapsed")


def test_button_pay_access_click(video_page):
    video_page.scroll_to_element(button_pay_access)
    video_page.wait_for_scroll_to_element(button_pay_access)
    video_page.click_element(button_pay_access)
    video_page.wait_for_element_visible_by_locator(title_access_to_video_dz_course)
    assert video_page.is_current_url(VIDEO_DZ)
    assert video_page.is_element_visible(title_access_to_video_dz_course)


def test_click_button_pay_access_without_home_tasks(video_page):
    video_page.scroll_to_element(button_pay_access_without_home_tasks)
    video_page.wait_for_scroll_to_element(button_pay_access_without_home_tasks)
    video_page.click_element(button_pay_access_without_home_tasks)
    video_page.wait_for_element_visible_by_locator(title_access_to_video_no_dz_course)
    assert video_page.is_current_url(VIDEO_NO_DZ)
    assert video_page.is_element_visible(title_access_to_video_no_dz_course)


def test_button_get_practical_task_click(video_page):
    video_page.scroll_to_element(button_get_a_practical_assignment)
    video_page.wait_for_scroll_to_element(button_get_a_practical_assignment)
    video_page.click_element(button_get_a_practical_assignment)
    video_page.wait_for_element_visible_by_locator(title_practical_task)
    assert video_page.is_current_url(PRACTICAL_TASK)
    assert video_page.is_element_in_viewport(title_practical_task)


def test_carousel_previous_button_click(video_page):
    video_page.scroll_to_element_top_of_screen(div_carousel)
    video_page.wait_for_scroll_to_element(div_carousel)
    video_page.click_element(button_carousel_previous)
    video_page.wait_for_element_visible_by_locator(img_carousel_item_7)
    assert video_page.is_element_in_viewport(img_carousel_item_7)


def test_carousel_next_button_click(video_page):
    video_page.scroll_to_element_top_of_screen(div_carousel)
    video_page.wait_for_scroll_to_element(div_carousel)
    video_page.click_element(button_carousel_next)
    video_page.wait_for_element_visible_by_locator(img_carousel_item_2)
    assert video_page.is_element_in_viewport(img_carousel_item_2)


def test_all_carousel_pages_click(video_page):
    video_page.scroll_to_element_top_of_screen(div_carousel)
    video_page.wait_for_scroll_to_element(div_carousel)
    video_page.click_all_carousel_elements(buttons_carousel)


def test_button_open_chat_click(video_page):
    video_page.scroll_to_element(button_open_chat)
    video_page.wait_for_scroll_to_element(button_open_chat)
    video_page.click_element(button_open_chat)
    video_page.wait_for_element_visible_by_locator(opened_chat)
    assert video_page.is_element_visible(opened_chat)
