from KeywordDriven.ApiHandle.login.login import LoginApiClient


class Login(LoginApiClient):

    def select_user_login(self, params):
        return self._select_user_login(params)
