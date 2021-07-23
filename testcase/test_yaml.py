import requests
import yaml


class Api:
    data = {
        "schema": "http",
        "method": "get",
        "url": "http://docker.testing-studio.com:10000/demo64.txt",
        "headers":
            {"Host": None}
    }

    # 把host修改为ip，并附加host header
    env = {
        "docker.testing-studio.com": {
            "dev": "127.0.0.1",
            "test": "1.1.1.2"
        },
        "default": "dev"
    }
    data["url"] = str(data["url"]).replace(
        "docker.testing-studio.com",
        env["docker.testing-studio.com"][env["default"]]
    )
    data["headers"]["Host"] = "docker.testing-studio.com"

    # data是一个请求的信息
    def send(self, data:dict):
        # 进行替换
        data["url"] = str(data["url"]).replace("docker.testing-studio.com", self.env["env_select"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r

if __name__ == '__main__':
    api = Api()
    print(api.send(api.data).text)

def test_yaml():
    env = {"id": 36, "automationTaskId": 81, "pushDate": "2021-8-02", "pushHour": "12",
           "pushWorkerList": [{"id": "shrzy147221_luoxiaoxin2", "orgName": "区庄教学中心", "name": "罗晓欣"}], "pushOrgList": [],
           "targetType": "1", "targetId": 36}
    with open("transport.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)

