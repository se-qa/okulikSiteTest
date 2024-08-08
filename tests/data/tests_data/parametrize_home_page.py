from tests.data.locators.full_price_page_locators import title_full_price
from tests.data.locators.outdoor_page_locators import youtube_channel_title, telegram_channel_title
from tests.data.locators.part_price_page_locators import title_part_price
from utils.client import FULL_PRICE, PART_PRICE, VIDEO

from tests.data.locators.common_locators import CommonLocators as locCom
from tests.data.locators.video_page_locators import VideoPageLocators as locVid
from tests.data.locators.home_page_locators import HomePageLocators as locHP


anchors_top_list = [
    (locHP.anchor_course_program, locHP.title_course_program),
    (locHP.anchor_nearest_course, locHP.title_start_group),
    (locHP.anchor_price, locHP.title_price),
    (locHP.anchor_booking, locHP.title_booking)
]

anchors_top_list_ids = [
    "Course program",
    "Nearest course",
    "Price",
    "Booking"
]

buy_links_list = [
    (locHP.link_full_price, title_full_price, FULL_PRICE),
    (locHP.link_part_price, title_part_price, PART_PRICE),
    (locHP.link_video_price, locVid.paragraph_study_whenever_you_want, VIDEO)
]

buy_links_list_ids = [
    "Full price",
    "Part price",
    "Video price"
]

other_links_list = [
    (locCom.link_about_me_youtube, youtube_channel_title,
     "https://www.youtube.com/@SeniorTester"),
    (locHP.link_video_course, locVid.paragraph_study_whenever_you_want, VIDEO),
    (locHP.link_full_price_middle, title_full_price, FULL_PRICE),
    (locHP.link_part_price_middle, title_part_price, PART_PRICE),
    (locHP.link_video_price_middle, locVid.paragraph_study_whenever_you_want, VIDEO),
    (locHP.link_telegram_step_by_step_radio, telegram_channel_title, "https://t.me/okulikby")
]

other_links_list_ids = [
    "Senior Tester",
    "video course",
    "Full price middle",
    "Part price middle",
    "Video price middle",
    "telegram"
]
