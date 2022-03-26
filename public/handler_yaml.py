from ruamel import yaml
from abs_path import config_path


class Yaml(object):

    @staticmethod
    def read_yaml(path: str = config_path):
        """
        读取yaml文件数据
        :param path: 文件路径
        :type path: str
        :return: yaml文件数据
        :rtype:
        """
        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f.read(), Loader=yaml.Loader)


YamlClient = Yaml

if __name__ == '__main__':
    print(YamlClient.read_yaml("../config/config.yaml"))
    mysql_data = YamlClient.read_yaml("../config/config.yaml")["mysql"]
    print(mysql_data)
