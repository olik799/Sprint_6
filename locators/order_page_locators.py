from selenium.webdriver.common.by import By


class OrderPageLocators:
    TOP_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text() = 'Заказать']"]
    NAME_FIELD = [By.XPATH, "//input[@placeholder = '* Имя']"]
    FIRST_NAME_FIELD = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    METRO_STATION = [By.XPATH, "//input[@placeholder = '* Станция метро']"]
    METRO_STATION_ROLL = [By.XPATH, "//div[contains(@class, 'select-search')]/ul/li[1]"]
    PHONE_NUMBER_FIELD = [By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    BACK_BUTTON = [By.XPATH, "//button[text()='Назад']"]
    DATE_FIELD = [By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"]
    CALENDAR = [By.XPATH, "//*[text() = '28']/parent::div"]
    RENTAL_PERIOD_FIELD = [By.XPATH, "//div[contains(@class, 'Dropdown-root')]"]
    PERIOD_ROLL = [By.CLASS_NAME, "Dropdown-menu"]
    PERIOD = [By.XPATH, "//*[text() = 'сутки']/parent::div[@class = 'Dropdown-menu']"]
    ORDER_BUTTON_IN_ORDER_FORM = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text() = 'Заказать']"]
    YES_IN_POP_UP_ORDER_MODAL = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text() = 'Да']"]
    ORDER_MODAL_SUCCESS = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]
    LOW_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text() = 'Заказать']"]
