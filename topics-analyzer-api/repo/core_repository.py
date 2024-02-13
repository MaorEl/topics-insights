import json

import requests


class CoreRepository:

    __instance = None
    url = 'http://localhost:8080'

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CoreRepository, cls).__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def sign_up(self, user_id, topics):
        URL = self.url + '/signUp'
        params = {'user_id': user_id, 'topics': topics}

        response = self.__send_get_request(URL, params)

        result: str = response.content.decode('UTF-8')
        return result

    def analyze(self, topic):
        URL = self.url + '/analyze'
        params = {'topic': topic}

        response = self.__send_get_request(URL, params)

        result: str = response.content.decode('UTF-8')
        return result

    def visualize(self, topic):
        URL = self.url + '/visualize'
        params = {'topic': topic}

        response = self.__send_get_request(URL, params)

        result: str = response.content.decode('UTF-8')
        return result

    def __send_get_request(self, url, params):
        response = requests.get(url, params=params, timeout=120)
        response.raise_for_status()
        return response