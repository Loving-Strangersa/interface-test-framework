import copy
from KeywordDriven.api import Data


def fresh_parse_data(selector=None):
    """
    :param selector:传入字符串 以空格隔开 表示一个字典的key
    :type selector:str
    :return:tdata要单位的数据
    :rtype:
    """
    print(selector)


if __name__ == '__main__':
    setattr(Data, "case_data", {"a": {"b": 1}})
    print(fresh_parse_data("a b"))
