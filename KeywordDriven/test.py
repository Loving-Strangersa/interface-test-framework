from public.handler_yaml import YamlClient


def fresh_parse_data():
    """
    实现自动找寻文件，用例对应方法
    :return:
    :rtype:
    """
    YamlClient.read_yaml("case")


def add_attr(**kwargs):
    """
    初始化用例级别
    :param kwargs:
    :return:
    """
    def wrapper(f):
        if "type" in kwargs:
            type_list = ["P0", "P1", "P2", "P3"]

            case_type = kwargs.get("type")
            if isinstance(case_type, str):
                if case_type not in type_list:
                    raise ValueError(f"用例级别{case_type}不是允许的用例级别{type_list}")

        return f.__name__

    return wrapper
