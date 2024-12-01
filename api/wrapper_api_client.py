import requests
import allure


class APIClientWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    @allure.step("Отправка post-запроса")
    def action(base_url, endpoint, params=None, data=None):
        """Функция отправки post-запроса

        Args:
            base_url: Базовый URL для отправки запросов
            endpoint: Конечная точка
            params: Параметры запроса
            data: Данные запроса

        """
        url = base_url + endpoint
        response = requests.post(url=url, params=params, data=data)
        return response
