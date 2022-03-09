import json

from KeywordDriven.api.api import ApiClient


class DataHandle(ApiClient):

    def inquiry_of_id_card_pp(self, params):
        return json.loads(self.inquiry_of_id_card(params))
