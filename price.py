import requests
import json


class Price:
    def __call__(self, currency_name):
        self.url = "https://api.bithumb.com/public/ticker/ALL_KRW"
        self.headers = {"accept": "application/json"}
        self.currency_name = currency_name
        response = json.loads(requests.get(self.url, headers=self.headers).text)
        return response["data"][self.currency_name]
