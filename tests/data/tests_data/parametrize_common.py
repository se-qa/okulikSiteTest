from tests.data.selectors.home_page_selectors import button_sign_up_top
from tests.data.selectors.common_selectors import button_open_chat, link_copyright, link_payment_rules, link_offer, \
    title_offer, opened_chat, div_payment_rules, button_carousel_previous, img_carousel_item_2, img_carousel_item_7, \
    button_carousel_next

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
