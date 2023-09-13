from KeywordDriven.ApiHandle.handle_user import User


class UserClient(User):

    def user_login(self, params):
        return self._user_login(params)

    def user_register(self, params):
        return self._user_register(params)
