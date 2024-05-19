from pages.base_page import BasePage
from locators.base_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Ожидание загрузки страницы')
    def wait_for_load_next_page(self):
        self.wait_for_element_visible(BasePageLocators.NAME_FIELD)

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_order_button(self):
        self.click_element(BasePageLocators.TOP_ORDER_BUTTON)

    @allure.step('Переход и клик по нижней кнопке "Заказать"')
    def select_low_order_button(self):
        self.scroll_page(BasePageLocators.LOW_ORDER_BUTTON)
        self.wait_for_element_visible(BasePageLocators.LOW_ORDER_BUTTON)
        self.click_element(BasePageLocators.LOW_ORDER_BUTTON)

    @allure.step('Получаем URL текущей страницы')
    def current_url(self):
        return self.get_current_url()

    @allure.step('Перемещаемся вниз по странице до Вопросов о главном')
    def move_to_question(self):
        self.scroll_page(MainPageLocators.HEAD_QUESTION_PAGE)
        self.wait_for_element_visible(MainPageLocators.EIGHTH_QUESTION_SIGN)

    @allure.step('Кликаем по вопросу')
    def select_question(self, locator):
        self.click_element(locator)

    @allure.step('Получаем ответ')
    def get_answer(self, locator):
        return self.get_text(locator)

    @allure.step('Переключаемся между открытыми окнами браузера')
    def switch_window(self):
        self.switch_to_new_window()
