import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    CART = (By.CSS_SELECTOR, "#cart")
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[name=search]")
    LAPTOP = (By.CSS_SELECTOR, "[title~=MacBook]")
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
    BUTTON_CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    BUTTON_EURO = (By.CSS_SELECTOR, "[name=EUR]")
    BUTTON_STERLING = (By.CSS_SELECTOR, "[name=GBP]")
    BUTTON_DOLLAR = (By.CSS_SELECTOR, "[name=USD]")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    CURRENCY_VALUE = (By.CSS_SELECTOR, "#form-currency strong")

    @allure.step("Переключение валюты")
    def switch_currency(self, name):
        self.click(self.BUTTON_CURRENCY)
        if name == "EUR":
            self.click(self.BUTTON_EURO)
        elif name == "GBP":
            self.click(self.BUTTON_STERLING)
        elif name == "USD":
            self.click(self.BUTTON_DOLLAR)
        else:
            raise AssertionError(f"Валюта {name} отсутствует")
