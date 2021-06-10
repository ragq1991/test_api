import main as m
import requests


class TestApi:

    def test_createcatalog(self):
        ya = m.YaUpLoader('token')
        ya.create_catalog('test_catalog')
        params = {'path': 'test_catalog'}
        rest = requests.get(ya.url + 'resources', params=params, headers=ya.headers).status_code
        if rest == 200:
            print('200 каталог успешно создан.')
        elif rest == 400:
            print('400 Некорректные данные.')
        elif rest == 401:
            print('401 Не прошла авторизация.')
        elif rest == 404:
            print('404 Каталог не найден.')