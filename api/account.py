
from api.base_api import BaseApi


class Account(BaseApi):
    def __init__(self):
        super().__init__()

    def create(self, userid,name,departmentId):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/saveOrUpdate",
            "headers": {
                "SysTemToken": self.token,
                'Content-Type': 'application/json;charset=UTF-8',
            },
            "json": {
                "accountName": name,
                "departmentId": departmentId,
                "userId": userid,
                "dataRoleIds": [23],
                "operateIds": [175, 27, 32, 37]
            }
        }
        return self.send(data)

    def update(self, id,userid, name, departmentId):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/saveOrUpdate",
            "headers": {
                "SysTemToken": self.token
            },
            "json": {
                "id": id,
                "accountName": name,
                "userId": userid,
                "departmentId": departmentId,
                "dataRoleIds": [23],
                "operateIds": [175, 27, 32, 37]
            }
        }
        return self.send(data)

    def find(self, staffName,departmentName):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/getAccountList",
            "headers": {
                "SysTemToken": self.token
            },
            "json": {
                "staffName": staffName,
                "departmentName": departmentName,
                # "dataRoleId": "1",
                # "operateRoleId": "2",
                "pageNum": "1",
                "pageSize": "10"
            }
        }
        return self.send(data)

    def find_one(self,accountId):
        data={
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/getAccountDetail",
            "headers": {"SysTemToken": self.token,
                       'Content-Type': 'application/json;charset=UTF-8'},
            "params": {
                       "accountId": accountId}
        }
        return self.send(data)

    def start_account(self, id,status):
        # 启/禁用账号
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/changeAccountStatus",
            "headers": {"SysTemToken": self.token},
            "json": {
                "id": id,
                "status": status}
        }
        return self.send(data)

