import copy
from KeywordDriven.api import Data


def fresh_parse_data(selector=None):
    """
    :param selector:用例step
    :type selector:str
    :return:
    """
    return selector


if __name__ == '__main__':
    setattr(Data, "case_data", {"a": {"b": 1}})
    print(fresh_parse_data("a b"))
