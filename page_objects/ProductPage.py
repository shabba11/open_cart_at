from selenium.webdriver.common.by import By


class ProductPage:
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    TAB_DESCRIPTION = (By.CSS_SELECTOR, "a[href^='#tab-description']")
    TAB_REVIEW = (By.CSS_SELECTOR, "a[href^='#tab-review']")
    QUANTITY = (By.CSS_SELECTOR, "[name=quantity]")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title~=Compare]")
