import os

import pytest
import requests
from _pytest.mark import Mark

from KeywordDriven.tdata import clear_env


@pytest.fixture(scope="function", autouse=True)
def init():
    """
    初始化requests 忽略ssl证书未验证错误
    :return:
    """
    requests.packages.urllib3.disable_warnings()
    yield
    print("这是前置的方法，可以实现部分以及全部用例的前后置")
    clear_env()
    print("这是后置的方法，可以实现部分以及全部用例的前后置")


def function_marks(func):
    return [ob.name for name, obj in vars(func).items() for ob in obj if isinstance(ob, Mark)]


@pytest.fixture(scope="function", autouse=True)
def marker(request):
    """
    动态设置@pytest.mark.xxxx
    :param request:
    :return:
    """
    [request.node.add_marker(i) for i in function_marks(request.function)]


def pytest_collection_modifyitems(items):
    """
    获取文件的tdata路径
    :param items:
    :return:
    """
    current_path = os.path.abspath(".")
    for item in items:
        case_path = os.path.join(current_path, item.nodeid.split("::")[0])
        case_file = os.path.basename(case_path)
        tdata_temp = case_file.replace("test", "tdata")
        dir_path = os.path.dirname(case_path)
        tdata_path = os.path.join(dir_path, tdata_temp.replace("test", "tdata"))
        if not os.path.exists(tdata_path):
            raise ValueError(f"{case_file}文件没有找到对应的tdata数据文件")

# @pytest.fixture(autouse=True)
# def del_env():
#     print("这是前置的方法，可以实现部分以及全部用例的前后置")
#     yield
#     clear_env
#     print("这是后置的方法，可以实现部分以及全部用例的前后置")
