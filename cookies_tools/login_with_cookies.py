import requests
import http_information.constants


def login(cookies):
    if cookies is None:
        print("登录失败")
        return None
    else:
        index = requests.get(url=http_information.constants.get_login_url(), cookies=cookies)
        if index.status_code == 200:
            print("---------------------------------------")
            print("\t\t\t\t登录成功！！")
            print("---------------------------------------")
            return index.text

