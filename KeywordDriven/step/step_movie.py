import allure

from KeywordDriven.ApiHandle import MovieClient
from KeywordDriven.tdata import fresh_parse_data


class StepMovie(MovieClient):

    @fresh_parse_data
    @allure.step("查看定位信息")
    def step_get_location_information(self, params=None):
        return self.get_location_information(params)

    @fresh_parse_data
    @allure.step("获取热门搜索")
    def step_get_popular_searches(self, params={}):
        return self.get_popular_searches(params)

    @fresh_parse_data
    @allure.step("搜索关键词联想")
    def step_keyword_association(self, params=None):
        return self.get_location_information(params)
