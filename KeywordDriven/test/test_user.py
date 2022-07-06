import allure

from KeywordDriven.step.step_user import StepUser

from public.random_data import faker


class TestUser(StepUser):

    @allure.title("用户正常登录")
    def test_user_login_succeed(self):
        step_user_register = self.step_user_register(selector={"username": faker.random_name,
                                                               "pwd": faker.random_password,
                                                               "nickname": faker.random_username,
                                                               })
        self.step_check_user_login(selector={
            "username": step_user_register["username"],
            "pwd": step_user_register["pwd"]
        })
