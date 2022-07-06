import allure

from KeywordDriven.ApiHandle.handle_user import UserClient
from KeywordDriven.tdata import fresh_parse_data


class StepUser(UserClient):

    @allure.step("用户注册")
    def step_user_register(self, selector):
        config = fresh_parse_data(selector)
        return self.user_register(config)

    @allure.step("校验用户登录")
    def step_check_user_login(self, selector):
        config = fresh_parse_data(selector)
        self.user_login(config)
