import json as system_json

import allure
import requests
from public.random_data import counterfeit
from public.handler_yaml import YamlClient


class Request(object):

    def __init__(self):
        requests.packages.urllib3.disable_warnings()

        self.user_agent = counterfeit.random_user_agent()
        self.base_url = YamlClient.read_yaml()["config"]["domain"]

    @staticmethod
    def allure_data(**kwargs):
        """
        写入数据到allure报告
        :param kwargs: 要写入的数据
        :type kwargs:
        :return:
        :rtype:
        """
        allure.attach(str(kwargs), "所有参数", allure.attachment_type.TEXT)
        allure.attach(str(kwargs["url"]), "请求地址", allure.attachment_type.TEXT)
        allure.attach(str(kwargs["headers"]), "请求头", allure.attachment_type.TEXT)
        allure.attach(str(kwargs["method"]), "请求方法", allure.attachment_type.TEXT)
        allure.attach(str(kwargs.get("data")), "data请求参数", allure.attachment_type.TEXT)
        allure.attach(str(kwargs.get("json")), "json请求参数", allure.attachment_type.TEXT)
        allure.attach(str(kwargs["status_code"]), "反回状态码", allure.attachment_type.TEXT)
        allure.attach(kwargs["response"], "响应结果", allure.attachment_type.TEXT)

    def __header(self, token=None):
        """
        处理请求头,支持传入token
        :param token: 处理token
        :type token: str
        :return: 返回请求头
        :rtype: dict
        """
        header = {'User-Agent': self.user_agent}
        if token:
            header["token"] = token
        return header

    def __url(self, url: str):
        """
        处理请求地址
        :param url:
        :type url:
        :return:
        :rtype:
        """
        if not url.startswith("/"):
            return self.base_url + "/" + url

        return self.base_url + url

    @staticmethod
    def __proxies():
        """
        读取配置进行代理
        :return: 返回http和https代理配置
        :rtype: dict
        """
        config = YamlClient.read_yaml()
        if config["config"]["proxies"]:
            return config["proxies"]
        return False

    @staticmethod
    def __get_json_data(data=None):
        """
        判断data请求参数是否可以转换成dict类型
        :param data:
        :type data: str or dict
        :return:
        :rtype:
        """
        if data is not None:
            try:
                if data is not None and isinstance(data, str):
                    return system_json.loads(data)
            except TypeError:
                return data
            else:
                return data

    @staticmethod
    def __get_json(json=None):
        """
        判断json请求参数是否可以转换成dict类型
        :param json:
        :type json:
        :return:
        :rtype:
        """
        try:
            if json is not None and isinstance(json, str):
                return system_json.loads(json)
        except TypeError:
            return json
        else:
            return json

    def send_request(self, method: str, url: str, token: str = None, data=None, json=None, verify: bool = False,
                     **kwargs):
        """
        发送接口方法
        :param method: 请求方法
        :type method: str
        :param url: 请求地址
        :type url: str
        :param token: 鉴权
        :type token: str or None
        :param verify: 是否开启ssl证书
        :type verify: bool
        :param kwargs:
        :type kwargs:
        :return: 接口返回值
        :rtype: str or dict
        """
        headers = self.__header(token)
        url = self.__url(url)
        proxies = self.__proxies()
        data = self.__get_json_data(data)
        json = self.__get_json(json)

        response = requests.request(method, url, data=data, json=json, headers=headers, verify=verify, proxies=proxies,
                                    **kwargs)

        self.allure_data(url=url, headers=headers, method=method, data=data, json=json,
                         status_code=response.status_code, response=response.text, **kwargs)
        try:
            return system_json.loads(response.text)
        except TypeError:
            return response.text
