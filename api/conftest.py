import os
import sys

import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# def env(self):
#     env = yaml.safe_load(open(f"{os.path.dirname(os.path.dirname(__file__))}/testcase/datas/env.yaml",
#                               encoding='utf-8'))
#     self.data["url"] = str(self.base_url["url"]). \
#         replace("env_select",
#                 env["env_select"][env["default"]])
#
#
# def login(self):
#     userId="jing.zhou@chinapex.com"
#     password="chinapex007*"
#     data = {
#         "method": "get",
#         "url": f'{self.base_url}/service/authority/api/authority/uatLogin',
#         "params": {'userId': userId, 'password': password}
#     }
#     r = self.send(data)
#     token = r.json()['data']["sysToken"]
#     return token