from KeywordDriven.base.base_user import BaseClient
from public.random_data import faker


class MovieApiClientHandle(BaseClient):

    @staticmethod
    def convert_api_get_location_information(params):
        """

        :param params:
        :return:
        """
        headers = {"Realpath": "/movie-2c/staticcache/data/v1/cityList"}
        headers.update(params.get("headers", {}))
        return {
            "headers": headers
        }

    @staticmethod
    def convert_keyword_association(params):
        """

        :param params:
        :return:
        """
        headers = {"Content-Type": "application/json"}
        headers.update(params.get("headers", {}))
        return {
            {"sid": faker.get_time(), "k": "123", "contDisplayType": "1000", "mediaShape": "全片"}
        }

    @staticmethod
    def convert_get_popular_searches(params):
        """
        获取热门搜索数据
        :param params:
        :return:
        """
        headers = {}
        headers.update(params.get("headers", {}))

        return {
            "params": {"appName": "cinema"}
        }
