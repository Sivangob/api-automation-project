import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")

    def get_response_time_ms(self, response):
        return response.elapsed.total_seconds() * 1000
