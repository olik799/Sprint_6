from pages.base_page import BasePage
from locators.base_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.OrderPageLocators = OrderPageLocators
        self.driver = driver

    @allure.step('Загрузка страницы')
    def load_page(self):
        self.navigate(self)

#    @allure.step('Верхняя кнопка "Заказать"')
#    def select_top_order_button(self):
#        self.click_element(BasePageLocators.TOP_ORDER_BUTTON)

    @allure.step('Ввод имени')
    def set_name(self, name):
        self.enter_text(BasePageLocators.NAME_FIELD, name)

    @allure.step('Ввод фамилии')
    def set_first_name(self, first_name):
        self.enter_text(OrderPageLocators.FIRST_NAME_FIELD, first_name)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Ввыбор станции метро')
    def select_metro_station(self):
        self.click_element(OrderPageLocators.METRO_STATION)
        self.click_element(OrderPageLocators.METRO_STATION_ROLL)

    @allure.step('Ввод номера телефона')
    def set_phone_number(self, phone_number):
        self.enter_text(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step('Переход на следующую страницу оформления заказа')
    def go_to_next_page(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)
