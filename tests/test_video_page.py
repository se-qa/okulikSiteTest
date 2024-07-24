from utils.client import VIDEO


def test_video_page(driver, video_page):
    video_page.open(VIDEO)
