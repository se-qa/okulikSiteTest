import os
import json

from pathlib import Path

from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

load_dotenv()

URL: str = os.getenv('BASE_URL')
VIDEO: str = os.getenv('VIDEO_URL')
PERSON: str = os.getenv('LK_URL')
RESET: str = os.getenv('RESET_PASS_URL')
REGISTER: str = os.getenv('REGISTER_URL')
LOGIN: str = os.getenv('LOGIN_URL')
FULL_PRICE: str = os.getenv('FULL_PRICE_URL')
PART_PRICE: str = os.getenv('PART_PRICE_URL')
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

    argument_mappings = {
        "start_maximized": "--start-maximized",
        "ignore_certificate_errors": "--ignore-certificate-errors",
        "disable_popup_blocking": "--disable-popup-blocking",
        "disable_extensions": "--disable-extensions",
        "incognito": "--incognito",
        "headless": "--headless",
        "disable_gpu": "--disable-gpu",
        "disable_cache": "--disable-cache",
        "disable_notifications": "--disable-notifications",
        "disable_autofill": "--disable-autofill"
    }

    for key, argument in argument_mappings.items():
        add_argument_if_present(options, config, key, argument)

    custom_args = config.get("custom_args", [])
    for arg in custom_args:
        options.add_argument(arg)
        print(f"Added custom argument: {arg}")

    return options
