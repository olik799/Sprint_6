from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class OrderConfirmPopUp(BasePage):

    _YES_IN_POP_UP_ORDER_MODAL = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text() = 'Да']"
    _ORDER_MODAL_SUCCESS = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_pop_up(self):
        self.wait_for_element_visible(self._YES_IN_POP_UP_ORDER_MODAL)

    def select_confirm_button(self):
        self.click_element(self._YES_IN_POP_UP_ORDER_MODAL)

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.wait_for_pop_up()
        self.select_confirm_button()

    def text_in_modal_pop_up(self):
        return self.get_text(self._ORDER_MODAL_SUCCESS)
