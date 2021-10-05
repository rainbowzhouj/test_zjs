import datetime

import pytest

from api.employee import Employee


class TestEmployee:

    def setup(self):
        self.employee = Employee()


    def test_update(self):
        name="auto_test"+ str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        print(self.employee.update("38", "shrzy143620_daizilu", name, "3578"))

    @pytest.mark.parametrize("departmentName",[["终端赋能"],[""]])
    @pytest.mark.parametrize("employeeCode",[["007"],[""]])
    @pytest.mark.parametrize("mobile", [["13918097839"], [""]])
    @pytest.mark.parametrize("name", [["于俊"], [""]])
    @pytest.mark.parametrize("status", [["1"], ["2"],["4"], ["5"]])
    def test_find(self,departmentName,employeeCode,mobile,name,status):
        departmentName = ''.join(departmentName)
        employeeCode= ''.join(employeeCode)
        mobile = ''.join(mobile)
        name = ''.join(name)
        status = ''.join(status)
        r=self.employee.find(departmentname=departmentName
                                 ,employeeCode=employeeCode,mobile=mobile,name=name,status=status)
        assert r.json()["code"] == "200"
        #assert r.json()["data"][]
        """
        ,mobile,name,status
        ,mobile=mobile,name=name,status=status
        "name": "刘腾龙",可搜索姓名
        "departmentName": "中山八海星",可搜索部门
        之后此response里该字段的key值将改为parentNames，变更原因：客户要求所属部门全展示
        "sysAccount": "0",代表是否开通账户，boolean 0代表否未激活，1代表是激活
        "employeeCode": "ZY198345",代表工号，可搜索工号
        "status": "2",代表企微状态，可筛选状态
        "mobile": "13538132208",可筛选手机号
        
        """