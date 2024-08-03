import allure
import pytest

from utils.client import VIDEO, URL, allure_annotations

from tests.data.selectors.video_page_selectors import *
from tests.data.selectors.home_page_selectors import button_sign_up_top
from tests.data.selectors.outdoor_page_selectors import youtube_channel_title
from tests.data.selectors.common_selectors import collapse_cards, link_about_me_youtube

from tests.data.tests_data.parametrize_video_page import buttons_video_course_dz_no_dz, \
    buttons_video_course_dz_no_dz_ids


@allure_annotations(
    title="Video Page",
    story="Open video page",
    description='This test checks if the video page is open correctly',
    tag='Positive',
    severity=allure.severity_level.BLOCKER
)
def test_video_page_open(video_page):
    assert video_page.is_current_url(VIDEO)
    video_page.wait_for_element_visible_by_locator(paragraph_study_whenever_you_want)
    assert video_page.is_element_visible(paragraph_study_whenever_you_want)


@allure_annotations(
    title="Video Page",
    story="Get access button click",
    description='This test checks if the "get access" button is clickable and redirects to the correct target on page',
    tag='Positive'
)
def test_button_get_access_click(video_page):
    video_page.click_element(button_get_access)
    video_page.wait_for_scroll_to_element(title_price)
    assert video_page.is_element_visible(title_price)


@allure_annotations(
    title="Video Page",
    story="About me youtube button click",
    description='This test checks if the "about me youtube" button is clickable and redirects to the "YouTube" page',
    tag='Positive'
)
def test_link_about_me_youtube_click(video_page):
    video_page.scroll_wait_click_element_by_locator(link_about_me_youtube)
    video_page.wait_for_element_visible_by_locator(youtube_channel_title)
    assert video_page.is_element_in_viewport(youtube_channel_title)


@allure_annotations(
    title="Video Page",
    story="Join a group button click",
    description='This test checks if the "join a group" link is clickable and redirects to the home page',
    tag='Positive'
)
def test_link_join_a_group_click(video_page):
    video_page.scroll_wait_click_element_by_locator(link_join_a_group)
    video_page.wait_for_element_visible_by_locator(button_sign_up_top)
    assert video_page.is_element_visible(button_sign_up_top)
    assert video_page.is_current_url(URL)


@allure_annotations(
    title="Video Page",
    story="Collapse cards click",
    description='This test checks if the collapse cards are clickable and toggles their visibility',
    tag='Positive'
)
def test_collapse_cards_click(video_page):
    video_page.scroll_to_element_top_of_screen(collapse_cards)
    video_page.wait_for_scroll_to_element(collapse_cards)
    video_page.click_all_collapse_elements(collapse_cards, "collapsed")


@allure_annotations(
    title="Video Page",
    story="Buttons pay access click",
    description='This test checks if the "get access" buttons is clickable and redirects to the correct pages',
    tag='Positive',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.parametrize("btn, target, url", buttons_video_course_dz_no_dz, ids=buttons_video_course_dz_no_dz_ids)
def test_buttons_pay_access_click(video_page, btn, target, url):
    video_page.scroll_wait_click_element_by_locator(btn)
    video_page.wait_for_element_visible_by_locator(target)
    assert video_page.is_current_url(url)
    assert video_page.is_element_visible(target)
