# -*- coding: utf-8 -*-
import allure

from KeywordDriven.ApiHandle.system_management import SystemManagementApiClient
from KeywordDriven.base.base import teardown_fun
from KeywordDriven.tdata import fresh_parse_data, get_env_data


class StepSystemManagementApiClient(SystemManagementApiClient):

    @allure.step("新增角色")
    def step_api_system_management_add_roles(self, params, teardown=False):
        self.api_system_management_add_roles(params)
        if teardown:
            teardown_fun.add_cleanup_step(lambda: self.step_api_system_management_delete_roles(
                {
                    "roleId": get_env_data("api_system_management_add_roles")["roleId"]
                }))

    @fresh_parse_data
    @allure.step("筛选角色")
    def step_api_system_management_filter_roles(self, params):
        self.api_system_management_filter_roles(params)

    @allure.step("查询角色，校验属性")
    def step_api_system_management_query_roles(self, params):
        self.api_system_management_query_roles(params)

    @allure.step("修改角色")
    def step_api_system_management_edit_roles(self, params):
        self.api_system_management_edit_roles(params)

    @fresh_parse_data
    @allure.step("删除角色")
    def step_api_system_management_delete_roles(self, params):
        self.api_system_management_delete_roles(params)
