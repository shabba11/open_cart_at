import pytest
from page_objects.MainPage import MainPage
from page_objects.TabletPage import TabletPage
from page_objects.ProductPage import ProductPage
from page_objects.AdminPage import AdminPage
from page_objects.RegisterPage import RegisterPage


def test_main_page(browser):
    """Проверка элементов на главной странице"""
    browser.get(browser.url)
    browser.find_element(*MainPage.CART)
    browser.find_element(*MainPage.LOGO)
    browser.find_element(*MainPage.SEARCH_INPUT)
    browser.find_element(*MainPage.LAPTOP)
    browser.find_element(*MainPage.BUTTON_ADD_TO_CART)


def test_tablet_page(browser):
    """Проверка элементов на странице tablet"""
    browser.get(browser.url + "/tablet")
    browser.find_element(*TabletPage.GRID)
    browser.find_element(*TabletPage.LIST)
    browser.find_element(*TabletPage.INPUT_LIMIT)
    browser.find_element(*TabletPage.INPUT_SORT)
    browser.find_element(*TabletPage.SHOWING_PAGE)


def test_product_card_page(browser):
    """Проверка элементов на странице продукта"""
    browser.get(browser.url + "/tablet/samsung-galaxy-tab-10-1")
    browser.find_element(*ProductPage.BUTTON_CART)
    browser.find_element(*ProductPage.TAB_DESCRIPTION)
    browser.find_element(*ProductPage.TAB_REVIEW)
    browser.find_element(*ProductPage.QUANTITY)
    browser.find_element(*ProductPage.COMPARE)


def test_admin_page(browser):
    """Проверка элементов на странице admin"""
    browser.get(browser.url + "/admin")
    browser.find_element(*AdminPage.USERNAME)
    browser.find_element(*AdminPage.PASSWORD)
    browser.find_element(*AdminPage.BUTTON_SUBMIT)
    browser.find_element(*AdminPage.FORGOTTEN)
    browser.find_element(*AdminPage.LOGO)


def test_register_page(browser):
    """Проверка элементов на странице register"""
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*RegisterPage.FIRTSNAME)
    browser.find_element(*RegisterPage.PASSWORD)
    browser.find_element(*RegisterPage.CHECKBOX)
    browser.find_element(*RegisterPage.SUBMIT)
    browser.find_element(*RegisterPage.RADIO)


@pytest.mark.parametrize('currency', ('EUR', 'GBP', 'USD'))
def test_switch_currency(browser, currency):
    """Проверка переключения валют"""
    browser.get(browser.url)
    MainPage(browser).switch_currency(currency)


def test_add_new_product(browser):
    """Проверка добавления нового продукта"""
    browser.get(browser.url + "/admin")
    admin_page = AdminPage(browser)
    admin_page.admin_login()
    admin_page.open_catalog()
    admin_page.add_new_product()
    admin_page.find_product()
    admin_page.check_added_product()


def test_del_product(browser):
    """Проверка удаления продукта"""
    browser.get(browser.url + "/admin")
    admin_page = AdminPage(browser)
    admin_page.admin_login()
    admin_page.open_catalog()
    admin_page.add_new_product()
    admin_page.find_product()
    admin_page.del_product()
    admin_page.check_deleted_product()


def test_register_user(browser):
    """Проверка регистриции пользователя"""
    browser.get(browser.url + "/index.php?route=account/register")
    register_page = RegisterPage(browser)
    register_page.register_user()
    register_page.check_register_user()
