import allure

from KeywordDriven.ApiHandle import UserClient
from KeywordDriven.tdata import fresh_parse_data


class StepUser(UserClient):

    @fresh_parse_data
    @allure.step("用户注册")
    def step_user_register(self, selector):
        # config = fresh_parse_data(selector)
        return self.user_register(selector)

    @fresh_parse_data
    @allure.step("校验用户登录")
    def step_check_user_login(self, selector):
        self.user_login(selector)

