import requests


class YaUpLoader:
    def __init__(self, token: str):
        self.token = 'OAuth ' + token
        self.url = 'https://cloud-api.yandex.net/v1/disk/'
        self.headers = {'Accept': 'application/json', 'Authorization': self.token}
        self.json = []

    def create_catalog(self, path: str):
        """Метод создает каталог"""
        url = self.url + 'resources'
        params = {'path': path}
        resp = requests.put(url, params=params, headers=self.headers)
        return resp.status_code