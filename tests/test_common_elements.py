import allure
import pytest

from utils.client import PRACTICAL_TASK, allure_annotations

from tests.data.locators.home_page_locators import HomePageLocators as locHP
from tests.data.locators.practical_task_page_locators import title_practical_task
from tests.data.locators.common_locators import CommonLocators as locCom

from tests.data.tests_data.parametrize_common import class_pages_list_ids, class_pages_list, \
    pages_and_common_elements_list, pages_and_common_elements_list_ids, pages_and_carousel_buttons_list, \
    pages_and_carousel_buttons_list_ids


@allure_annotations(
    title="Anchor learning process click",
    feature="Common elements",
    story="Clicking an anchor",
    description='This test checks if the common anchors are clickable and redirects to the correct targets',
    tag='Positive'
)
@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_anchor_learning_process_click(testing_page):
    testing_page.scroll_wait_click_element_by_locator(locCom.anchor_learning_process)
    testing_page.waiting_conditions.wait_for_scroll_to_element(locCom.title_learning_process)
    assert testing_page.element_state_checking.is_element_in_viewport(locCom.title_learning_process)


@allure_annotations(
    title="Button get practical task click",
    feature="Common elements",
    story="Clicking a button",
    description='This test checks if the "get practical task" button is clickable and redirects to the "practice" page',
    tag='Positive',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_button_get_practical_task_click(testing_page):
    testing_page.scroll_wait_click_element_by_locator(locHP.button_get_a_practical_task)
    testing_page.waiting_conditions.wait_for_element_visible_by_locator(title_practical_task)
    assert testing_page.element_state_checking.is_current_url(PRACTICAL_TASK)
    assert testing_page.element_state_checking.is_element_in_viewport(title_practical_task)


@allure_annotations(
    title="Carousel buttons click",
    feature="Common elements",
    story="Clicking a button",
    description='This test checks if the carousel previous and next buttons are clickable and toggles their visibility',
    tag='Positive'
)
@pytest.mark.parametrize("testing_page, button_to_click, img_to_check", pages_and_carousel_buttons_list,
                         ids=pages_and_carousel_buttons_list_ids, indirect=["testing_page"])
def test_carousel_button_click(testing_page, button_to_click, img_to_check):
    testing_page.scroll_wait_click_element_by_locator(locCom.div_carousel, button_to_click, scroll_option='top')
    testing_page.waiting_conditions.wait_for_element_visible_by_locator(img_to_check)
    assert testing_page.element_state_checking.is_element_in_viewport(img_to_check)


@allure_annotations(
    title="Carousel elements click",
    feature="Common elements",
    story="Clicking an element",
    description='This test checks if the carousel elements are clickable and toggles their visibility',
    tag='Positive'
)
@pytest.mark.parametrize("testing_page", class_pages_list, ids=class_pages_list_ids, indirect=True)
def test_all_carousel_pages_click(testing_page):
    testing_page.utility_functions.scroll_to_element_top_of_screen(locCom.div_carousel)
    testing_page.waiting_conditions.wait_for_scroll_to_element(locCom.div_carousel)
    testing_page.click_all_carousel_elements(locCom.buttons_carousel, locCom.img_carousel_items)


@allure_annotations(
    title="Multiple elements click",
    feature="Common elements",
    story="Clicking an element",
    description='This test checks if the common button "open chat" and links are clickable and redirects to the '
                + 'correct pages',
    tag='Positive'
)
@pytest.mark.parametrize("testing_page, locator_to_click, locator_to_check", pages_and_common_elements_list,
                         ids=pages_and_common_elements_list_ids, indirect=["testing_page"])
def test_multiple_elements_click(testing_page, locator_to_click, locator_to_check):
    testing_page.scroll_wait_click_element_by_locator(locator_to_click)
    testing_page.waiting_conditions.wait_for_element_visible_by_locator(locator_to_check)
    assert testing_page.element_state_checking.is_element_visible(locator_to_check)
