from selenium.webdriver.common.by import By


class BasePageLocators:
    TOP_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text() = 'Заказать']"
    LOW_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text() = 'Заказать']"
    NAME_FIELD = By.XPATH, "//input[@placeholder = '* Имя']"
