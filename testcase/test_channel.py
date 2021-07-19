import datetime

import allure
from jsonpath import jsonpath

from api.channel import Channel



@allure.feature("拼课团功能")
class TestChannel():

    def setup_class(self):
        self.channel = Channel()

    @allure.story('查看所有渠道')
    def test_channel_list_group_buy_event(self):
        # 查看所有渠道
        r = self.channel.list_group_buy_event()
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$..name")[0]
        print(a)
        #assert "".join(a) == "线上-微信"

    @allure.story('添加渠道')
    def test_channel_add_group_buy_event(self):
        # 添加渠道
        channel_name = "auto" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.channel.add_group_buy_event(channel_name)
        # for item in range(1,101):
        #     channel_name = "auto" + str(item)
        #     r = self.channel.add_group_buy_event(channel_name)
        assert r.json()['code'] == '0'
        r1 = self.channel.list_group_buy_event()
        a = jsonpath(r1.json(), f"$..name")[-1]
        assert "".join(a) == channel_name

    # @allure.story('添加多个渠道')
    # def test_channel_adds_group_buy_event(self):
    #     for item in range(1, 101):
    #         channel_name = "auto" + str(item)
    #         r = self.channel.add_group_buy_event(channel_name)
    #     assert r.json()['code'] == '0'

    @allure.story('更新渠道')
    def test_channel_update_group_buy_event(self):
        # 更新渠道
        r = self.channel.list_group_buy_event()
        channel_name = "auto" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        channel_id = r.json()['data'][-1]['id']
        r = self.channel.update_group_buy_event(channel_name=channel_name, channel_id = channel_id)
        r1 = self.channel.list_group_buy_event()
        a = jsonpath(r1.json(), f"$..name")[-1]
        assert "".join(a) == channel_name

    @allure.story('删除渠道')
    def test_channel_delete_group_buy_event(self):
        r = self.channel.list_group_buy_event()
        channel_id = r.json()['data'][-1]['id']
        r = self.channel.delete_group_buy_event(channel_id)
        assert r.json()['code'] == '0'

    @allure.story('添加区域')
    def test_area_add(self):
        area_name = "auto"
        r = self.channel.area_add(area_name=area_name)
        assert r.json()['code'] == '0'

    @allure.story('更新区域')
    def test_area_update(self):
        r = self.channel.organizations_list()
        area_name = "auto" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        area_id = r.json()['data'][-1]['id']
        r = self.channel.area_update(area_name=area_name, area_id=area_id)
        assert r.json()['code'] == '0'

    @allure.story('删除区域')
    def test_area_delete(self):
        r = self.channel.organizations_list()
        area_id = r.json()['data'][-1]['id']
        r = self.channel.area_delete(area_id)
        assert r.json()['code'] == '0'

    """
    组织下有区域，区域下有校区，均可新建与删除
    """

    @allure.story('查看所有组织')
    def test_organizations_list(self):
        # 查看所有校区
        r = self.channel.organizations_list()
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$..data[1].name")
        # print(a)
        assert "".join(a) == "广州"

    @allure.story('查看所有校区')
    def test_store_list(self):
        # 查看所有校区
        r = self.channel.store_list()
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$..data[0].name")
        #print(a)
        assert "".join(a) == "南山巧问辅导班"

    @allure.story('添加校区')
    def test_store_add(self):
        store_name = "auto"
        r = self.channel.store_add(store_name=store_name)
        assert r.json()['code'] == '0'

    @allure.story('更新校区')
    def test_store_update(self):
        r = self.channel.organizations_list()
        store_name = "auto" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        store_id1 = r.json()['data'][-1]['stores'][0]['id']
        # print(store_id1)
        # store_id = jsonpath(r.json(), f"$..stores[0].id")[-1]
        r = self.channel.store_update(store_id=store_id1, store_name=store_name)
        assert r.json()['code'] == '0'

    @allure.story('删除校区')
    def test_store_delete(self):
        r = self.channel.organizations_list()
        # store_id = r.json()['data'][-1]['stores'][0]['storeName']
        # store_id2 = r.json()['data'][-1]['stores'][-1]['storeName']
        # print(store_id2)
        # print(store_id)
        # a = jsonpath(r.json(), f"$..stores[0].storeName")[-1]
        # b = jsonpath(r.json(), f"$..stores[0].id")[-1]
        # print(a)
        # print(b)
        store_id = jsonpath(r.json(), f"$..stores[0].id")[-1]
        # print(store_id)
        r = self.channel.store_delete(store_id)
        assert r.json()['code'] == '0'

