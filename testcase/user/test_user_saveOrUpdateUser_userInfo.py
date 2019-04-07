# import random
# from conftest import http
# from common.commonData import CommonData
# class Test_saveOrUpdateUser():
#     def test_saveOrUpdateUser_success(self):
#         CommonData.nickName = str(random.randint(10000000, 100000000))
#         CommonData.userName='159'+CommonData.nickName
#         data = {"nickName": CommonData.nickName,
#                 "userName":CommonData.userName ,
#                 "telNo": "",
#                 "email": "",
#                 "address": "",
#                 "roleIds": "1",
#                 "regionId": 1,
#                 "regionLevel": 1
#                 }
#         add_user = http.post("/user/saveOrUpdateUser", data)
#         # assert add_user['code'] == 302
#         # assert add_user['msg']=="操作成功"
#     def test_login(self):
#         data = {"userName": CommonData.userName,
#                 "password": "123456"}
#         re_login = http.post("/sys/login", data)
#         assert re_login['code']==200
#         assert re_login['msg']=="操作成功"
#         # assert re_login['object']['userId']==117
#         print("登录成功")
#         CommonData.add_user_id=re_login['object']['userId']
#
#     def test_loadUserInfo(self):
#         data = {"id": CommonData.add_user_id}
#         re_login = http.post("/user/loadUserInfo", data)
#         assert re_login['code'] == 200
#         assert re_login['msg'] == "操作成功"
#         assert re_login["object"]["userName"] == CommonData.userName