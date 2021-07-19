import pytest

from api.report import Report


class TestReport:

    def setup(self):
        self.report = Report()

    def test_event(self):
        r=self.report.find_event()
        assert r.json()['code']=="0"
        assert r.json()['data'] is not None


    def test_eventone(self):
        eventId = "852609070543196160"
        startTime = ''
        endTime = ''
        memberMobile= ''
        memberNo= ''
        r=self.report.find_event_one(eventId=eventId,startTime=startTime,endTime=endTime,memberMobile=memberMobile,memberNo=memberNo)
        assert r.json()['data'][0]['eventId'] == eventId


    def test_group_buy_event(self):
        r= self.report.find_group_buy_event()
        assert r.json()['code']=='0'

    def test_find_group_buy_event_one(self):
        eventId = "849390304411455488"
        startTime = ""
        endTime = ""
        memberMobile = "13244766662"
        memberNo = ""
        r=self.report.find_group_buy_event_one(eventId=eventId,startTime=startTime,endTime=endTime,memberMobile=memberMobile,memberNo=memberNo)
        assert r.json()['data'][0]['eventId'] == eventId

    def test_event_category(self):
        r= self.report.find_event_category()
        assert r.json()['code']=='0'

    def test_event_category_list(self):
        r= self.report.find_event_category_list()
        assert r.json()['code']=='0'

    def test_event_category_one(self):
        eventId = "849334814679699456"
        r = self.report.find_event_category_one(eventId=eventId)
        assert r.json()['code']=='0'

    def test_find_event_category_firstone(self):
        r= self.report.find_event_category_list()
        eventId=r.json()["data"][0]["id"]
        r1 = self.report.find_event_category_one(eventId=eventId)
        assert r1.json()['code'] == '0'
        assert r.json()['data'][0]['resourceId']==r1.json()['data'][0]['resourceId']


    @pytest.mark.parametrize("activity_introducer_type",[["0"], ["1"], ["2"]])
    @pytest.mark.parametrize("activity_invitee_type", [["0"], ["1"], ["2"]])
    @pytest.mark.parametrize("tms",[["1"], ["2"], ["3"],["4"]])
    #@pytest.mark.parametrize("nsb", [["未签约"], ["近一个月在消耗"], ["未上首课"],["停课1个月或以上"], ["结束3个月内"], ["结束3个月外"],["其他"]])
    def test_data(self,activity_introducer_type,activity_invitee_type,tms):
        #print("手机号": mobile ,"班辅": tms, "个辅": nsb)
        print(f"手机号:{activity_introducer_type}",activity_invitee_type, tms)