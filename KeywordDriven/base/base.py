from requests import Session
from abs_path import config_path
from public.handler_yaml import YamlClient


class BaseClient(object):
    host = YamlClient().read_yaml(config_path)["config"]["domain"]
    Session = Session()

    def post(self, url, data=None, json=None, **kwargs):
        return self.Session.post(url, verify=False, data=data, json=json, **kwargs)
