from ruamel import yaml


class Yaml(object):

    @staticmethod
    def read_yaml(path: str):
        """
        读取yaml文件数据
        :param path: 文件路径
        :type path: str
        :return: yaml文件数据
        :rtype:
        """
        with open(path, "r") as f:
            return yaml.load(f.read(), Loader=yaml.Loader)


handle_yaml = Yaml

if __name__ == '__main__':
    print(handle_yaml.read_yaml("../config/config.yaml"))