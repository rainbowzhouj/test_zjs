from api.base_api import BaseApi


class Campus(BaseApi):
    def __init__(self):
        super().__init__()

    def find(self, id):
        data = {
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/manage/api/campus/getCampusById",
            "params": {"id": id},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def find_list(self, pageNum,pageSize):
        data = {
            "method": "post",
            "url": "https://zjs.zytest.net/service/manage/api/campus/getCampusList",
            "json": {"pageNum": pageNum,
                     "pageSize": pageSize,
                     "city": "",
                     "system": "",
                     "region": "",
                     "dictValue": "",
                     },
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

#{"id":null,"createBy":"周晶","createTime":"","updateBy":"","updateTime":"","delFlag":"0","enumId":"33","dictValue":"auto","orderBy":0,"parentId":"95","leaveInfoType":"8","dictShow":"1","campusTelephone":"","campusAddress":"","campusLongitude":"","campusLatitude":"","dictType":"2","dictSync":"0","dictEditStatus":"0"}
#
    def create(self, id):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/manage/api/campus/addCampus",
            "json": {"id": "", "createBy": "周晶", "createTime": "", "updateBy": "", "updateTime": "", "delFlag": "0",
                     "enumId": "33", "dictValue": "auto", "orderBy": 0, "parentId": "95", "leaveInfoType": "8",
                     "dictShow": "1", "campusTelephone": "", "campusAddress": "", "campusLongitude": "",
                     "campusLatitude": "", "dictType": "2", "dictSync": "0", "dictEditStatus": "0"},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def update(self, id, fieldName, fieldValue):
        data = {
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/manage/api/campus/updataCampusShowOrSync",
            "json": {"id": id,
                     "fieldName": fieldName,
                     "fieldValue": fieldValue,

                     },
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def delete(self, id):
        data = {
            "method": "get",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/manage/api/campus/delectCampusById",
            "params": {"id": id},
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)

    def employlist(self,pageNum,pageSize):
        data={
            "method": "post",
            "url": "https://zy-zjs-dev.chinapex.com.cn/service/manage/api/employee/getEmployList",
            "json": {"pageNum": pageNum,
                     "pageSize": pageSize,
                     "name": "",
                     "userid": "",
                     "status": "",
                     "departmentname": "",


                     },
            "headers": {
                'Content-Type': 'application/json;charset=UTF-8',
                'SysTemToken': self.token
            }
        }
        return self.send(data)
