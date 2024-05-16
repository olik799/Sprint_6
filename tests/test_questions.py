from selenium import webdriver
from pages.question_page import QuestionPageScooter
from config import URL
import allure


class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(URL)
        cls.home_page = QuestionPageScooter(cls.driver)

    @allure.title('Проверка ответа на первый вопрос')
    def test_click_first_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_first_question()
        assert "Сутки — 400 рублей" in self.home_page.first_answer()

    @allure.title('Проверка ответа на второй вопрос')
    def test_click_second_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_second_question()
        assert "Пока что у нас так:" in self.home_page.second_answer()

    @allure.title('Проверка ответа на третий вопрос')
    def test_click_third_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_third_question()
        assert "Допустим, вы оформляете" in self.home_page.third_answer()

    @allure.title('Проверка ответа на четвертый вопрос')
    def test_click_fourth_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_fourth_question()
        assert "Только начиная" in self.home_page.fourth_answer()

    @allure.title('Проверка ответа на пятый вопрос')
    def test_click_fifth_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_fifth_question()
        assert "Пока что нет" in self.home_page.fifth_answer()

    @allure.title('Проверка ответа на шестой вопрос')
    def test_click_sixth_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_sixth_question()
        assert "Самокат приезжает к вам" in self.home_page.sixth_answer()

    @allure.title('Проверка ответа на седьмой вопрос')
    def test_click_seventh_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_seventh_question()
        assert "Да, пока самокат" in self.home_page.seventh_answer()

    @allure.title('Проверка ответа на восьмой вопрос')
    def test_click_eighth_question(self, driver):
        self.home_page.scroll_to_question()
        self.home_page.select_eighth_question()
        assert "Да, обязательно" in self.home_page.eighth_answer()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
