from utils.client import FULL_PRICE, PART_PRICE, VIDEO, VIDEO_DZ, VIDEO_NO_DZ

from tests.data.selectors.common_selectors import *
from tests.data.selectors.home_page_selectors import *
from tests.data.selectors.video_with_dz_page_selectors import title_access_to_video_dz_course
from tests.data.selectors.video_without_dz_page_selectors import title_access_to_video_no_dz_course
from tests.data.selectors.video_page_selectors import button_pay_access, button_pay_access_without_home_tasks
from tests.data.selectors import part_price_page_selectors, full_price_page_selectors, video_page_selectors, \
    outdoor_page_selectors

anchors_top_list = [
    (anchor_course_program, title_course_program),
    (anchor_nearest_course, title_start_group),
    (anchor_price, title_price),
    (anchor_booking, title_booking)
]

anchors_top_list_ids = [
    "Course program",
    "Nearest course",
    "Price",
    "Booking"
]

buy_links_list = [
    (link_full_price, full_price_page_selectors.title_full_price, FULL_PRICE),
    (link_part_price, part_price_page_selectors.title_part_price, PART_PRICE),
    (link_video_price, video_page_selectors.paragraph_study_whenever_you_want, VIDEO)
]

buy_links_list_ids = [
    "Full price",
    "Part price",
    "Video price"
]

other_links_list = [
    (link_about_me_youtube, outdoor_page_selectors.youtube_channel_title, "https://www.youtube.com/@SeniorTester"),
    (link_video_course, video_page_selectors.paragraph_study_whenever_you_want, VIDEO),
    (link_full_price_middle, full_price_page_selectors.title_full_price, FULL_PRICE),
    (link_part_price_middle, part_price_page_selectors.title_part_price, PART_PRICE),
    (link_video_price_middle, video_page_selectors.paragraph_study_whenever_you_want, VIDEO),
    (link_telegram_step_by_step_radio, outdoor_page_selectors.telegram_channel_title, "https://t.me/okulikby")
]

other_links_list_ids = [
    "Senior Tester",
    "video course",
    "Full price middle",
    "Part price middle",
    "Video price middle",
    "telegram"
]

class_pages_list = [
    "home_page",
    "video_page"
]

class_pages_list_ids = [
    "home page",
    "video page"
]

pages_and_common_elements_list = [
    ("home_page", button_open_chat, opened_chat),
    ("home_page", link_copyright, button_sign_up_top),
    ("home_page", link_payment_rules, div_payment_rules),
    ("home_page", link_offer, title_offer),
    ("video_page", button_open_chat, opened_chat),
    ("video_page", link_copyright, button_sign_up_top),
    ("video_page", link_payment_rules, div_payment_rules),
    ("video_page", link_offer, title_offer),
]

pages_and_common_elements_list_ids = [
    "home page - open chat",
    "home page - copyright",
    "home page - payment rules",
    "home page - offer",
    "video page - open chat",
    "video page - copyright",
    "video page - payment rules",
    "video page - offer"
]

pages_and_carousel_buttons_list = [
    ("home_page", button_carousel_previous, img_carousel_item_7),
    ("home_page", button_carousel_next, img_carousel_item_2),
    ("video_page", button_carousel_previous, img_carousel_item_7),
    ("video_page", button_carousel_next, img_carousel_item_2)
]

pages_and_carousel_buttons_list_ids = [
    "home page - carousel previous",
    "home page - carousel next",
    "video page - carousel previous",
    "video page - carousel next"
]

buttons_video_course_dz_no_dz = [
    (button_pay_access, title_access_to_video_dz_course, VIDEO_DZ),
    (button_pay_access_without_home_tasks, title_access_to_video_no_dz_course, VIDEO_NO_DZ)
]

buttons_video_course_dz_no_dz_ids = [
    "button pay access - dz course",
    "button pay access without home tasks - no dz course"
]
