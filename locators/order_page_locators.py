from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_FIELD = By.XPATH, "//input[@placeholder = '* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//input[@placeholder = '* Станция метро']"
    METRO_STATION_ROLL = By.XPATH, "//div[contains(@class, 'select-search')]/ul/li[1]"
    PHONE_NUMBER_FIELD = By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"
