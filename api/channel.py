import os

import yaml

from api.base_api import BaseApi


class Channel(BaseApi):

    def __init__(self):
        super().__init__()
        self.params["token"] = self.token
        self.params["base_url"] = self.base_url
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/channel.yaml",
                  encoding='utf-8') as f:
            self.data = yaml.load(f)

    def list_group_buy_event(self):
        # data = {
        #     "method": "get",
        #     "url": f"{self.base_url}/channel/list",
        #     "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
        #     "params": {
        #         "page": 1,
        #         "size": 100, }
        # }
        return self.send(self.data['channel_list'])


    def add_group_buy_event(self, channel_name):
        # data = {
        #     "method": "POST",
        #     "url": f"{self.base_url}/channel",
        #     "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
        #     "json": {
        #         "descr: "123",
        # name: "副本", }
        # }
        self.params["channel_name"] = channel_name
        return self.send(self.data['channel_add'])


    def update_group_buy_event(self, channel_id, channel_name):
        self.params["channel_id"] = channel_id
        self.params["channel_name"] = channel_name
        return self.send(self.data['channel_update'])


    def delete_group_buy_event(self, channel_id):
        # data = {
        #     "method": "POST",
        #     "url": f"{self.base_url}/channel",
        #     "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
        #     "json": {
        #         "descr: "123",
        # name: "副本", }
        # }
        self.params["channel_id"] = channel_id
        return self.send(self.data['channel_delete'])

    def area_add(self, area_name):
        self.params["area_name"] = area_name
        return self.send(self.data['area_add'])

    def area_update(self, area_id, area_name):
        self.params["area_id"] = area_id
        self.params["area_name"] = area_name
        return self.send(self.data['area_update'])

    def area_delete(self, area_id):
        self.params["area_id"] = area_id
        return self.send(self.data['area_delete'])

    def store_list(self):
        return self.send(self.data['store_list'])

    def store_add(self, store_name):
        self.params["store_name"] = store_name
        return self.send(self.data['store_add'])

    def store_update(self, store_id, store_name):
        self.params["store_id"] = store_id
        self.params["store_name"] = store_name
        return self.send(self.data['store_update'])

    def store_delete(self, store_id):
        self.params["store_id"] = store_id
        return self.send(self.data['store_delete'])

    def organizations_list(self):
        return self.send(self.data['organizations_list'])