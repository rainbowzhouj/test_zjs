import os

import yaml

from api.base_api import BaseApi


class Auto(BaseApi):
    def __init__(self):
        super().__init__()
        self.params["token"] = self.token
        self.params["base_url"] = self.base_url
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/auto.yaml",
                  encoding='utf-8') as f:
            self.data = yaml.load(f)

    def find_eventCategory(self):
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/event/get_all_events_the_id_and_name",
        #     "headers": {
        #         "SysTemToken": self.token
        #     },
        #     "params": {            }
        # }
        return self.send(self.data['eventCategory'])
        #return self.send(data)


    def pushPlan(self,beginDate,endDate):
        self.params["beginDate"]=beginDate
        self.params["endDate"] = endDate
        return self.send(self.data["pushPlan"])

    def taskList(self,pageNum,pageSize):
        self.params["pageNum"] = pageNum
        self.params["pageSize"] = pageSize
        return self.send(self.data['taskList'])


    def taskCreate(self, miniProgramVisible,name,needPushFlag,visibleCrowd,picUrl):
        # data = {
        #     "method": "post",
        #     "url": f"{self.base_url}/group_buy_event_order/group_buy_order_infos",
        #     "headers": {
        #         "SysTemToken": self.token,
        #         'Content-Type': 'application/json;charset=UTF-8',
        #     },
        #     "json": {"page": 1, "limit": 20, "size": 10, "startTime": startTime, "endTime": endTime,
        #              "eventIds": [eventId], "memberMobile": memberMobile, "memberNickName": "", "memberNo": memberNo}
        # }
        self.params['miniProgramVisible']=miniProgramVisible
        self.params["name"] = name
        self.params["needPushFlag"] = needPushFlag
        self.params["visibleCrowd"]=visibleCrowd
        self.params["picUrl"]=picUrl
        return self.send(self.data["taskCreate"])

    def taskCreate_needPushFlag(self, miniProgramVisible,name,needPushFlag,visibleCrowd,picUrl):
        # data = {
        #     "method": "post",
        #     "url": f"{self.base_url}/group_buy_event_order/group_buy_order_infos",
        #     "headers": {
        #         "SysTemToken": self.token,
        #         'Content-Type': 'application/json;charset=UTF-8',
        #     },
        #     "json": {"page": 1, "limit": 20, "size": 10, "startTime": startTime, "endTime": endTime,
        #              "eventIds": [eventId], "memberMobile": memberMobile, "memberNickName": "", "memberNo": memberNo}
        # }
        self.params['miniProgramVisible']=miniProgramVisible
        self.params["name"] = name
        self.params["needPushFlag"] = needPushFlag
        self.params["visibleCrowd"]=visibleCrowd
        self.params["picUrl"]=picUrl
        return self.send(self.data["taskCreate_needPushFlag"])


    def taskModify(self, miniProgramVisible,name,needPushFlag,visibleCrowd,picUrl):

        self.params['miniProgramVisible']=miniProgramVisible
        self.params["name"] = name
        self.params["needPushFlag"] = needPushFlag
        self.params["visibleCrowd"]=visibleCrowd
        self.params["picUrl"]=picUrl
        return self.send(self.data["task_Modify"])

    def taskPub(self, taskId):
        self.params['taskId']=taskId
        return self.send(self.data["taskPub"])

    def taskDelete(self, taskId):
        self.params['taskId']=taskId
        return self.send(self.data["taskDelete"])

    def taskTop(self, topId):
        self.params['topId']=topId
        return self.send(self.data["taskTop"])


    def taskminiAppVisible(self, taskId,showFlag):
        self.params['taskId']=taskId
        self.params['showFlag'] = showFlag
        return self.send(self.data["taskminiAppVisible"])

    def taskDetail(self, taskId):
        self.params['taskId'] = taskId
        return self.send(self.data["taskDetail"])

    def taskoffShelf(self, taskId):
        self.params['taskId'] = taskId
        return self.send(self.data["taskoffShelf"])

    def taskpushPlan(self, taskId):
        self.params['taskId'] = taskId
        return self.send(self.data["taskpushPlan"])

    def billBoardlistPage(self, pageNum, pageSize):
        self.params['pageNum'] = pageNum
        self.params['pageSize'] = pageSize
        return self.send(self.data["billBoardlistPage"])

    def billBoardbuild(self, automationTaskId, billBoardColumnList, billboardNumber, calculateMethod, startTime,
                       endTime, name, userDimension):
        self.params['automationTaskId'] = automationTaskId
        self.params['billBoardColumnList'] = billBoardColumnList
        self.params['billboardNumber'] = billboardNumber
        self.params['calculateMethod'] = calculateMethod
        self.params['startTime'] = startTime
        self.params['endTime'] = endTime
        self.params['name'] = name
        self.params['userDimension'] = userDimension
        return self.send(self.data["billBoardbuild"])

    def billBoardpush(self):
        return self.send(self.data["billBoardpush"])

    def billBoarddetail(self):
        return self.send(self.data["billBoarddetail"])

    def billBoarddetail(self):
        return self.send(self.data["billBoarddetail"])
