from utils.client import VIDEO_DZ, VIDEO_NO_DZ

from tests.data.selectors.video_with_dz_page_selectors import title_access_to_video_dz_course
from tests.data.selectors.video_without_dz_page_selectors import title_access_to_video_no_dz_course
from tests.data.selectors.video_page_selectors import button_pay_access, button_pay_access_without_home_tasks

buttons_video_course_dz_no_dz = [
    (button_pay_access, title_access_to_video_dz_course, VIDEO_DZ),
    (button_pay_access_without_home_tasks, title_access_to_video_no_dz_course, VIDEO_NO_DZ)
]

buttons_video_course_dz_no_dz_ids = [
    "button pay access - dz course",
    "button pay access without home tasks - no dz course"
]
