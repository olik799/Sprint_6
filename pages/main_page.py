from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Ожидание загрузки страницы')
    def wait_for_load_next_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.
                                            visibility_of_element_located(OrderPageLocators.NAME_FIELD))

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()
