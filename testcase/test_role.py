from api.role import Role


class TestAccount:

    def setup(self):
        self.role = Role()

    def test_find_Role(self):
        print(self.role.find_RoleByType("1"))

    def test_find_Operate(self):
        print(self.role.find_OperateRoles("1"))

    def test_create_Operate(self):
        print(self.role.create("auto20210607"))

    def test_update_Operate(self):
        print(self.role.update("254","auto20210607"))

    def test_list_Intree(self):
        print(self.role.get_tree())

    def test_list_Operate_Default(self):
        print(self.role.get_list())

    def test_delete(self):
        print(self.role.delete("253","1"))

    def test_create_Data(self):
        self.role.create_datarole("autodatarole")

    def test_updata_Data(self):
        self.role.update_datarole("autodatarole2021","256")

    def test_find_Data(self):
        self.role.find_datarole("autodatarole","1","10")

    def test_find_One_Data(self):
        self.role.find_one_datarole("256")

    def test_create_DataRole(self):
        self.role.create_DataRolePermission("")

    def test_update_DataRole(self):
        self.role.update_DataRolePermission("")
