import requests
# import urllib3   #禁用证书警告
# urllib3.disable_warnings()
# res=requests.post("https://testerhome.com/account/sign_in",{"username":"admin","password":"123456"},verify=False)   #如果是https请求加verify=False，移除SSL认证print(res.json())


class Test:

    def __init__(self):
        self.host="http://106.14.37.200:8000/"
        self.token=""
        self.headers={"Content-Type": "application/json"}

    def login(self,username,password):
        body={"username":username,"password":password}
        print("api-token-auth/",body)
        res=requests.post(f'{self.host}api-token-auth/',body)
        self.token="Token "+res.json()['token']
        print(f"返回：{res.json()}")

    def get(self,url,headers=None):
        if headers:
            self.headers.update(headers)
        resp=requests.get(self.host+url,headers={"authorization":self.token})
        print(resp.json())
        return resp.json()

if __name__ == '__main__':
    t =Test()
    t.login("admin","123456")
    t.get("api/book/?book_name=&format=json")


# response = requests.post("http://106.14.37.200:8000/api-token-auth/",
#                          {"username": "admin", "password": "123456"})
# print(response.json())
# authorization = response.json()['token']
# res2=requests.get("http://106.14.37.200:8000/api/book/?book_name=&format=json", headers={"authorization":"Token "+authorization})
# print(res2.json())

# 

# token="Token "+response.json()['token']
# response2=requests.get("http://106.14.37.200:8000/api/book/?book_name=&format=json",headers={"authorization":token})
# print(response2.json())
