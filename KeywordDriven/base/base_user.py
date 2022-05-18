from requests import Session

from abs_path import config_path
from public.handler_yaml import YamlClient
from public.log import Log


class BaseClient(object):
    host = YamlClient().read_yaml(config_path)["config"]["domain"]
    Session = Session()

    def post(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次post请求信息为:{url},{data},{json},{kwargs}")
        return self.Session.post(url, verify=False, data=data, json=json, **kwargs)
