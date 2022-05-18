# -*- coding: utf-8 -*-
# @Time    : 2022/05/18
# @Author  : chron
# @FileName: test_user.py 
# @Software: PyCharm 
# @E-mail  : chron@foxmil.com
import allure

from KeywordDriven.step.step_user import StepUser
from public.random_data import faker


# TODO 进行step数据串联
class TestUser(StepUser):

    @allure.title("用户正常登录")
    def test_user_login_succeed(self):
        self.step_user_register({"username": faker.random_password,
                                 "pwd": faker.random_password,
                                 "nickname": faker.random_password,
                                 })
        self.step_user_login({"username": "chron1", "pwd": "1231987"})
