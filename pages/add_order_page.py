from pages.base_page import BasePage
from locators.add_order_page_locators import AddOrderPageLocators
import allure


class AddOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.AddOrderPageLocators = AddOrderPageLocators
        self.driver = driver

    @allure.step('Ожидание загрузки формы "Про аренду"')
    def wait_for_load_next_page(self):
        self.wait_for_element_visible(AddOrderPageLocators.BACK_BUTTON)

    def set_date(self):
        self.click_element(AddOrderPageLocators.DATE_FIELD)
        self.click_element(AddOrderPageLocators.CALENDAR)

    def set_rent_period(self):
        self.click_element(AddOrderPageLocators.RENTAL_PERIOD_FIELD)
        self.wait_for_element_visible(AddOrderPageLocators.PERIOD_ROLL)
        self.click_element(AddOrderPageLocators.PERIOD)

    @allure.step('Выбор даты и срока аренды')
    def set_customer_add_data(self):
        self.set_date()
        self.set_rent_period()

    @allure.step('Подтверждение заказа')
    def select_order_button(self):
        self.click_element(AddOrderPageLocators.ORDER_BUTTON_IN_ORDER_FORM)
