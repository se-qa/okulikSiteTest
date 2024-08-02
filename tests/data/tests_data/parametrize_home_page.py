from utils.client import FULL_PRICE, PART_PRICE, VIDEO

from tests.data.selectors.home_page_selectors import *
from tests.data.selectors.common_selectors import *
from tests.data.selectors import part_price_page_selectors, full_price_page_selectors, video_page_selectors, \
    outdoor_page_selectors

anchors_top_list = [
    (anchor_course_program, title_course_program),
    (anchor_nearest_course, title_start_group),
    (anchor_price, title_price),
    (anchor_booking, title_booking)
]

anchors_top_list_ids = ["Course program", "Nearest course", "Price", "Booking"]

buy_links_list = [
    (link_full_price, full_price_page_selectors.title_full_price, FULL_PRICE),
    (link_part_price, part_price_page_selectors.title_part_price, PART_PRICE),
    (link_video_price, video_page_selectors.paragraph_study_whenever_you_want, VIDEO)
]

buy_links_list_ids = ["Full price",
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

other_links_list_ids = ["Senior Tester",
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

pages_and_common_selectors_list = [
        ("home_page", button_open_chat, opened_chat),
        ("home_page", link_copyright, button_sign_up_top),
        ("home_page", link_payment_rules, div_payment_rules),
        ("home_page", link_offer, title_offer),
        ("video_page", button_open_chat, opened_chat),
        ("video_page", link_copyright, button_sign_up_top),
        ("video_page", link_payment_rules, div_payment_rules),
        ("video_page", link_offer, title_offer),
    ]

pages_and_common_selectors_list_ids = [
        "home page - open chat",
        "home page - copyright",
        "home page - payment rules",
        "home page - offer",
        "video page - open chat",
        "video page - copyright",
        "video page - payment rules",
        "video page - offer"
    ]
