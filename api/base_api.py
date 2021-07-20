import json
import os

import requests
import yaml


class BaseApi:
    params = {}
    json_data = None

    def __init__(self):
        # 多环境切换
        self.dev_url = "https://zy-zjs-dev.chinapex.com.cn"
        env = yaml.safe_load(open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/env.yaml",
                                  encoding='utf-8'))
        self.base_url = str(self.dev_url). \
            replace("zy-zjs-dev.chinapex.com.cn",
                    env["env_select"][env["default"]])
        # print(self.base_url)
        self.token = self.get_token()
        #self.token = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2MjY3NzM1NTEsInN1YiI6IlRhbk5lbmdXZW4tMTMiLCJjcmVhdGVkIjoxNjI2MTY4NzUxNjA3fQ.GH6q7YyXxZTw2m243rMgFLDuTRvV_K67T32E2A3DEmyu6QwYQIeK2KYPiigxQQ2KJLpOSQ6HGptRsKQwJb9Few"

    def get_token(self):
        data = {
            "method": "get",
            "url": f"{self.base_url}/service/authority/api/authority/uatLogin",
            "headers": {'Content-Type': 'application/json;charset=UTF-8'},
            "params": {"userId": "jing.zhou@chinapex.com",
                     "password": "chinapex007*"}
        }
        r = self.send(data)
        token = "Bearer " + r.json()['data']["sysToken"]
        return token


    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        # return requests.request(**data).json()
        r = requests.request(**data)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        return r

    def env(self):
        env = yaml.safe_load(open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/env.yaml",
                                  encoding='utf-8'))
        self.data["url"] = str(self.base_url["url"]). \
            replace("env_select",
                    env["env_select"][env["default"]])
