import os

import yaml

# done 封装代码，去除冗余代码
from api.base_api import BaseApi


class Pingketuan(BaseApi):
    # 方式一放到类里：token= None
    # 先获取token
    def __init__(self):
        super().__init__()
        self.params["token"] = self.token
        self.params["base_url"] = self.base_url
        #with open(f"../testcase/datas/pingketuan.yaml", encoding="utf-8")as f:
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/pingketuan.yaml", encoding='utf-8') as f:
            self.data = yaml.load(f)

    def add(self, type=None):
        self.params["type"] = type
        return self.send(self.data["add"])
        # return self.send(data)
        # resource_id = r.json()['data']
        # return resource_id

    def add_group_buy_event(self, resourceId, titile):
        self.params["resourceId"] = resourceId
        self.params["titile"] = titile
        return self.send(self.data["add_group_buy_event"])

    def update_group_buy_event(self, group_buy_event_id, resourceId, titile):
        self.params["group_buy_event_id"] = group_buy_event_id
        self.params["resourceId"] = resourceId
        self.params["titile"] = titile
        return self.send(self.data["update_pkt"])

    def list_group_buy_event(self, titile):
        #查询拼课团列表
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/group_buy_event/list",
        #     "headers": {'SysTemToken': self.token},
        #     "params": {
        #         "page": 1,
        #         "limit": "",
        #         "size": 110,
        #         "searchWord": titile,
        #         "eventSearchVO": "%7B%7D"
        #     }
        #
        # }
        # return self.send(data)
        self.params["titile"] = titile
        return self.send(self.data["list_pkt"])

    def delete_group_buy_event(self, group_buy_event_id):
        # 删除一个拼课团
        # data = {
        #     "method": "DELETE",
        #     "url": f"{self.base_url}/group_buy_event/" + group_buy_event_id,
        #     "headers": {'X-Token': self.token},
        #     "data": {}
        # }
        # return self.send(data)
        self.params["group_buy_event_id"] = group_buy_event_id
        return self.send(self.data['delete_pkt'])

    def add_group_buy_event_specification_detail(self, group_buy_event_id):
        # 为某一个拼课团关联课程班级
        self.params["group_buy_event_id"] = group_buy_event_id
        return self.send(self.data["specification_detail_pkt"])

    def copy_group_buy_event(self, group_buy_event_id):
        # data = {
        #     "method": "PUT",
        #     "url": f"{self.base_url}/group_buy_event/" + group_buy_event_id + "/copy",
        #     "headers": {'X-Token': self.token},
        #     "data": {}
        # }
        self.params["group_buy_event_id"] = group_buy_event_id
        return self.send(self.data["copy_pkt"])

    def enable_group_buy_event(self, group_buy_event_id, enable):
        # 撤销和发布一个拼课团
        # data = {
        #     "method": "PUT",
        #     "url": f"{self.base_url}/group_buy_event/" + group_buy_event_id + "/enable",
        #     "headers": {'X-Token': self.token},
        #     "data": {"enable": enable}
        # }
        self.params["group_buy_event_id"] = group_buy_event_id
        self.params["enable"] = enable
        return self.send(self.data["enable_pkt"])

    def recommend_group_buy_event(self, group_buy_event_id, recommend):
        # 移除和置顶一个拼课团，recommend字段控制
        # data = {
        #     "method": "PUT",
        #     "url": f"{self.base_url}/group_buy_event/" + group_buy_event_id + "/recommend",
        #     "headers": {'X-Token': self.token},
        #     "data": {"recommend": recommend}
        # }
        # return self.send(data)
        self.params["group_buy_event_id"] = group_buy_event_id
        self.params["recommend"] = recommend
        return self.send(self.data["recommend_pkt"])

    def find_team_group_buy_event(self, group_buy_event_id):
        # 查看单个拼课团的参团列表
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/group_buy_event_order/teams",
        #     "headers": {'X-Token': self.token},
        #     "params": {
        #         "page": 1,
        #         "limit": 20,
        #         "size": 10,
        #         "groupBuyEventId": group_buy_event_id
        #     }
        # }
        self.params["group_buy_event_id"] = group_buy_event_id
        return self.send(self.data["find_team_pkt"])

    def find_teamnumber_group_buy_event(self, group_buy_event_id):
        # 查看拼课团的成团规格
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/group_buy_event_order/event_rule/numbers",
        #     "headers": {'X-Token': self.token},
        #     "params": {
        #         "groupBuyEventId": group_buy_event_id
        #     }
        # }
        # return self.send(data)
        self.params["group_buy_event_id"] = group_buy_event_id
        return self.send(self.data["find_teamnumber_pkt"])

    def excel_teamnumber_group_buy_event(self, group_buy_event_id, status):
        data = {
            "method": "get",
            "url": f"{self.base_url}/group_buy_event_order/excel_teams",
            "headers": {'X-Token': self.token, 'Content-Type': 'text/plain;charset=UTF-8'},
            "params": {
                "status": status,
                "groupBuyEventId": group_buy_event_id
            }
        }
        return self.send(data)






    def url_list_excel_group_buy_event(self, group_buy_event_id):
        data = {
            "method": "post",
            "url": f"{self.base_url}/group_buy_event/url_list_excel",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "json": {
                "page": 1,
                "size": 10,
                "channelIds": [],
                "groupBuyEventId": group_buy_event_id,
                "orgIds": []
            }
        }
        return self.send(data)

    def add_launch_group_buy_event(self, channelIds, group_buy_event_id, organizationId):
        self.params['channelIds'] = channelIds
        self.params['group_buy_event_id'] = group_buy_event_id
        self.params['organizationId'] = organizationId

        return self.send(self.data['add_launch'])

    def upload_qrcode_group_buy_event(self):
        data = {
            "method": "GET",
            "url": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/mocha_qrcode_4389708749976803471.png",
            "headers": {'X-Token': self.token},
            "params": {}
        }
        return self.send(data)

    def orders_group_buy_event(self, group_buy_event_id):
        self.params['group_buy_event_id'] = group_buy_event_id
        return self.send(self.data['orders_group_buy_event'])

    def status_group_buy_event(self, group_buy_event_id, status):
        # data = {
        #     "method": "GET",
        #     "url": f"{self.base_url}/group_buy_event_order/search",
        #     "headers": {'X-Token': self.token},
        #     "params": {
        #         "page": 1,
        #         "size": 100,
        #         "limit": 20,
        #         "groupBuyEventId": group_buy_event_id,
        #         "keyWord": "",
        #         "status": status
        #     }
        # }
        self.params['group_buy_event_id'] = group_buy_event_id
        self.params['status'] = status
        return self.send(self.data['order_status'])

    """
    取消订单前，判断该订单是否存在
    - 如存在，则状态是否属于
        - 待支付 UNPAID 
        - 支付处理中 PAY_PROCESSING
        - 预约待审核 RESERVATION_REVIEW_PENDING
        - 待核销 UNUSED
        - 取消待审核 CANCEL_REVIEW_PENDING
    上述5种，属于其中一种的时候，订单可以取消
    - 如不存在，则添加一个订单，将订单的id返回
        - 再调用取消接口
    """

    def canceled_orders_group_buy_event(self, orderId):
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/group_buy_event_order/" + orderId + "/canceled",
            "headers": {'X-Token': self.token},
            "params": {}
        }
        return self.send(data)

    def add_workers(self, name, mobile, workerNo, onWork):
        data = {
            "method": "POST",
            "url": f"{self.base_url}/workers",
            "headers": {'X-Token': self.token},
            "json": {"name": name,
                     "mobile": mobile,
                     "department": "",
                     "workerNo": workerNo,
                     "onWork": onWork}
        }
        return self.send(data)

    def list_workers(self):
        data = {
            "method": "GET",
            "url": f"{self.base_url}/workers",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "size": 10000,
                "limit": 10000,
                "onWork": "",
                "beginTime": "",
                "endTime": "",
                "searchKey": "",
                "sort": ""}
        }
        return self.send(data)

    def update_workers(self, workerId, name, mobile, workerNo, onWork):
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/workers/" + workerId,
            "headers": {'X-Token': self.token},
            "json": {"id": workerId, "name": name, "memberId": mobile, "department": "",
                     "mobile": "11111111111", "workerNo": workerNo, "onWork": onWork, "createdTime": 1618999283000,
                     "updatedTime": 1619000553997, "position": None, "wechatQrcode": None, "headImage": None,
                     "wechatNum": None}
        }
        return self.send(data)

    def delete_workers(self, workerId):
        data = {"method": "DELETE",
                "url": f"{self.base_url}/workers/" + workerId,
                "headers": {'X-Token': self.token},
                "params": {}
                }
        return self.send(data)

#     def add_and_delete(self, userid, name, mobile, department, **kwargs):
#         r = self.add(userid, name, mobile, department, **kwargs)
#         errcode = r.json()['errcode']
#         # userid出现相同的时候
#         if errcode == 60102:
#             user_id = self.list(userid).json()['userid']
#             if not user_id:
#                 return ""
#             self.delete(userid)
#             self.add(userid, name, mobile, department, **kwargs)
#             result = self.list(userid).json()['userid']
#             if not result:
#                 print("add not success")
#             return result
#         # 当出现手机号相同情况
#         elif errcode == 60104:
#             # 根据错误信息返回拿到user_id
#             msg = r.json()['errmsg']
#             user = re.findall("([^:]+)$", msg)[0]
#             # 判断是否存在手机号
#             mobile = self.list(user).json()['mobile']
#             if not mobile:
#                 return ""
#             self.delete(user)
#             self.add(userid, name, mobile, department, **kwargs)
#             result = self.list(userid).json()['userid']
#             if not result:
#                 print("add not success")
#             return result
#         # 手机号和邮箱为空的情况
#         elif errcode == 60129:
#             pg = PhoneNOGenerator()
#             mobile = pg.phoneNORandomGenerator()
#             email = mobile + "@139.com"
#             self.add(userid, name, email=email, **kwargs)
#         # 当部门为空或者不存在时候
#         elif errcode == 40066:
#             print("不合法的部门列表")
#

#
#     def delete_and_detect_user(self, user_ids):
#         deleted_user_ids = []
#         r = self.delete(user_ids)
#         if r.json()["errcode"] == 60111:
#             # 如果用户不存在，就添加一个用户，将它的 userid存储进来
#             for userid in user_ids:
#                 if not self.find_userid_exist(userid):
#                     user_id_tmp = self.add(userid="hechenxin", name="zy", mobile="13452808772", department=[1])
#                     deleted_user_ids.append(user_id_tmp)
#                     # 如果标签存在，就将它存入标签组
#                 else:
#                     deleted_user_ids.append(userid)
#
#         elif r.json()["errcode"] == 301005:
#             # 当用户id为本人时，不允许删除
#             print("不允许删除创建者")
#         r = self.delete(deleted_user_ids)
#         return r
#
#     def find_userid_exist(self, user_id):
#         # 查询用户id是否存在，如果不存在，报错
#         user = self.list(user_id).json()["errmsg"]
#         if 'userid not found' == user:
#             return ""
#
#     def get_partyid(self, par_id=None):
#         # par_id 为空时，获取所有部门信息
#         data = {"method": "post",
#                 "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
#                 "params": {"access_token": self.token, "id": par_id}}
#         return self.send(data)
#
#