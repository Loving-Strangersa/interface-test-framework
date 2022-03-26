# -*- coding: utf-8 -*-
import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.startswith("test") and file.endswith(".py"):
                data_file = file.replace("test", "data")
                data_file = data_file.replace("py", "yaml")
                if data_file not in files:
                    raise ValueError(f"{data_file}未找到对应data文件")


file_name("../KeywordDriven/case")
