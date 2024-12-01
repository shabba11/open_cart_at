import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.elements.LoginPage import User


class RegisterPage(BasePage):
    FIRTSNAME = (By.CSS_SELECTOR, "[name=firstname]")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    SUBMIT = (By.CSS_SELECTOR, "input[type=submit]")
    RADIO = (By.CSS_SELECTOR, "input[type=radio]")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PRIVATE_POLICY = (By.CSS_SELECTOR, "[name=agree]")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[type=submit]")
    SUCCESS_REGISTER = (By.CSS_SELECTOR, "#common-success")

    @allure.step("Регистрация пользователя")
    def register_user(self):
        self._element(self.FIRTSNAME).send_keys(User.FIRST_NAME)
        self._element(self.LAST_NAME).send_keys(User.LAST_NAME)
        self._element(self.EMAIL).send_keys(User.EMAIL)
        self._element(self.TELEPHONE).send_keys(User.PHONE)
        self._element(self.PASSWORD).send_keys(User.PASSWORD)
        self._element(self.CONFIRM_PASSWORD).send_keys(User.PASSWORD)
        self.click(self.PRIVATE_POLICY)
        self.click(self.CONTINUE_BTN)

    @allure.step("Проверка что новый пользователь зарегистрировался")
    def check_register_user(self):
        new_user = self._wait_element(self.SUCCESS_REGISTER)
        assert new_user is not None, 'Новый пользователь не добавлен!'
