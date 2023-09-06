import os

import pytest
import requests


@pytest.fixture(scope="function", autouse=True)
def init():
    """
    初始化requests 忽略ssl证书未验证错误
    :return:
    """
    requests.packages.urllib3.disable_warnings()


def pytest_collection_modifyitems(items):
    current_path = os.path.abspath(".")
    for item in items:
        case_path = os.path.join(current_path, item.nodeid.split("::")[0])
        case_file = os.path.basename(case_path)
        tdata_temp = case_file.replace("test", "tdata")
        dir_path = os.path.dirname(case_path)
        tdata_path = os.path.join(dir_path, tdata_temp.replace("test", "tdata"))
        if not os.path.exists(tdata_path):
            raise ValueError(f"{case_file}文件没有找到对应的tdata数据文件")
