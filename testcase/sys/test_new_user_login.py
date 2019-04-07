from conftest import http
from common.commonData import CommonData
import allure
@allure.feature("新用户登录")
class Test_newuser_login():
    @allure.story("新用户登录成功")
    def login(self):
        data = {"userName": CommonData.userName,
                "password": "123456"}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 200
        assert re_login['msg'] == "操作成功"
        # assert re_login['object']['userId']==117
        print("登录成功")
        CommonData.add_user_id = re_login['object']['userId']