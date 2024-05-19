from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL
import time


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, driver):
        self.driver.get(URL)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))

    def scroll_page(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[1])
