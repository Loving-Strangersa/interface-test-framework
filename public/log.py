# -*- coding: utf-8 -*-
import logging
import os

from abs_path import log_path, time_now
from public.handler_yaml import YamlClient


class LogClient(logging.Logger):

    def __init__(self, file=None):
        """
        :param file:是否生成本地文件
        """
        config = YamlClient.read_yaml()["log"]
        super().__init__(config.get('name'), config.get('level'))

        f = '%(asctime)s - %(name)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s:%(message)s'
        formatter = logging.Formatter(f)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.addHandler(console)

        if file:
            console2 = logging.FileHandler(file, encoding='utf8')
            console2.setFormatter(formatter)
            self.addHandler(console2)


if YamlClient.read_yaml()["log"]["file_ok"]:
    file = os.path.join(log_path, time_now + YamlClient.read_yaml()["log"]['file_name'])

Log = LogClient(file)

if __name__ == '__main__':
    print(Log.__dict__.get("handlers"))
