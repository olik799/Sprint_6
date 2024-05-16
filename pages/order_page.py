from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import phone_number
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбор кнопки "Заказать"')
    def select_order_button_for_user(self, user):
        if user == "2":
            self.select_low_order_button()
        else:
            self.select_top_order_button()

    @allure.step('Верхняя кнопка')
    def select_top_order_button(self):
        self.driver.find_element(*OrderPageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Нижняя кнопка')
    def select_low_order_button(self):
        element = self.driver.find_element(*OrderPageLocators.LOW_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        (WebDriverWait(self.driver, 5).until(expected_conditions.
                                             visibility_of_element_located(OrderPageLocators.LOW_ORDER_BUTTON)))
        self.driver.find_element(*OrderPageLocators.LOW_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                              NAME_FIELD))

    @allure.step('Ввод имени')
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    @allure.step('Ввод фамилии')
    def set_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Ввыбор станции метро')
    def select_metro_station(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATION).click()
        self.driver.find_element(*OrderPageLocators.METRO_STATION_ROLL).click()

    @allure.step('Ввод номера телефона')
    def set_phone_number(self):
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)

    @allure.step('Переход на следующую страницу оформления заказа')
    def go_to_next_page(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.
                                            visibility_of_element_located(OrderPageLocators.BACK_BUTTON))

    def set_date(self):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.CALENDAR).click()

    def set_rent_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.PERIOD_ROLL))
        self.driver.find_element(*OrderPageLocators.PERIOD).click()

    @allure.step('Выбор даты и срока аренды')
    def set_customer_add_data(self):
        self.set_date()
        self.set_rent_period()

    def select_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_IN_ORDER_FORM).click()

    def wait_for_modal_pop_up(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                              YES_IN_POP_UP_ORDER_MODAL))

    def select_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.YES_IN_POP_UP_ORDER_MODAL).click()

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.select_order_button()
        self.wait_for_modal_pop_up()
        self.select_confirm_button()

    def text_in_modal_pop_up(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_MODAL_SUCCESS).text
