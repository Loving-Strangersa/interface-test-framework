from KeywordDriven.base.base import BaseClient


class LoginApi(BaseClient):

    def login_public_key(self):
        """
        获取系统加密key
        :return:
        """
        url = "/manage-server/common/login/rsa-public-key"
        response = self.get(url=self.domain + url)
        return response.json()

    def login_captcha_code(self):
        """
        获取图片验证码
        :return:
        """
        url = "/manage-server/common/login-captcha-code"
        response = self.get(url=self.domain + url)
        return response.json()

    def login_send_code(self, params=None):
        """
        获取短信验证码
        :param params:dict
                        captchaCode:图片验证码
                        captchaId:图片验证码id
                        password:密码
                        username:用户名
        :return:
        """
        url = "/manage-server/common/sendCode"
        response = self.post(url=self.domain + url, json=params)
        return response.json()

    def login_certification(self, params=None):
        """
        登录
        :param params:dict
                        phoneCode:手机验证码
                        captchaCode:图片验证码
                        captchaId:图片验证码id
                        password:密码
                        username:用户名
        :return:
        """
        url = "/manage-server/miguoa/certification/login"
        response = self.post(url=self.domain + url, data=params)
        return response.json()
