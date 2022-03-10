from public.handler_yaml import YamlClient


def fresh_parse_data():
    """
    实现自动找寻文件，用例对应方法
    :return:
    :rtype:
    """
    YamlClient.read_yaml("./test")
