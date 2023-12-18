from KeywordDriven.ApiHandle.base import MovieApiClientHandle


class MovieApiClient(MovieApiClientHandle):
    jb = "https://jadeite.migu.cn"

    def api_get_location_information(self, params=None):
        """
        获取定位信息
        :param params: None
        :return:
        """
        url = "/mesh/v2/staticcache/mesh-info"
        response = self.post(url=self.host + url, **params)
        return response.json()

    def api_keyword_association(self, params=None):
        """
        获取定位信息
        :param params: None
        :return:
        """
        url = "/search4mv/v1/search/suggest"
        response = self.get(url=self.host + url, **params)
        return response.json()

    def api_get_popular_searches(self, params=None):
        """
        获取热门搜索数据
        :param params:
        :return:
        """
        url = "/search/hotword"
        response = self.get(url=self.jb + url, **params)
        return response.json()
