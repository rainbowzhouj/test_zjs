import os

import yaml

from api.base_api import BaseApi


class Report(BaseApi):
    def __init__(self):
        super().__init__()
        self.params["token"] = self.token
        self.params["base_url"] = self.base_url
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/report.yaml",
                  encoding='utf-8') as f:
            self.data = yaml.load(f)

    def find_event(self):
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/event/get_all_events_the_id_and_name",
        #     "headers": {
        #         "SysTemToken": self.token
        #     },
        #     "params": {            }
        # }
        return self.send(self.data['event_list'])
        #return self.send(data)

#可使用参数化，查询不同的活动报表详情
    def find_event_one(self,eventId,startTime,endTime,memberMobile,memberNo):
        # data = {
        #     "method": "post",
        #     "url": f"{self.base_url}/report/promotion_infos",
        #     "headers": {
        #         "SysTemToken": self.token,
        #         'Content-Type': 'application/json;charset=UTF-8',
        #     },
        #     "json": {"page": 1, "limit": 20, "size": 10, "startTime": startTime, "endTime": endTime,
        #              "eventIds": [eventId], "memberMobile": memberMobile, "memberNickName": "", "memberNo": memberNo}
        # }
        self.params["eventId"]=eventId
        self.params["startTime"] = startTime
        self.params["endTime"] = endTime
        self.params["memberMobile"] = memberMobile
        self.params["memberNo"] = memberNo
        return self.send(self.data["event_one"])

    def find_group_buy_event(self):
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/group_buy_event/list",
        #     "headers": {
        #         "SysTemToken": self.token
        #     },
        #     "params": {  "page":1,"size":1000          }
        # }
        return self.send(self.data['group_buy_event_list'])

    # 可使用参数化，查询不同的拼课团报表详情
    def find_group_buy_event_one(self, eventId,startTime,endTime,memberMobile,memberNo):
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
        self.params['eventId']=eventId
        self.params["startTime"] = startTime
        self.params["endTime"] = endTime
        self.params["memberMobile"] = memberMobile
        self.params["memberNo"] = memberNo
        return self.send(self.data["group_buy_event_one"])

    def find_event_category(self):
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/dab/event_category",
        #     "headers": {
        #         "SysTemToken": self.token
        #     },
        #     "params": {  "page":1,"size":1000          }
        # }
        return self.send(self.data['event_category'])

    def find_event_category_list(self):

        return self.send(self.data['event_category_list'])

    def find_event_category_one(self, eventId):
        #{"beginTime":"","endTime":"","page":1,"pageSize":10,"eventIds":["852609070543196160"],"eventCategoryFirstId":"847066781074096128","eventCategorySecondId":""}
        self.params['eventId'] = eventId
        return self.send(self.data['event_category_one'])

