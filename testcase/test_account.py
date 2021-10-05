import datetime

import pytest

from api.account import Account


class TestAccount:

    def setup(self):
        self.account = Account()

    def test_create(self):
        print(self.account.create("shrzy143620_daizilu", "auto_test", "3578"))

    def test_update(self):
        name="auto_test"+ str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        print(self.account.update("38", "shrzy143620_daizilu", name, "3578"))

    def test_find(self):
        print(self.account.find("戴子",""))

    def test_findone(self):
        print(self.account.find_one("10"))

    @pytest.mark.parametrize('status', ['2', '1'])
    def test_start_account(self,status):
        print(self.account.start_account(38, status))