import pytest
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()
@pytest.fixture(scope='session',autouse=True) #False
def session_fixturea():
    path="/sys/login"
    data = {"userName":"18634664122","password":"123456"}
    re_login=http.post(path,data)
    assert re_login["code"]==200
    print("登录成功")
    CommonData.token=re_login["object"]["token"]
    yield
    path="/sys/logout"
    re_logout = http.post(path)
    assert re_logout["code"] == 200
    print("退出登录")



