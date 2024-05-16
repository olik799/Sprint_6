from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    HEAD_QUESTION_PAGE = [By.XPATH, "//div[text() = 'Вопросы о важном']"]
    FIRST_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-0']/parent::*[@class = 'accordion__heading']"] # указатель первого вопроса
    FIRST_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Сутки — 400 рублей')]"]
    SECOND_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-1']/parent::*[@class = 'accordion__heading']"] # указатель второго вопроса
    SECOND_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Пока что у нас так:')]"]
    THIRD_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-2']/parent::*[@class = 'accordion__heading']"]  # указатель третьего вопроса
    THIRD_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Допустим, вы оформляете')]"]
    FOURTH_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-3']/parent::*[@class = 'accordion__heading']"]  # указатель четвертого вопроса
    FOURTH_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Только начиная с завтрашнего дня')]"]
    FIFTH_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-4']/parent::*[@class = 'accordion__heading']"]  # указатель пятого вопроса
    FIFTH_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Пока что нет')]"]
    SIXTH_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-5']/parent::*[@class = 'accordion__heading']"]  # указатель шестого вопроса
    SIXTH_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Самокат приезжает к вам')]"]
    SEVENTH_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-6']/parent::*[@class = 'accordion__heading']"]  # указатель седьмого вопроса
    SEVENTH_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Да, пока самокат')]"]
    EIGHTH_QUESTION_SIGN = [By.XPATH, "//*[@id = 'accordion__heading-7']/parent::*[@class = 'accordion__heading']"]  # указатель восьмого вопроса
    EIGHTH_QUESTION_TEXT = [By.XPATH, "//p[starts-with(text(),'Да, обязательно')]"]
