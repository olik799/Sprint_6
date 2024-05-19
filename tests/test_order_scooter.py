from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.add_order_page import AddOrderPage
from pages.order_confirm_popup_page import OrderConfirmPopUp
from data import name, first_name, address, phone_number
import allure


class TestOrderScooter:

    @allure.title('Проверка заказа самоката через верхнюю кнопку "Заказать"')
    def test_order_scooter_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        order_page = OrderPage(driver)
        order_page.set_name(name)
        order_page.set_first_name(first_name)
        order_page.set_address(address)
        order_page.select_metro_station()
        order_page.set_phone_number(phone_number)
        order_page.go_to_next_page()
        add_order_page = AddOrderPage(driver)
        add_order_page.wait_for_load_next_page()
        add_order_page.set_customer_add_data()
        add_order_page.select_order_button()
        order_confirm_popup_page = OrderConfirmPopUp(driver)
        order_confirm_popup_page.confirm_order()
        assert 'Номер заказа' in order_confirm_popup_page.text_in_modal_pop_up()

    @allure.title('Проверка заказа самоката через нижнюю кнопку "Заказать"')
    def test_order_scooter_low_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.select_low_order_button()
        order_page = OrderPage(driver)
        order_page.set_name(name)
        order_page.set_first_name(first_name)
        order_page.set_address(address)
        order_page.select_metro_station()
        order_page.set_phone_number(phone_number)
        order_page.go_to_next_page()
        add_order_page = AddOrderPage(driver)
        add_order_page.wait_for_load_next_page()
        add_order_page.set_customer_add_data()
        add_order_page.select_order_button()
        order_confirm_popup_page = OrderConfirmPopUp(driver)
        order_confirm_popup_page.confirm_order()
        assert 'Номер заказа' in order_confirm_popup_page.text_in_modal_pop_up()
