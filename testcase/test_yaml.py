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
    env = {"name":"zidonghuaceshi","create_by":"周晶","orgId":"4608","orgName":"终端赋能处","startTime":"2021-07-21 16:45","endTime":"2021-07-21 23:59","miniProgramVisible":"1","description":"","visibleCrowd":"0","picUrl":"https://marketingcentertest-1252877917.cos.ap-guangzhou.myqcloud.com/55f842f2e0764779a136fa94c5ff4d80.jpg","needPushFlag":"0","eventList":[{"id":701,"automationTaskId":214,"eventType":"0","eventId":"867412408176058368","eventName":"0721权限控制","promotionDesc":"","showOrder":1,"showUrl":""}],"pushPlanParam":{"pushDate":"","pushHour":"","pushDateTime":"","pushWorkerList":[],"pushOrgList":[]},"taskRewardList":[{"id":26,"automationTaskId":214,"startRanking":1,"endRanking":2,"rewardName":"telephone","showOrder":1,"getTime":"1626858643127442013"}],"id":"214","delEventRelIds":""}
    with open("transport.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)

