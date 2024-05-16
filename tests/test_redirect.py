from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPageScooter
from config import URL
import allure


class TestRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(URL)
        cls.main_page = MainPageScooter(cls.driver)

    @allure.title('Проверка перехода на главную страницу по клику на логотип Самоката')
    def test_redirect_main_page(self):
        self.main_page.click_order_button()
        self.main_page.wait_for_load_next_page()
        self.main_page.click_logo_scooter()
        assert self.driver.current_url == URL

    @allure.title('Проверка перехода на страницу Дзена по клику на логотип Яндекса')
    def test_redirect_dzen(self):
        original_window = self.driver.current_window_handle
        self.main_page.click_logo_yandex()
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Дзен"))

        assert 'dzen.ru' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
