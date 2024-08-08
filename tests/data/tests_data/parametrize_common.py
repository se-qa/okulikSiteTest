from tests.data.locators.home_page_locators import HomePageLocators as locHP
from tests.data.locators.common_locators import CommonLocators as locCom

class_pages_list = [
    "home_page",
    "video_page"
]

class_pages_list_ids = [
    "home page",
    "video page"
]

pages_and_common_elements_list = [
    ("home_page", locCom.button_open_chat, locCom.opened_chat),
    ("home_page", locCom.link_copyright, locHP.button_sign_up_top),
    ("home_page", locCom.link_payment_rules, locCom.div_payment_rules),
    ("home_page", locCom.link_offer, locCom.title_offer),
    ("video_page", locCom.button_open_chat, locCom.opened_chat),
    ("video_page", locCom.link_copyright, locHP.button_sign_up_top),
    ("video_page", locCom.link_payment_rules, locCom.div_payment_rules),
    ("video_page", locCom.link_offer, locCom.title_offer),
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
    ("home_page", locCom.button_carousel_previous, locCom.img_carousel_item_7),
    ("home_page", locCom.button_carousel_next, locCom.img_carousel_item_2),
    ("video_page", locCom.button_carousel_previous, locCom.img_carousel_item_7),
    ("video_page", locCom.button_carousel_next, locCom.img_carousel_item_2)
]

pages_and_carousel_buttons_list_ids = [
    "home page - carousel previous",
    "home page - carousel next",
    "video page - carousel previous",
    "video page - carousel next"
]
