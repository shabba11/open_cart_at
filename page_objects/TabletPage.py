from selenium.webdriver.common.by import By


class TabletPage:
    GRID = (By.CSS_SELECTOR, "#grid-view")
    LIST = (By.CSS_SELECTOR, "#list-view")
    INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
    INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
    SHOWING_PAGE = (By.XPATH, '//*[@id="content"]/div[3]/div[2]')
