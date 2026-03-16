# -*- coding: utf-8 -*-
import allure

from KeywordDriven.step.step_system_management import StepSystemManagementApiClient
from KeywordDriven.tdata import get_env_data
from public.random_data import faker


@allure.feature('角色功能')
class TestUser(StepSystemManagementApiClient):

    @allure.title("新建角色，修改角色，校验角色")
    def test_add_role(self):
        self.step_api_system_management_add_roles(
            {"roleName": faker.generate_random_string(min_length=1, max_length=32),
             "isPreWeekly": faker.random_bool,
             "isPrePerformance": faker.random_bool,
             "description": faker.generate_random_string(min_length=0, max_length=128)
             }, teardown=True)
        self.step_api_system_management_edit_roles({
            "id": get_env_data("api_system_management_add_roles")["roleId"],
            "roleName": faker.generate_random_string(min_length=1,
                                                     max_length=32),
            "isPreWeekly": faker.random_bool,
            "isPrePerformance": faker.random_bool,
            "description": faker.generate_random_string(min_length=0, max_length=128)
        })
        self.step_api_system_management_query_roles({
            "roleId": get_env_data("api_system_management_edit_roles")["id"],
            "roleName": get_env_data("api_system_management_edit_roles")["roleName"],
            "isPreWeekly": get_env_data("api_system_management_edit_roles")["isPreWeekly"],
            "isPrePerformance": get_env_data("api_system_management_edit_roles")["isPrePerformance"],
            "description": get_env_data("api_system_management_edit_roles")["description"],
        })
