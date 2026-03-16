# -*- coding: utf-8 -*-
from KeywordDriven.ApiHandle.system_management.base import SystemManagementBase


class SystemManagement(SystemManagementBase):

    def _api_system_management_add_roles(self, params):
        """
          新增角色
          :return:
          """
        params = self._convert_api_system_management_add_roles(params)

        self.system_management_add_roles(params)
        result = self._api_system_management_filter_roles({"roleNameForQuery": params["roleName"],
                                                           "isPrePerformance": params["isPrePerformance"],
                                                           "isPreWeekly": params["isPreWeekly"]
                                                           })
        if result["totalCount"] == 1:
            return result["records"][0]
        else:
            return result["records"]

    def _api_system_management_filter_roles(self, params):
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
        params = self._convert_api_system_management_filter_roles(params)
        response = self.system_management_filter_roles(params)
        return response

    def _api_system_management_query_roles(self, params):
        """
        查询角色
        :param params: dict
            roleId:角色id
        :return:
        """
        response = self.system_management_query_roles(params)
        self.compare_response(params, response)

        return response

    def _api_system_management_edit_roles(self, params):
        """
        编辑角色
        :param params: dict
            roleId:角色id
        :return:
        """
        params = self._convert_api_system_management_edit_roles(params)

        self.system_management_edit_roles(params)
        return params

    def _api_system_management_delete_roles(self, params):
        """
        删除角色
        :param params: dict
            roleId:角色id
        :return:
        """
        response = self.system_management_delete_roles(params)
        return response
