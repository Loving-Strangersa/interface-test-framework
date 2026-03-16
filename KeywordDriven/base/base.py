from requests import Session

from abs_path import config_path
from public.handler_yaml import YamlClient
from public.log import Log


class Teardown:
    cleanup_steps = []

    def add_cleanup_step(self, func):
        self.cleanup_steps.append(func)

    def execute_cleanup_steps(self):
        for func in reversed(self.cleanup_steps):
            print(f"Attempting to call {func} of type {type(func)}")
            if callable(func):
                func()
            else:
                print(f"Warning: Skipping non-callable item {func} in cleanup_steps")


teardown_fun = Teardown()


class BaseClient(object):
    session = Session()

    @property
    def code_address(self):
        return YamlClient().read_yaml(config_path)["config"]["code_address"]

    @property
    def domain(self):
        return YamlClient().read_yaml(config_path)["config"]["domain"]

    @staticmethod
    def headers(token=None):
        return {
            "Authorization": token
        }

    def post(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次post请求信息为url： {url},data： {data}, json：{json},kwargs： {kwargs}")
        return self.session.post(url, verify=False, data=data, json=json, **kwargs)

    def get(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次get请求信息为url： {url},data： {data}, json：{json},kwargs： {kwargs}")
        return self.session.get(url, verify=False, data=data, json=json, **kwargs)

    def put(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次put请求信息为url： {url},data： {data}, json：{json},kwargs： {kwargs}")
        return self.session.put(url, verify=False, data=data, json=json, **kwargs)

    def delete(self, url, data=None, json=None, **kwargs):
        Log.info(f"本次delete请求信息为url： {url},data： {data}, json：{json},kwargs： {kwargs}")
        return self.session.delete(url, verify=False, data=data, json=json, **kwargs)

    def compare_response(self, expected, actual):
        """
        递归地比较预期的响应和实际的HTTP响应体是否一致。

        :param expected: 预期的响应体，可以是字典或列表。
        :param actual: 实际的HTTP响应体，也应该是字典或列表。
        :return: 布尔值，表示两者是否一致。
        """
        # 确保两者类型相同
        if type(expected) != type(actual):
            raise ValueError("类型不一致")

            # 如果两者都是字典，则进行字典的递归比较
        if isinstance(expected, dict):
            # 检查expected中的每个键是否在actual中，并且值相等
            for key, value in expected.items():
                if key not in actual:
                    raise ValueError(f"值不相等{key}：{actual}")

                if not self.compare_response(value, actual[key]):
                    raise ValueError(f"值不相等{value}：{actual[key]}")

                    # 注意：这里没有检查actual中是否有extra的键，如果需要检查，可以添加额外的逻辑
            return True

            # 如果两者都是列表，则进行列表的递归比较
        elif isinstance(expected, list):
            # 检查列表长度是否相等
            if len(expected) != len(actual):
                raise ValueError(f"列表长度不相等")
                # 递归地比较每个元素
            for exp, act in zip(expected, actual):
                if not self.compare_response(exp, act):
                    return False
            return True

            # 如果两者都不是字典或列表，则直接比较它们的值
        else:
            # 注意：对于复杂的对象（如自定义类实例），可能需要更复杂的比较逻辑
            # 这里只考虑基本数据类型（如str, int, bool, None等）
            return expected == actual
