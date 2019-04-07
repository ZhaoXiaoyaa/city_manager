from conftest import http
from common.commonData import CommonData
from testcase.sys.test_new_user_login import Test_newuser_login
import allure
@allure.feature("查看用户清单")
class Test_loadUserList():
    @allure.story("成功查看用户清单")
    def loadUserList(self):
        data = {"pageCurrent": 1,"pageSize": 10,"nickName": "","userName": "","regionId": 1}
        loadUserList = http.post("/user/loadUserList", data)
        assert loadUserList['code'] == 200
        assert loadUserList['msg'] == "操作成功"
        assert loadUserList["object"]["list"][0]["id"]==CommonData.add_user_id
        assert loadUserList["object"]["list"][0]["userName"]==CommonData.userName