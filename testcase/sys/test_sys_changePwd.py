import pytest
from conftest import http
from common.commonData import CommonData
import allure
@allure.feature("修改密码")
class Test_changePwd():
    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("resetPwd")
    def test_changePwd_success(self):
        data = {"userId": 117,
                "userName": CommonData.mobile,
                "oldPwd":"123456",
                "password":"111111"
                }
        chang_pwd = http.post("/sys/changePwd", data)
        assert chang_pwd['code'] == 200
        assert chang_pwd['msg'] == "操作成功"
        print("成功修改密码")


    @pytest.fixture
    def resetPwd(self):
        yield
        data = {"userId": 117,
                "userName": CommonData.mobile,
	            "oldPwd": "111111",
	            "password": "123456"
                }
        change_pwd = http.post("/sys/changePwd", data)
        assert change_pwd['code'] == 200
        assert change_pwd['msg'] == "操作成功"
        print("恢复密码")

    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("resetPwd")
    def test_changePwd_id_null(self):
        data = {
                "userName": CommonData.mobile,
                "oldPwd": "123456",
                "password": "111111"
                }
        change_pwd = http.post("/sys/changePwd", data)
        assert change_pwd['code'] == 200
        assert change_pwd['msg'] == "操作成功"
        print("成功修改密码")

    @allure.story("修改密码失败")
    def test_changePwd_uname_empty(self):
        data = {"userId": 117,
                "userName": "",
                "oldPwd": "123456",
                "password": "111111"
                }
        change_pwd = http.post("/sys/changePwd", data)
        assert change_pwd['code'] == 411
        assert change_pwd['msg'] == "旧密码错误"
        print("用户名为空，修改密码失败")

