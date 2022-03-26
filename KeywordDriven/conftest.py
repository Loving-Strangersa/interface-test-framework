import os

import pytest

import requests

from public.get_file_name import file_name


@pytest.fixture(scope="function", autouse=True)
def init():
    """
    初始化requests 忽略ssl证书未验证错误
    校验对应test用例的data yaml文件
    :return:
    """
    requests.packages.urllib3.disable_warnings()
    file_name("./KeywordDriven/case")

def pytest_collection_modifyitems(items):
    current_path = os.path.abspath(".")
    for item in items:
        case_path = os.path.join(current_path, item.nodeid.split("::")[0])
        case_file = os.path.basename(case_path)
        tdata_temp = case_file.replace("test", "tdata")
        tdata_path = os.path.join(current_path, tdata_temp.replace(".py", ".yaml"))

        if os.path.isfile(tdata_path):
            pass
        else:
            raise ValueError(f"{case_file}文件没有找到对应的tdata数据文件")
