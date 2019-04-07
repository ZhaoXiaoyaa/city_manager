from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("用户登录")

class Test_login():
    @allure.story("用户登录成功")
    def test_login_success(self):
        data = {"userName": CommonData.mobile,
                "password": "123456"}
        re_login = http.post("/sys/login", data)
        assert re_login['code']==200
        assert re_login['msg']=="操作成功"
        assert re_login['object']['userId']==117
        print("登录成功")

    @allure.story("密码错误")
    def test_login_pwd_wrong(self):
        data = {"userName": CommonData.mobile,
                "password": "12345678"}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 410
        assert re_login['msg'] == "用户名或密码错误"
        assert re_login['object'] == None
        print("密码错误")

    @allure.story("用户不存在")
    def test_login_uname_not_exist(self):
        data = {"userName": "18634664121",
                "password": "123456"}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 301
        assert re_login['msg'] == "用户不存在"
        assert re_login['object'] == None
        print("用户不存在")

    @allure.story("用户名为空")
    def test_login_uname_empty(self):
        data = {"userName": "",
                "password": "123456"}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 301
        assert re_login['msg'] == "用户不存在"
        assert re_login['object'] == None
        print("用户名为空")

    @allure.story("不输入用户名")
    def test_login_uname_null(self):
        data = {"password": "123456"}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 301
        assert re_login['msg'] == "用户不存在"
        assert re_login['object'] == None
        print("不输入用户名")

    @allure.story("密码为空")
    def test_login_pwd_empty(self):
        data = {"userName": CommonData.mobile,
                "password": ""}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 410
        assert re_login['msg'] == "用户名或密码错误"
        assert re_login['object'] == None
        print("密码为空")

    @allure.story("不输入密码")
    def test_login_pwd_null(self):
        data = {"userName": CommonData.mobile}
        re_login = http.post("/sys/login", data)
        assert re_login['code'] == 410
        assert re_login['msg'] == "用户名或密码错误"
        assert re_login['object'] == None
        print("不输入密码")

