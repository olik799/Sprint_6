import pytest
from selenium import webdriver
from config import URL
from pages.order_page import OrderPageScooter
import allure


class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(URL)
        cls.order_page = OrderPageScooter(cls.driver)

    @pytest.mark.parametrize(
        "user, name, first_name, address", [
            ("1", "Иван", "Иванов", "Москва, ул. Тверская"),
            ("2", "Петр", "Петров", "Москва, ул. Пушкинская"),
        ]
    )
    @allure.title('Проверка заказа самоката')
    def test_order_scooter_top_order_button(self, user, name, first_name, address):
        self.driver.get(URL)
        self.order_page.select_order_button_for_user(user)
        self.order_page.set_name(name)
        self.order_page.set_first_name(first_name)
        self.order_page.set_address(address)
        self.order_page.select_metro_station()
        self.order_page.set_phone_number()
        self.order_page.go_to_next_page()
        self.order_page.set_customer_add_data()
        self.order_page.confirm_order()

        assert 'Номер заказа' in self.order_page.text_in_modal_pop_up()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
