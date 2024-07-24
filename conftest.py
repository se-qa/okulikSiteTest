import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.person_page import PersonPage
from pages.recovery_page import RecoveryPage
from pages.register_page import RegisterPage
from pages.video_page import VideoPage
from pages.home_page import HomePage
from utils.client import load_config, get_chrome_options


@pytest.fixture
def driver():
    config = load_config()
    options = get_chrome_options(config["chrome_options"])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def video_page(driver):
    return VideoPage(driver)


@pytest.fixture
def person_page(driver):
    return PersonPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def recovery_page(driver):
    return RecoveryPage(driver)


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)
