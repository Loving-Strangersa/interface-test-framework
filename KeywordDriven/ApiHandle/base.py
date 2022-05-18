# -*- coding: utf-8 -*-
# @Time    : 2022/05/18
# @Author  : chron
# @FileName: base_user.py
# @Software: PyCharm 
# @E-mail  : chron@foxmil.com

class Client:

    @staticmethod
    def _convert_user_login(params):
        data = {
            "username": params.get("username"),
            "pwd": params.get("pwd")
        }
        return data

    @staticmethod
    def _convert_user_register(params):
        data = {
            "username": params.get("username"),
            "pwd": params.get("pwd"),
            "nickname": params.get("nickname"),
            "description": params.get("description", "default description")
        }
        return data
