from KeywordDriven.api.movie_api import MovieApiClient


class Movie(MovieApiClient):

    @staticmethod
    def _convert(response):
        assert response["code"] == 200

    def _get_location_information(self, params=None):
        """
        获取定位信息
        :param params:
        :return:
        """
        params = self.convert_api_get_location_information(params)
        response = self.api_get_location_information(params)
        self._convert(response)
        return response

    def _get_popular_searches(self, params=None):
        """
        获取热门搜索数据
        :param params:
        :return:
        """
        params = self.convert_get_popular_searches(params)
        response = self.api_get_popular_searches(params)
        self._convert(response)
        return response

    def _keyword_association(self, params=None):
        """
        搜索关键词联想
        :param params:
        :return:
        """
        params = self.convert_keyword_association(params)
        response = self.api_keyword_association(params)
        self._convert(response)
        return response
