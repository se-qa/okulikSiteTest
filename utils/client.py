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

BASE_DIR: Path = Path(__file__).resolve().parent.parent
ENV_FILE: Path = BASE_DIR / '.env'
CONFIG_FILE: Path = BASE_DIR / 'config.json'


def load_config():
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)


def get_chrome_options(config):
    options = Options()
    if config.get("start_maximized", False):
        options.add_argument("--start-maximized")
    if config.get("ignore_certificate_errors", False):
        options.add_argument("--ignore-certificate-errors")
    if config.get("disable_popup_blocking", False):
        options.add_argument("--disable-popup-blocking")
    if config.get("disable_extensions", False):
        options.add_argument("--disable-extensions")
    if config.get("incognito", False):
        options.add_argument("--incognito")
    if config.get("headless", False):
        options.add_argument("--headless")
    if config.get("disable_gpu", False):
        options.add_argument("--disable-gpu")
    if config.get("disable_cache", False):
        options.add_argument("--disable-cache")
    if config.get("disable_notifications", False):
        options.add_argument("--disable-notifications")
    if config.get("disable_autofill", False):
        options.add_argument("--disable-autofill")
    return options
