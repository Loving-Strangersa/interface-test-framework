from KeywordDriven.base.base_user import BaseClient


class ApiClient(BaseClient):

    def login(self, params):
        api_url = "/api/login"
        response = self.post(url=self.host + api_url, json=params)
        return response.json()

    def register(self, params):
        api_url = "/api/register"
        response = self.post(url=self.host + api_url, json=params)
        return response.json()
