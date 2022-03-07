from request import Request


class Requests(Request):

    def send_requests(self, *args, **kwargs):

        return self.send_request(*args, **kwargs)


if __name__ == '__main__':
    data = {
        "username": "18574783294",
        "password": "nightfell.",
        "sessitime": "2022-03-07 15:50:50",
        "sessiond": "saas",
        "method": "login"
    }
    print(Requests().send_requests(method="post", url="UserAction", data=data))
