import requests
import json
from common.commonData import CommonData
class HttpUtil():
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':"application/json;charset=UTF-8"}
    def post(self,path,data=None):
        # proxies = {'http': 'http://localhost:8888'}  # 代理
        proxies=CommonData.proxies
        # headers={}
        # headers["Content-Type"]="application/json;charset=UTF-8"
        if CommonData.token is not None:
            self.headers["token"]=CommonData.token
        host=CommonData.host
        data=json.dumps(data)  #字典转换成json
        re_login=self.http.post(url=host+path,# http -->requests
                         proxies=proxies,
                         data=data,
                         headers=self.headers)
        assert re_login.status_code==200
        re_json=json.loads(re_login.text)  #json转换成字典
        return re_json


