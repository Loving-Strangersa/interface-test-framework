import pytest
import requests

from KeywordDriven.ApiHandle.login import Login
from KeywordDriven.base.base import teardown_fun
from KeywordDriven.tdata import clear_env
from abs_path import config_path
from public.handler_yaml import YamlClient


@pytest.fixture(scope="function", autouse=True)
def init_function():
    """
    初始化requests 忽略ssl证书未验证错误
    :return:
    """
    print(123)
    requests.packages.urllib3.disable_warnings()

    yield
    clear_env()
    teardown_fun.execute_cleanup_steps()


@pytest.fixture(scope="function", autouse=True)
def init_login():
    """
    初始化
    :return:
    """
    Login().select_user_login(YamlClient().read_yaml(config_path)["config"]["Super_administrator"])
