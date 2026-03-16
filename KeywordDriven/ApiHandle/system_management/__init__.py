# -*- coding: utf-8 -*-
from KeywordDriven.ApiHandle.system_management.system_management import SystemManagement
from KeywordDriven.tdata import fresh_parse_data


class SystemManagementApiClient(SystemManagement):

    @fresh_parse_data
    def api_system_management_add_roles(self, params):
        """
        新增角色
        :param params:
        :return:
        """
        return self._api_system_management_add_roles(params)

    def api_system_management_filter_roles(self, params):
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
        return self._api_system_management_filter_roles(params)

    @fresh_parse_data
    def api_system_management_query_roles(self, params):
        """
        查询角色
        :param params: dict
            roleId:角色id
        :return:
        """
        return self._api_system_management_query_roles(params)

    @fresh_parse_data
    def api_system_management_edit_roles(self, params):
        """
        修改角色
        :param params: dict
            id:角色id
            roleName:角色名称
            isPreWeekly:是否预生成周报
            isPrePerformance:是否预生成绩效
            description:描述
        :return:
        """
        return self._api_system_management_edit_roles(params)

    def api_system_management_delete_roles(self, params):
        """
        删除角色
        :param params: dict
            id:角色id
        :return:
        """
        return self._api_system_management_delete_roles(params)
