from pages.main_page import MainPage
from config import URL
import allure


class TestRedirect:

    @allure.title('Проверка перехода на главную страницу по клику на логотип Самоката')
    def test_redirect_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.wait_for_load_next_page()
        main_page.click_logo_scooter()
        assert main_page.current_url() == URL

    @allure.title('Проверка перехода на страницу Дзена по клику на логотип Яндекса')
    def test_redirect_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        main_page.switch_window()
        assert 'dzen.ru' in main_page.current_url()
