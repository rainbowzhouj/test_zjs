from api.base_api import BaseApi


class Huodongyuyue(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, type):
        data = {
            "method": "get",
            "url": f"{self.base_url}/common/get_new_resource_id",
            "params": {"type": type},
            "headers": {'systemtoken': self.token}
        }
        return self.send(data)

    def update_event(self, event_id, resourceId, name):
        # 更新活动
        data = {
            "method": "put",
            "url": f"{self.base_url}/event/" + event_id,
            "headers": {
                'systemtoken': self.token,
                'Content-Type': 'application/json;charset=UTF-8'
            },
            "json": {
                "shareImageUrl": "null",
                "customerServerShowVO": {
                    "title": "",
                    "image": "",
                    "iconName": "",
                    "status": False
                },
                "customerServerGuideOpened": False,
                "fissionPosterUrl": "null",
                "hasFissionPoster": "null",
                "shareId": "null",
                "organizationId": "587357539759292416",
                "resourceId": resourceId,
                "brief": "null",
                "name": name,
                "banner": "null",
                "published": False,
                "chargedAmount": 0,
                "reservationReviewToggle": False,
                "cancelReviewToggle": False,
                "chargeToggle": True,
                "createdTime": 1614925860000,
                "coverImage": "null",
                "detail": "",
                "form": "[]",
                "id": event_id,
                "eventSessionList": [
                    {
                        "id": "817403833151447040",
                        "startTime": 1603696130000,
                        "endTime": 1604073600000,
                        "quota": "null",
                        "createdTime": 0,
                        "address": "",
                        "placeType": "STORE",
                        "applicableStoreIds": "610770683353366528",
                        "seatsLeft": 100,
                        "latitude": "null",
                        "longitude": "null",
                        "applicableStoreCount": 0
                    }
                ],
                "beginTime": 1603641600000,
                "lastTime": 1604073600000,
                "tags": [

                ],
                "hasOrder": "null",
                "orderId": "null",
                "smsTemplateId": "",
                "couponBatch": "",
                "status": "CLOSED",
                "endTime": 1604073600000,
                "eventCategorySecondId": "",
                "eventCategoryFirstId": "767799481818927104",
                "eventCategorySecondIdName": "",
                "eventCategoryFirstIdName": "活动类目-lu",
                "applicableStoreIds": "768420307354107904,768419758852390912,768420240182329344,768573611400871936,768419795774849024,768419937961754624,768419724291325952,768574015970852864,768419885767835648,768419983163768832,768420112813899776,768419663792685056,768419964918546432",
                "applicableStoreCount": 13,
                "storeVo": {
                    "name": " ",
                    "organizationId": "768420307354107904",
                    "longitude": "",
                    "latitude": "",
                    "address": "啊范德萨",
                    "tel": "",
                    "length": 0
                },
                "guideImage": "",
                "checkinQrcodeToggle": False
            },
        }
        return self.send(data)

    def list_event(self, name):
        # 查询活动列表
        data = {
            "method": "get",
            "url": f"{self.base_url}/event/list",
            "headers": {'systemtoken': self.token},
            "params": {
                "page": 1,
                "limit": 50,
                "size": 50,
                "searchWord": name,
                "eventSearchVO": "%7B%7D"
            }
        }
        return self.send(data)

    def delete_event(self, event_id):
        # 删除一个活动
        data = {
            "method": "DELETE",
            "url": f"{self.base_url}/event/" + event_id,
            "headers": {'systemtoken': self.token},
            "data": {}
        }
        return self.send(data)

    def copy_event(self, event_id):
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/event/" + event_id + "/copy",
            "headers": {'systemtoken': self.token},
            "data": {}
        }
        return self.send(data)

    def publish_event(self, event_id, publish):
        # 撤销和发布一个活动
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/event/" + event_id + "/publish",
            "headers": {'systemtoken': self.token},
            "data": {"publish": publish}
        }
        return self.send(data)

    def recommend_event(self, event_id, recommend):
        # 移除和置顶一个活动，recommend字段控制
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/event/" + event_id + "/recommend",
            "headers": {'systemtoken': self.token},
            "data": {"recommend": recommend}
        }
        return self.send(data)

    def find_get_order_list_event(self, event_id):
        # 查看单个活动的参团列表
        """
        "json": {
                "channel": "微信",
                "orderStatus": "UNPAID",
                "pamentStatus": "UNPAID",
                "storeOrgIds": ["768419663792685056"],
                "keyWord":"150"
            }
        :param event_id:
        :return:
        """
        data = {
            "method": "post",
            "url": f"{self.base_url}/event_orders/get_order_list",
            "headers": {'systemtoken': self.token},
            "params": {
                "page": 1,
                "size": 10,
                "eventId": event_id
            },
            "json": {
                "storeOrgIds": []
            }

        }
        return self.send(data)

    def find_teamnumber_event(self, event_id, status):
        data = {
            "method": "get",
            "url": f"{self.base_url}/event_orders/search",
            "headers": {'systemtoken': self.token},
            "params": {
                "page": 1,
                "size": 20,
                "limit": 20,
                "event_id": event_id,
                "keyWord": "",
                "status": status

            }
        }
        return self.send(data)

    def find_event_checkin_qrcode(self, event_id):
        # https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_checkin_qrcode/list?page=1&size=20
        data = {
            "method": "post",
            "url": f"{self.base_url}/event_checkin_qrcode/list",
            "headers": {'systemtoken': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "params": {
                "page": 1,
                "size": 20
            },
            "json": {
                "page": 1,
                "limit": 20,
                "size": 20,
                "eventId": event_id,
                "storeOrgIds": []
            }
        }
        return self.send(data)

    def canceled_event(self, event_id):
        data = {
            "method": "PUT",
            "url": f"{self.base_url}/event_orders/" + event_id + "/canceled",
            "headers": {'systemtoken': self.token},
            "data": {}
        }
        return self.send(data)


# {"shareImageUrl": null, "customerServerShowVO": {"title": "", "image": "", "iconName": "", "status": False},
#  "customerServerGuideOpened": False, "fissionPosterUrl": null, "hasFissionPoster": null, "shareId": null,
#  "organizationId": "587357539759292416", "resourceId": "hd_854822127000858624", "name": "202106161", "brief": null,
#  "banner": null, "published": False, "chargedAmount": 0, "reservationReviewToggle": true, "cancelReviewToggle": true,
#  "chargeToggle": true, "createdTime": 1623847135000, "coverImage": null, "detail": "", "form": "[]",
#  "id": "854822370903830528", "eventSessionList": [
#     {"id": "854822370924802048", "startTime": 1623772800000, "endTime": 1624982400000, "quota": 7, "createdTime": 0,
#      "address": "", "placeType": "NONE",
#      "applicableStoreIds": "610770683353366528,611621694439686144,611621924300128256", "seatsLeft": 7, "latitude": null,
#      "longitude": null, "applicableStoreCount": 0}], "beginTime": 1623772800000, "lastTime": 1624982400000, "tags": [],
#  "hasOrder": null, "orderId": null, "smsTemplateId": "", "couponBatch": "", "status": "CLOSED",
#  "endTime": 1624982400000, "eventCategorySecondId": "", "eventCategoryFirstId": "847066781074096128",
#  "eventCategorySecondIdName": "", "eventCategoryFirstIdName": "测试部",
#  "applicableStoreIds": "610770683353366528,611621924300128256,611621694439686144", "applicableStoreCount": 3,
#  "storeVo": {"name": "南山巧问辅导班", "organizationId": "610770683353366528", "longitude": "113.92248",
#              "latitude": "22.53453", "address": "学府路220东方银座广场二楼巧问教育(东方银座、富邦国际酒店)", "tel": "13522380238", "length": 0},
#  "guideImage": "", "checkinQrcodeToggle": False}
