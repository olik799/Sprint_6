from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page_locators import QuestionsPageLocators
import allure


class QuestionPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Пролистываем страницу до раздела "Вопросы о важном"')
    def scroll_to_question(self):
        element = self.driver.find_element(*QuestionsPageLocators.HEAD_QUESTION_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        (WebDriverWait(self.driver, 5).
         until(expected_conditions.visibility_of_element_located(QuestionsPageLocators.EIGHTH_QUESTION_SIGN)))

    @allure.step('Кликаем по первому вопросу')
    def select_first_question(self):
        self.driver.find_element(*QuestionsPageLocators.FIRST_QUESTION_SIGN).click()

    def first_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.FIRST_QUESTION_TEXT).text

    @allure.step('Кликаем по второму вопросу')
    def select_second_question(self):
        self.driver.find_element(*QuestionsPageLocators.SECOND_QUESTION_SIGN).click()

    def second_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.SECOND_QUESTION_TEXT).text

    @allure.step('Кликаем по третьему вопросу')
    def select_third_question(self):
        self.driver.find_element(*QuestionsPageLocators.THIRD_QUESTION_SIGN).click()

    def third_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.THIRD_QUESTION_TEXT).text

    @allure.step('Кликаем по четвертому вопросу')
    def select_fourth_question(self):
        self.driver.find_element(*QuestionsPageLocators.FOURTH_QUESTION_SIGN).click()

    def fourth_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.FOURTH_QUESTION_TEXT).text

    @allure.step('Кликаем по пятаму вопросу')
    def select_fifth_question(self):
        self.driver.find_element(*QuestionsPageLocators.FIFTH_QUESTION_SIGN).click()

    def fifth_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.FIFTH_QUESTION_TEXT).text

    @allure.step('Кликаем по шестому вопросу')
    def select_sixth_question(self):
        self.driver.find_element(*QuestionsPageLocators.SIXTH_QUESTION_SIGN).click()

    def sixth_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.SIXTH_QUESTION_TEXT).text

    @allure.step('Кликаем по седьмому вопросу')
    def select_seventh_question(self):
        self.driver.find_element(*QuestionsPageLocators.SEVENTH_QUESTION_SIGN).click()

    def seventh_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.SEVENTH_QUESTION_TEXT).text

    @allure.step('Кликаем по восьмому вопросу')
    def select_eighth_question(self):
        self.driver.find_element(*QuestionsPageLocators.EIGHTH_QUESTION_SIGN).click()

    def eighth_answer(self):
        return self.driver.find_element(*QuestionsPageLocators.EIGHTH_QUESTION_TEXT).text
