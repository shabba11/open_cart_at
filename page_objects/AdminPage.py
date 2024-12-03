import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.elements.LoginPage import Admin


class Product:
    NAME = 'TestProduct'
    TAG_TITLE = 'TestProductTag'
    MODEL = 'TestModel'
    PRICE = '100'


class AdminPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[name=username]")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type=submit]")
    FORGOTTEN = (By.CSS_SELECTOR, "span > a[href$='route=common/forgotten']")
    LOGO = (By.CSS_SELECTOR, "[title~=OpenCart]")
    CATALOG_BTN = (By.CSS_SELECTOR, 'a[href$="collapse1"]')
    PRODUCTS_BTN = (By.LINK_TEXT, 'Products')
    ADD_NEW_PRODUCT_BTN = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    PRODUCT_MODEL = (By.CSS_SELECTOR, '#input-model')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#input-price')
    SAVE_NEW_PRODUCT_BTN = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    FILTER_BY_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="filter_name"]')
    FILTER_BTN = (By.CSS_SELECTOR, 'button[id="button-filter"]')
    ADDED_PRODUCT = (By.XPATH, "//td[text()='TestModel']")
    CHECK_BOX_PRODUCT = (By.CSS_SELECTOR, 'input[type=checkbox]')
    DELETE_BTN = (By.CSS_SELECTOR, '[data-original-title="Delete"]')
    NO_RESULT = (By.XPATH, '//td[contains(text(),"No results!")]')

    @allure.step("Авторизация")
    def admin_login(self):
        self._element(self.USERNAME).send_keys(Admin.LOGIN)
        self._element(self.PASSWORD).send_keys(Admin.PASSWORD)
        self.click(self.BUTTON_SUBMIT)

    @allure.step("Открытие каталога")
    def open_catalog(self):
        self.click(self.CATALOG_BTN)

    @allure.step("Добавление нового продукта в каталог")
    def add_new_product(self):
        self.click(self.PRODUCTS_BTN)
        self.click(self.ADD_NEW_PRODUCT_BTN)
        self._element(self.PRODUCT_NAME).send_keys(Product.NAME)
        self._element(self.META_TAG_TITLE).send_keys(Product.TAG_TITLE)
        self.click(self.DATA_TAB)
        self._element(self.PRODUCT_MODEL).send_keys(Product.MODEL)
        self._element(self.PRODUCT_PRICE).send_keys(Product.PRICE)
        self.click(self.SAVE_NEW_PRODUCT_BTN)

    @allure.step("Поиск продукта")
    def find_product(self):
        self._element(self.FILTER_BY_NAME_FIELD).send_keys(Product.NAME)
        self.click(self.FILTER_BTN)

    @allure.step("Проверка наличия добавленного продукта")
    def check_added_product(self):
        added_product = self._wait_element(self.ADDED_PRODUCT)
        assert added_product is not None, 'Product not added!'

    @allure.step("Удаление продукта")
    def del_product(self):
        self.click(self.CHECK_BOX_PRODUCT)
        self.click(self.DELETE_BTN)
        self.accept_alert()

    @allure.step("Проверка что продукт удален")
    def check_deleted_product(self):
        assert self._wait_element(self.NO_RESULT).text == 'No results!', 'Product not deleted!'
