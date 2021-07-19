from api.base_api import BaseApi


class Role(BaseApi):
    def __init__(self):
        super().__init__()

    def find_RoleByType(self, roleType):
        data={
            "method":"get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/getRoleByType",
            "params": {"roleType": roleType},
            "headers" : {
            'Content-Type': 'application/json;charset=UTF-8',
            'SysTemToken': self.token
        }
        }
        return self.send(data)

    def find_OperateRoles(self, roleId):
        data={
            "method":"get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/getOperateRoles",
            "params": {"roleId": roleId},
            "headers" : {
            'Content-Type': 'application/json;charset=UTF-8',
            'SysTemToken': self.token
        }
        }
        return self.send(data)

#  创建操作角色
    def create(self,roleName):
        data={
            "method":"post",
            "url" : "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateOperateRole",
            "json" : {"saveRoleParam": {"id": "null", "roleName": roleName, "comments": ""},
                         "permissionIds": [ ]},
            "headers" : {
            'Content-Type': 'application/json;charset=UTF-8',
            'SysTemToken': self.token
        }
        }
        return self.send(data)

        #  更新操作角色
    def update(self, id,roleName):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateOperateRole",
            "json": {"saveRoleParam": {"id": id, "roleName": roleName, "comments": ""},
                        "permissionIds": [4, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
                                          130,
                                          131, ]},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def delete(self, roleId,roleType):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/deleteRole",
            "json": {"roleId": roleId,
                        "roleType": roleType},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def get_tree(self):
        data = {
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/permission/listInTree",
            "params": {},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }}
        return self.send(data)

    def get_list(self):
        data = {
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/permission/listDefault",
            "params": {},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }}
        return self.send(data)

#  创建数据角色
    def create_datarole(self,roleName):
        data={
            "method":"post",
            "url" : "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateDataRole",
            "json" : {"id": "null", "roleName": roleName, "comments": ""
                         },
            "headers" : {
            'Content-Type': 'application/json;charset=UTF-8',
            'SysTemToken': self.token
        }
        }
        return self.send(data)


    def update_datarole(self, roleName,id):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateDataRole",
            "json": {"id": id, "roleName": roleName, "comments": "",
                     },
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def find_datarole(self, roleName, pageNum, pageSize):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/getDataRoleList",
            "json": {"pageNum": pageNum, "roleName": roleName, "pageSize": pageSize},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def find_one_datarole(self, roleId):
        data = {
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/getDataPermissionByRoleId",
            "params": {"roleId": roleId},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

        #  创建数据角色权限
    def create_DataRolePermission(self, roleName):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateOperateRole",
            "json": {"saveRoleParam": {"id": "null", "roleName": roleName, "comments": ""},
                     "dataPermissions": [{"systemType": "tms", "citys": "21", "regions": "59", "campus": "162",
                                          "organizationIds": "588132666851721241,689856505393971200"},
                                         {"systemType": "nsb", "citys": "", "regions": "null", "campus": "null",
                                          "organizationIds": ""},
                                         {"systemType": "other", "citys": "", "regions": "null", "campus": "null",
                                          "organizationIds": ""}]},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def update_DataRolePermission(self, id,roleName):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/role/saveOrUpdateOperateRole",
            "json": {"saveRoleParam": {"id": id, "roleName": roleName, "comments": ""},
                     "dataPermissions": [{"systemType": "tms", "citys": "21", "regions": "59", "campus": "162",
                                          "organizationIds": "588132666851721241,689856505393971200"},
                                         {"systemType": "nsb", "citys": "", "regions": "null", "campus": "null",
                                          "organizationIds": ""},
                                         {"systemType": "other", "citys": "", "regions": "null", "campus": "null",
                                          "organizationIds": ""}]},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)