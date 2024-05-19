from selenium.webdriver.common.by import By


class AddOrderPageLocators:
    BACK_BUTTON = By.XPATH, "//button[text()='Назад']"
    DATE_FIELD = By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//*[text() = '28']/parent::div"
    RENTAL_PERIOD_FIELD = By.XPATH, "//div[contains(@class, 'Dropdown-root')]"
    PERIOD_ROLL = By.CLASS_NAME, "Dropdown-menu"
    PERIOD = By.XPATH, "//*[text() = 'сутки']/parent::div[@class = 'Dropdown-menu']"
    ORDER_BUTTON_IN_ORDER_FORM = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text() = 'Заказать']"
