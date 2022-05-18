# -*- coding: utf-8 -*-
# @Time    : 2022/05/18
# @Author  : chron
# @FileName: step_user.py 
# @Software: PyCharm 
# @E-mail  : chron@foxmil.com
import allure

from KeywordDriven.ApiHandle.handle_user import UserClient


# TODO:暂时省略获取yaml存取的参数,并返回数据


class StepUser(UserClient):

    @allure.step("用户登录")
    def step_user_login(self, selector):
        result = self.user_login(params=selector)

    @allure.step("用户注册")
    def step_user_register(self, selector):
        result = self.user_register(params=selector)