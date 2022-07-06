from KeywordDriven.ApiHandle.base import Client as UserClient
from KeywordDriven.api.api import ApiClient


class UserClient(ApiClient, UserClient):

    def user_login(self, params):
        """
        用户登录
        :param params:
             -[x] username: 登录用户名
             -[x] pwd: 登录密码
        :return:
        """
        result = self._convert_user_login(params)
        response = self.login(result)
        assert response["message"] == "恭喜你登录成功"

    def user_register(self, params):
        """
        用户注册
        :param params:
             -[x] username: 登录用户名
             -[x] pwd: 登录密码
             -[x] nickname: 昵称
             -[] description:描述
        :return:
        """
        result = self._convert_user_register(params)
        response = self.register(result)
        assert response["message"] == "恭喜你注册成功"
        response.update(result)
        return response
