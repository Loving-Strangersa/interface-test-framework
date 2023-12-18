from requests import Session

from abs_path import config_path
from public.handler_yaml import YamlClient
from public.log import Log


class BaseClient(object):
    host = YamlClient().read_yaml(config_path)["config"]["domain"]
    session = Session()

    @staticmethod
    def headers():
        return {
            "sign": "2ADAAD787F4226F91536E6F272E2FAF2",
            "userInfo": "%7B%22userId%22%3A%221205818233%22%2C%22userNum%22%3A%228618574783294%22%2C%22mobile%22%3A%2218574783294%22%2C%22areaId%22%3A%22731%22%2C%22cityId%22%3A%220731%22%2C%22carrierCode%22%3A%22CU%22%2C%22passId%22%3A%2293294915815479%22%2C%22userToken%22%3A%22nlps5C05412A9676789E9FA1%22%2C%22expiredOn%22%3A%221707811049000%22%2C%22encrypted%22%3Afalse%2C%22sign%22%3A%222ADAAD787F4226F91536E6F272E2FAF2%22%7D",
            "userToken": "nlps5C05412A9676789E9FA1"
        }

    def post(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次post请求信息为: {url}, {data}, {json}, {kwargs}")
        headers = kwargs.get('headers', {})
        headers.update(self.headers())
        kwargs['headers'] = headers
        return self.session.post(url, verify=False, data=data, json=json, **kwargs)

    def get(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次get请求信息为: {url}, {data}, {json}, {kwargs}")
        headers = kwargs.get('headers', {})
        headers.update(self.headers())
        kwargs['headers'] = headers
        return self.session.get(url, verify=False, data=data, json=json, **kwargs)
