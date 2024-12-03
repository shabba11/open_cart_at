import requests
import json
import os
import allure

from api.endpoints import Endpoints


class BaseAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api_token = None

    @allure.step("Получение токена")
    def get_token(self):
        """Метод получения токена"""
        token_url = f'{self.base_url}' + Endpoints.LOGIN

        api_credentials = self.get_api_credentials()

        if api_credentials is None:
            return None

        data = {
            'username': api_credentials['api_username'],
            'key': api_credentials['api_key']
        }

        try:
            response = requests.post(token_url, data=data)
            response.raise_for_status()
            token_data = response.json()
            if 'error' in token_data:
                print(token_data['error'])
            self.api_token = token_data.get('api_token')
            return self.api_token

        except requests.exceptions.RequestException as e:
            print(f'Ошибка при получении токена: {e}')
            return None

    @staticmethod
    @allure.step("Получение данных для входа")
    def get_api_credentials():
        """Метод получения данных для входа из файла"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        config_path = os.path.join(project_dir, 'config.json')

        try:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            return config
        except FileNotFoundError:
            print('Файл конфигурации config.json не найден.')
            return None
        except json.JSONDecodeError:
            print('Ошибка при чтении файла конфигурации config.json. Проверьте его формат.')
            return None
