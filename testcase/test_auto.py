import datetime

import pytest

from api.automation import Auto


class TestAuto:

    def setup(self):
        self.auto = Auto()

    def test_eventCategory(self):
        r=self.auto.find_eventCategory()
        assert r.json()['code']=="200"
        #assert r.json()['data'] is not None


    def test_pushPlan(self):
        beginDate = "2021-7-01"
        endDate = '2021-7-31'
        r=self.auto.pushPlan(beginDate=beginDate,endDate=endDate)
        assert r.json()['code'] == "200"

    def test_taskList(self):
        pageNum = "1"
        pageSize = '10'
        r=self.auto.taskList(pageNum=pageNum,pageSize=pageSize)
        assert r.json()['code'] == "200"

    @pytest.mark.parametrize("miniProgramVisible,name,needPushFlag,picUrl,visibleCrowd", [["0", "1", "0", "", ""],
                                                                                          ["1", "2", "0",
                                                                                           "https://marketingcentertest-1252877917.cos.ap-guangzhou.myqcloud.com/6ec8c05b57d146cea6e6309599e9d5ac.jpg",
                                                                                           "1"]])
    def test_taskCreate(self, miniProgramVisible, name, needPushFlag, visibleCrowd, picUrl):
        r = self.auto.taskCreate(miniProgramVisible=miniProgramVisible, name=name, needPushFlag=needPushFlag,
                                 visibleCrowd=visibleCrowd, picUrl=picUrl)
        assert r.json()['code'] == '200'

    @pytest.mark.parametrize("miniProgramVisible,name,needPushFlag,picUrl,visibleCrowd", [["0", "接口自动化测试", "0", "", ""],
                                                                                          ["1", "接口自动化测试1", "0",
                                                                                           "https://marketingcentertest-1252877917.cos.ap-guangzhou.myqcloud.com/6ec8c05b57d146cea6e6309599e9d5ac.jpg",
                                                                                           "1"]])
    def test_taskCreate_needPushFlag(self,miniProgramVisible,name,needPushFlag,visibleCrowd,picUrl):
        miniProgramVisible="1"
        name="接口自动化测试"+ str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        needPushFlag="0"
        picUrl="https://marketingcentertest-1252877917.cos.ap-guangzhou.myqcloud.com/6ec8c05b57d146cea6e6309599e9d5ac.jpg"
        visibleCrowd='1'
        r= self.auto.taskCreate_needPushFlag(miniProgramVisible=miniProgramVisible,name=name,needPushFlag=needPushFlag,visibleCrowd=visibleCrowd,picUrl=picUrl)
        assert r.json()['code']=='200'

    @pytest.mark.parametrize("miniProgramVisible,name,needPushFlag,picUrl,visibleCrowd", [["1", "1", "0",
                                                                                           "https://marketingcentertest-1252877917.cos.ap-guangzhou.myqcloud.com/55f842f2e0764779a136fa94c5ff4d80.jpg",
                                                                                           "0"],
                                                                                          ])
    def test_taskModify(self, miniProgramVisible, name, needPushFlag, visibleCrowd, picUrl):
        eventId = "867412408176058368"
        name = "autotest" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r=self.auto.taskModify(miniProgramVisible=miniProgramVisible, name=name, needPushFlag=needPushFlag,
                                 visibleCrowd=visibleCrowd, picUrl=picUrl)
        assert r.json()['data'][0]['eventId'] == eventId


    def test_taskPub(self):
        # 取第一条任务进行推送或取消推送
        taskId = "214"
        r = self.auto.taskPub(taskId=taskId)
        assert r.json()['code'] == '200'

    def test_taskDelete(self):
        taskId = "216"
        r = self.auto.taskDelete(taskId=taskId)
        assert r.json()['code'] == '200'

    def test_taskTop(self):
        topId = "216"
        r = self.auto.taskTop(topId=topId)
        assert r.json()['code'] == '200'

    def test_miniAppVisible(self):
        taskId = "216"
        showFlag = '1'
        r = self.auto.taskminiAppVisible(taskId=taskId, showFlag=showFlag)
        assert r.json()['code'] == '200'

    def test_taskDetail(self):
        taskId = "216"
        r = self.auto.taskDetail(taskId=taskId)
        assert r.json()['code'] == '200'

    def test_taskoffShelf(self):
        taskId = "216"
        r = self.auto.taskoffShelf(taskId=taskId)
        assert r.json()['code'] == '200'

    def test_taskpushPlan(self):
        taskId = "216"
        r = self.auto.taskpushPlan(taskId=taskId)
        assert r.json()['code'] == '200'

    def test_billBoardlistPage(self):
        pageNum = "1"
        pageSize = "10"
        r = self.auto.billBoardlistPage(pageNum=pageNum, pageSize=pageSize)
        assert r.json()['code'] == '200'

    def test_billBoardbuild(self):
        automationTaskId = '214'
        billBoardColumnList = ["ranking", "nickName", "dept", "name"]
        billboardNumber = "4"
        calculateMethod = "0"
        startTime = "2021-07-23 16:51:35"
        endTime = "2021-07-31 16:51:35"
        name = "autobillboard"
        userDimension = "0"

        r = self.auto.billBoardlistPage(automationTaskId=automationTaskId, billBoardColumnList=billBoardColumnList,
                                        billboardNumber=billboardNumber, calculateMethod=calculateMethod,
                                        startTime=startTime, endTime=endTime, name=name, userDimension=userDimension)
        assert r.json()['code'] == '200'

    def test_billBoardpublish(self):
        r = self.auto.billBoardlistPage()
        assert r.json()['code'] == '200'

    @pytest.mark.parametrize("mobile", [["15001731170"], ["17521151170"], ["18621614590"]])
    @pytest.mark.parametrize("tms", [["当期在读"], ["曾报读"], ["已预报"], ["从未报读"]])
    @pytest.mark.parametrize("nsb", [["未签约"], ["近一个月在消耗"], ["未上首课"], ["停课1个月或以上"], ["结束3个月内"], ["结束3个月外"], ["其他"]])
    def test_data(self, mobile, tms, nsb):
        # print("手机号": mobile ,"班辅": tms, "个辅": nsb)
        print(mobile, tms, nsb)
