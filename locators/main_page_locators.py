from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO_SCOOTER = By.XPATH, "//img[@alt = 'Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt = 'Yandex']"
    HEAD_QUESTION_PAGE = By.XPATH, "//div[text() = 'Вопросы о важном']"
    FIRST_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-0']/parent::*[@class = 'accordion__heading']" # указатель первого вопроса
    FIRST_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'400 рублей')]"
    SECOND_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-1']/parent::*[@class = 'accordion__heading']" # указатель второго вопроса
    SECOND_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'у нас так:')]"
    THIRD_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-2']/parent::*[@class = 'accordion__heading']" # указатель третьего вопроса
    THIRD_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'вы оформляете')]"
    FOURTH_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-3']/parent::*[@class = 'accordion__heading']" # указатель четвертого вопроса
    FOURTH_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'Только начиная')]"
    FIFTH_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-4']/parent::*[@class = 'accordion__heading']" # указатель пятого вопроса
    FIFTH_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'Пока что нет')]"
    SIXTH_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-5']/parent::*[@class = 'accordion__heading']" # указатель шестого вопроса
    SIXTH_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'Самокат приезжает')]"
    SEVENTH_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-6']/parent::*[@class = 'accordion__heading']" # указатель седьмого вопроса
    SEVENTH_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'пока самокат')]"
    EIGHTH_QUESTION_SIGN = By.XPATH, "//*[@id = 'accordion__heading-7']/parent::*[@class = 'accordion__heading']" # указатель восьмого вопроса
    EIGHTH_QUESTION_TEXT = By.XPATH, "//p[contains(text(),'обязательно')]"