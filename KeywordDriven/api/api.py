from KeywordDriven.base.base import BaseClient


class ApiClient(BaseClient):

    def inquiry_of_id_card(self, params):
        api_url = "/UserAction"
        response = self.post(url=self.host + api_url, data=params)
        return response.text
