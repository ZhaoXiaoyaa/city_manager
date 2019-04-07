import pytest
from conftest import http
from common.commonData import CommonData
import random
from testcase.user.test_user_loadUserInfo import Test_loadUserInfo
from testcase.sys.test_new_user_login import Test_newuser_login
from testcase.user.test_user_loadUserList import Test_loadUserList
import allure
@allure.feature("添加用户信息")
class Test_saveOrUpdateUser():
    @allure.story("成功添加用户信息")
    @pytest.mark.newuser
    def test_saveOrUpdateUser_success(self):
        CommonData.nickName=str(random.randint(10000000,100000000))
        CommonData.userName='159'+CommonData.nickName
        data = {"nickName": CommonData.nickName,
                "userName":CommonData.userName,
                "telNo": "",
                "email": "",
                "address": "",
                "roleIds": "1",
                "regionId": 1,
                "regionLevel": 1
                }
        add_user = http.post("/user/saveOrUpdateUser", data)
        print("成功添加用户信息")
        Test_newuser_login().login()
        Test_loadUserList().loadUserList()
        Test_loadUserInfo().loadUserInfo()
