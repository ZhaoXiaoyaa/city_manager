from conftest import http
from common.commonData import CommonData
import allure
@allure.feature("请求获取用户详情")
class Test_loadUserInfo():
    @allure.story("成功获取用户详情")
    def loadUserInfo(self):
        data = {"id": CommonData.add_user_id}
        re_login = http.post("/user/loadUserInfo", data)
        assert re_login['code'] == 200
        assert re_login['msg'] == "操作成功"
        assert re_login["object"]["userName"] == CommonData.userName