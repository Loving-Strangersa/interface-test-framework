import re

from tenacity import retry, wait_fixed, stop_after_attempt

from KeywordDriven.api.login.login import LoginApi
from public.encryption import encryption
from public.exception import SpecificLoginError
from public.image_processing import get_code


class LoginApiClient(LoginApi):

    @retry(wait=wait_fixed(5), stop=stop_after_attempt(5))
    def _select_user_login(self, params):
        """
        用户登录
        :param params:dict
                        username:用户名
                        password:密码
        :return:
        """
        key = self.login_public_key()["publicKey"]
        self.login_captcha_code()
        result = get_code(self.domain + "/manage-server/common/login-captcha-code", "$.captchaCode")
        request_d = {
            "username": encryption(key, params['username']),
            "password": encryption(key, params['password']),
            "captchaId": encryption(key, result["captchaId"]),
            "captchaCode": encryption(key, result["code"]),
        }
        s = self.login_send_code(request_d)["msg"]
        if s == "用户名或验证码不正确.":
            print("触发重试机制，最多重试5次")
            raise SpecificLoginError("触发重试机制，最多重试5次")

        request_d["phoneCode"] = encryption(key, self.__get_code())
        s = self.login_certification(request_d)["token"]
        self.session.headers.update(self.headers(s))

    def __get_code(self):
        """
        获取验证码
        :return:
        """
        domain = self.domain

        domain_map = {
            "dev": "http://sales.wxdev.com:2086",
            "test": "http://36.155.98.104:49680/"
        }
        if domain == domain_map["dev"]:
            return "888888"
        elif domain == domain_map["test"]:
            re_s = self.get(self.code_address).text
            pattern = '(?<=【销售管理系统】验证码).*?(?=，2分钟内有效)'
            return re.findall(pattern, re_s)[-1]
