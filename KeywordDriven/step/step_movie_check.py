import allure

from KeywordDriven.ApiHandle import MovieClient
from KeywordDriven.tdata import get_env_data
from KeywordDriven.tdata.tdata_movie import step_check_location_information_list


class StepMovieCheck(MovieClient):

    @allure.step("断言定位信息")
    def step_check_location_information_list(self, params=None):
        for param in get_env_data("step_get_location_information")["body"]["cityList"]:
            assert param in step_check_location_information_list
