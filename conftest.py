import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.home_page import HomePage
from pages.video_page import VideoPage
from pages.login_page import LoginPage
from pages.person_page import PersonPage
from pages.recovery_page import RecoveryPage
from pages.register_page import RegisterPage

from utils.browser_options import options_map
from utils.client import load_config, get_chrome_options, URL, VIDEO, PERSON, LOGIN, RESET, REGISTER


def pytest_addoption(parser):
    parser.addoption("--incognito", action="store_true", default=False, help="Run tests in incognito mode")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")
    parser.addoption("--disable-cache", action="store_true", default=False, help="Disable browser cache")
    parser.addoption("--disable-notifications", action="store_true", default=False,
                     help="Disable browser notifications")


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> WebDriver:
    config: dict = load_config()
    options: Options = get_chrome_options(config["chrome_options"])

    for option, argument in options_map.items():
        if request.config.getoption(f"--{option}"):
            options.add_argument(argument)
            print(f"Added argument: {argument}")

    driver: webdriver.Chrome = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def testing_page(request: pytest.FixtureRequest) -> HomePage | VideoPage:
    page_fixture = request.param
    return request.getfixturevalue(page_fixture)


@pytest.fixture
def home_page(driver: WebDriver) -> HomePage:
    driver.get(URL)
    return HomePage(driver)


@pytest.fixture
def video_page(driver: WebDriver) -> VideoPage:
    driver.get(VIDEO)
    return VideoPage(driver)


@pytest.fixture
def person_page(driver: WebDriver) -> PersonPage:
    driver.get(PERSON)
    return PersonPage(driver)


@pytest.fixture
def login_page(driver: WebDriver) -> LoginPage:
    driver.get(LOGIN)
    return LoginPage(driver)


@pytest.fixture
def recovery_page(driver: WebDriver) -> RecoveryPage:
    driver.get(RESET)
    return RecoveryPage(driver)


@pytest.fixture
def register_page(driver: WebDriver) -> RegisterPage:
    driver.get(REGISTER)
    return RegisterPage(driver)
