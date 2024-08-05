import os
import json
import allure

from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from utils.browser_options import argument_mappings

from selenium.webdriver.chrome.options import Options

load_dotenv()

URL: str = os.getenv('BASE_URL')
PERSON: str = os.getenv('LK_URL')
VIDEO: str = os.getenv('VIDEO_URL')
LOGIN: str = os.getenv('LOGIN_URL')
RESET: str = os.getenv('RESET_PASS_URL')
REGISTER: str = os.getenv('REGISTER_URL')
FULL_PRICE: str = os.getenv('FULL_PRICE_URL')
PART_PRICE: str = os.getenv('PART_PRICE_URL')
VIDEO_DZ: str = os.getenv('VIDEO_WITH_DZ_URL')
VIDEO_NO_DZ: str = os.getenv('VIDEO_WITHOUT_DZ_URL')
PRACTICAL_TASK: str = os.getenv('PRACTICAL_TASK_URL')

BASE_DIR: Path = Path(__file__).resolve().parent.parent
ENV_FILE: Path = BASE_DIR / '.env'
CONFIG_FILE: Path = BASE_DIR / 'config.json'


def load_config() -> dict:
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)


def add_argument_if_present(options: Options, config: dict, key: str, argument: str) -> None:
    if config.get(key, False):
        options.add_argument(argument)
        print(f"Added argument: {argument}")


def get_chrome_options(config: dict) -> Options:
    options = Options()

    for key, argument in argument_mappings.items():
        add_argument_if_present(options, config, key, argument)

    custom_args = config.get("custom_args", [])
    for arg in custom_args:
        options.add_argument(arg)
        print(f"Added custom argument: {arg}")

    return options


def allure_annotations(title: str, story: str, description: str, tag: str,
                       severity: allure = allure.severity_level.NORMAL, feature: str = None) -> Any:
    def wrapper(func: Any) -> Any:
        func = allure.title(title)(func)
        func = allure.feature(feature)(func)
        func = allure.story(story)(func)
        func = allure.severity(severity)(func)
        func = allure.description(description)(func)
        func = allure.tag(tag)(func)
        return func

    return wrapper
