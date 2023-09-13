import allure
import pytest

from KeywordDriven.step.step_user import StepUser
from KeywordDriven.tdata import e
from public.random_data import faker


# TODO 待进行step数据串联
class TestUser(StepUser):
    # @pytest.mark.hsf
    @allure.title("用户正常登录")
    def test_user_login_succeed(self):
        self.step_user_register({"username": faker.random_password,
                                 "pwd": faker.random_password,
                                 "nickname": faker.random_password,
                                 })
        self.step_check_user_login({"!username": "step_user_register username", "!pwd": "step_user_register pwd"})

    @pytest.mark.hsf
    @allure.title("用户正常登录")
    def test_user_login_2222(self):
        assert 1 == 1
