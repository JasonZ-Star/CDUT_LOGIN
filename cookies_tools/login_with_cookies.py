import requests
import http_information.constants


def login(cookies):
    index = requests.get(url=http_information.constants.get_login_url(), cookies=cookies)
    if index.status_code == 200:
        print("登录成功")
        return index.text
    else:
        print("登录失败")
        return None
