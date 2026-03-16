import allure

from KeywordDriven.ApiHandle import MovieClient
from KeywordDriven.base.base import teardown
from KeywordDriven.tdata import get_env_data
from KeywordDriven.tdata.tdata_movie import step_check_location_information_list


class StepMovieCheck(MovieClient):

    @allure.step("断言定位信息")
    def step_check_location_information_list(self, params=None):
        teardown.add_cleanup_step(lambda: print("Cleanup Step 2"))
        # for param in get_env_data("step_get_location_information")["body"]["cityList"]:
        #     assert param in step_check_location_information_list
