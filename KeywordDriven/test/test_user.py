import allure

from KeywordDriven.step.step_user import StepUser
# from public.random_data import faker


# TODO 进行step数据串联
class TestUser(StepUser):

    # @allure.title("用户正常登录")
    def test_user_login_succeed(self):
        self.step_user_register(selector="step_user_register")
        self.step_user_login(selector="step_user_login")
