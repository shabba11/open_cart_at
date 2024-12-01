from random import randint


class Admin:
    LOGIN = 'user'
    PASSWORD = 'bitnami'


class User:
    FIRST_NAME = 'Ivan'
    LAST_NAME = 'Ivanov'
    EMAIL = f'test_{randint(0, 1000000)}@mail.com'
    PHONE = '+79111234565'
    LOGIN = 'USER'
    PASSWORD = 'USER_123'
