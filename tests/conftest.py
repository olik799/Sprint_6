import pytest
from selenium import webdriver
from config import URL, RESOLUTION


def browser_settings():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument(f'--window-size={RESOLUTION[0]}, {RESOLUTION[1]}')
    return firefox_options


@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=browser_settings())
    firefox.get(URL)
    yield firefox
    firefox.quit()
