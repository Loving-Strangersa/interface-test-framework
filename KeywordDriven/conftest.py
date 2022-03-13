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
