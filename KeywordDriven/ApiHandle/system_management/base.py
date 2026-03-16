# -*- coding: utf-8 -*-
from KeywordDriven.api.system_management.system_management import SystemManagementApi


class SystemManagementBase(SystemManagementApi):

    @staticmethod
    def _convert_api_system_management_add_roles(params):
        """

        :param params: dict
            roleName:角色名称
            isPreWeekly:是否预生成周报
            isPrePerformance:是否预生成绩效
            description:描述
        :return:
        """
        return {"roleName": params["roleName"], "isPreWeekly": params["isPreWeekly"],
                "isPrePerformance": params["isPrePerformance"],
                "description": params.get("description")}

    @staticmethod
    def _convert_api_system_management_filter_roles(params):
        """
        筛选角色列表
        :param params: dict
            pageSize:显示页面数据条数
            currentPage:页面
            isPrePerformance:bool 是否预生成绩效
            isPreWeekly:bool 是否预生成周报
            roleNameForQuery:角色名称，支持模糊搜索
        :return:
        """
        s = {"pageSize": 10, "currentPage": 1}
        s.update(params)
        return s

    @staticmethod
    def _convert_api_system_management_edit_roles(params):
        """
        删除角色
        :param params: dict
            roleId:角色id
        :return:
        """
        return {"id": params["id"], "roleName": params["roleName"], "isPreWeekly": params["isPreWeekly"],
                "isPrePerformance": params["isPrePerformance"],
                "description": params["description"]}
