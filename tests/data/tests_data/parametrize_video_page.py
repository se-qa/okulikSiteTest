from utils.client import VIDEO_DZ, VIDEO_NO_DZ

from tests.data.locators.video_with_dz_page_locators import title_access_to_video_dz_course
from tests.data.locators.video_without_dz_page_locators import title_access_to_video_no_dz_course
from tests.data.locators.video_page_locators import VideoPageLocators as locVid

buttons_video_course_dz_no_dz = [
    (locVid.button_pay_access, title_access_to_video_dz_course, VIDEO_DZ),
    (locVid.button_pay_access_without_home_tasks, title_access_to_video_no_dz_course, VIDEO_NO_DZ)
]

buttons_video_course_dz_no_dz_ids = [
    "button pay access - dz course",
    "button pay access without home tasks - no dz course"
]
