from KeywordDriven.base.base import BaseClient


class SystemManagementApi(BaseClient):

    def system_management_add_roles(self, params):
        """
        新增角色
        :return:
        """
        url = "/manage-server/sys/miguRoles"
        self.post(url=self.domain + url, json=params)

    def system_management_filter_roles(self, params):
        """
        过滤角色
        :return:
        """
        url = "/manage-server/sys/miguRoles/page"
        response = self.get(url=self.domain + url, data=params)
        return response.json()

    def system_management_query_roles(self, params):
        """
        查看角色
        :return:
        """
        url = f"/manage-server/sys/miguRoles/{params['roleId']}"
        response = self.get(url=self.domain + url)
        return response.json()

    def system_management_edit_roles(self, params):
        """
        修改角色
        :return:
        """
        url = f"/manage-server/sys/miguRoles/{params['id']}"
        self.put(url=self.domain + url, json=params)

    def system_management_delete_roles(self, params):
        """
        修改角色
        :return:
        """
        url = f"/manage-server/sys/miguRoles/{params['roleId']}"
        self.delete(url=self.domain + url)
