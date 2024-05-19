import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure


class TestAnswersToQuestions():

    @allure.title('Проверка ответов на вопросы')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, text_answer',
        [
            [MainPageLocators.FIRST_QUESTION_SIGN, MainPageLocators.FIRST_QUESTION_TEXT, '400 рублей'],
            [MainPageLocators.SECOND_QUESTION_SIGN, MainPageLocators.SECOND_QUESTION_TEXT, 'Пока что у нас так:'],
            [MainPageLocators.THIRD_QUESTION_SIGN, MainPageLocators.THIRD_QUESTION_TEXT, 'Допустим, вы оформляете'],
            [MainPageLocators.FOURTH_QUESTION_SIGN, MainPageLocators.FOURTH_QUESTION_TEXT, 'Только начиная'],
            [MainPageLocators.FIFTH_QUESTION_SIGN, MainPageLocators.FIFTH_QUESTION_TEXT, 'Пока что нет'],
            [MainPageLocators.SIXTH_QUESTION_SIGN, MainPageLocators.SIXTH_QUESTION_TEXT, 'Самокат приезжает'],
            [MainPageLocators.SEVENTH_QUESTION_SIGN, MainPageLocators.SEVENTH_QUESTION_TEXT, 'Да, пока самокат'],
            [MainPageLocators.EIGHTH_QUESTION_SIGN, MainPageLocators.EIGHTH_QUESTION_TEXT, 'Да, обязательно']
        ]
    )
    def test_answers_to_question(self, driver, question_locator, answer_locator, text_answer):
        main_page = MainPage(driver)
        main_page.move_to_question()
        main_page.select_question(question_locator)
        main_page.get_answer(answer_locator)
        assert text_answer in main_page.get_answer(answer_locator)
