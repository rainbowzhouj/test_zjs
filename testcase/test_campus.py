from api.campus import Campus


class TestAccount:

    def setup(self):
        self.campus = Campus()

    def test_find(self):
        print(self.campus.find("256"))

    def test_find_list(self):
        self.campus.find_list("1","10")

    def test_create(self):
        self.campus.create()

    def test_update(self):
        self.campus.update()

    def test_delete(self):
        self.test_delete()

    def test_employlist(self):
        self.test_employlist()

