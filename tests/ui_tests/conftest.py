import pytest
import os
import logging
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="10.0.2.15")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")

    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == 'local':
        if browser_name == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)

        elif browser_name == "chrome":
            service = Service()
            options = ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(options=options)

        elif browser_name == "yandex":
            service = Service(executable_path=os.path.expanduser("~/drivers/yandexbrowserdriver/yandexdriver"))
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options, service=service)

        else:
            raise ValueError(f"Driver {browser_name} not supported.")

    else:
        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
                "screenResolution": "1280x2000",
                "enableVideo": False,
                "enableLog": False,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            },
            "acceptInsecureCerts": True,
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
        )

    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.get(url)
    driver.url = url

    driver.log_level = log_level
    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    return driver
