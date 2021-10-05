from api.base_api import BaseApi


class Employee(BaseApi):
    def __init__(self):
        super().__init__()

    #开通账号
    def update(self, id,userid, name, departmentId):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/account/saveOrUpdate",
            "headers": {
                "systemtoken": self.token
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

    def find(self, **kwargs):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/authority/api/employee/getEmployList",
            "headers": {
                "systemtoken": self.token
            },
            "json": {
                #"name": name,
                "pageNum": "1",
                "pageSize": "10",
                **kwargs
                # "departmentName": departmentName,
                # "employeeCode":employeeCode
                # "status": "1",
                # "mobile": "2",

            }
        }
        return self.send(data)