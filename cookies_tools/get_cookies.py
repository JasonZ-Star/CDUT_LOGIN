import json
import os
import sys
from tools import rsa_encryption
import pprint
import requests
import http_information.constants


def get_cookies_statue():
    file_path = "data/data.json"
    flag = True
    while flag:
        # 检查data.json文件是否存在
        cookie_path = file_path
        if os.path.exists(cookie_path):
            flag = input("cookies存在，是否需要更新cookies?(Y/N)：\n")
            flag = flag.upper()
            if flag == 'Y' or flag == 'y':
                return Login().get_cookies()
            elif (flag == 'N' or flag == 'n'):
                # 检测文件是否为空
                if os.path.getsize(cookie_path) == 0:
                    print("---------------------------------------")
                    print("文件为空，重新获取cookie！")
                    print("---------------------------------------")
                    return Login().get_cookies()
                else:
                    json_data = json.load(open(cookie_path, "r"))
                    print("---------------------------------------")
                    print("\t\t\tcookies加载成功")
                    print("---------------------------------------")
                    return json_data
            else:
                print("---------------------------------------")
                print("\t\t\输入错误，请重新输入！")
                print("---------------------------------------")
                flag = True
        else:
            print("------------------------------------------------------------")
            print("文件或cookie不存在，正在创建，结束时创建或写入文件'data/data.json''")
            print("------------------------------------------------------------")
            return Login().get_cookies()


class Login:

    def __init__(self):
        self.cookies = None
        self.username = None
        self.file_path = "data/data.json"
        self.__password = None
        self.__password_encrypt = None

    def get_cookies(self):
        file_path = "data/data.json"
        # 设置登录信息
        self.set_userinfo()

        if os.path.exists(file_path):
            os.remove(file_path)
        # 1.获取登录页面
        # 1.1.构造请求头
        headers = http_information.constants.get_headers()
        # CAS登录验证URL
        cas_login_url = http_information.constants.get_cas_login_url()

        # 1.2创建session对象，获取登录页面的cookies
        se = requests.session()

        # 使用session对象发送get请求，获取登录页面的隐藏参数execution
        response1 = se.get(cas_login_url, headers=headers)
        login_page = response1.text
        execution_start = login_page.find('name="execution" value="') + len('name="execution" value="')
        execution_end = login_page.find('"', execution_start)
        execution = login_page[execution_start:execution_end]

        # 2.提交登录表单（用户名、密码、隐藏参数execution以及params）
        payload = http_information.constants.get_payload(self.username, self.__password_encrypt, execution)
        # 为重定向后的url添加参数
        params = http_information.constants.get_params()

        # 2.1使用session对象发送post请求，提交登录表单，获取响应，不允许重定向以获取响应头中的Location
        response = se.post(cas_login_url, data=payload, params=params, allow_redirects=False)

        # 2.2判断响应状态码是否为302，如果是则说明登录成功，否则说明登录失败
        if response.status_code == 302:
            # 访问响应头中带有ticket的Location，获取重定向后的url
            url_with_ticket = response.headers["Location"]
            # print("url_with_ticket:"+ url_with_ticket)
            confirm_response = se.get(url_with_ticket, headers=headers)

            # 2.3判断响应状态码是否为200，如果是则说明确认登录成功，否则说明确认登录失败
            if confirm_response.status_code == 200:
                print("--------")
                print("登录成功！")
                print("--------")
                self.cookies = se.cookies
                # 如果登录成功，将cookies保存到文件中
                # 如果cookies文件不存在 则创建文件
                if not os.path.exists(file_path):
                    with open(file_path, "w") as file:
                        json.dump(requests.utils.dict_from_cookiejar(self.cookies), file)
                else:
                    os.remove(file_path)
                    with open(file_path, "w") as file:
                        json.dump(requests.utils.dict_from_cookiejar(self.cookies), file)

                print("--------------------------------------")
                print("你的cookies已存于:'data\\data.json中'")
                print("--------------------------------------")
                # pprint.pprint(json.load(open(file_path, "r")))
                return json.load(open(file_path, "r"))
            else:
                print("------------------------------------------------------")
                print("确认登录失败！请清空data/data.json文件中的内容，重新运行程序！")
                print("------------------------------------------------------")
                return None
        else:
            if response.status_code == 401:
                print("------------------------")
                print("登录失败！用户名或密码错误！")
                print("------------------------")
            elif response.status_code == 500:
                print("-------------------------------------------")
                print("请清空data/data.json文件中的内容，重新运行程序！")
                print("-------------------------------------------")
            else:
                print("Http状态码为：", response.status_code)
            return None

    def set_userinfo(self):
        try_time1 = 0
        try_time2 = 0
        while try_time1 < 6:
            try_time1 = try_time1 + 1
            self.username = input("请输入你的学号：")
            if len(self.username) == 0 and try_time1 < 6:
                print("----------------------")
                print("账号不能为空，请重新输入！")
                print("----------------------")
            elif try_time1 == 6:
                print("输入错误次数过多，请重新运行程序！")
                sys.exit()
            else:
                break
        while try_time2 < 6:
            try_time2 = try_time2 + 1
            self.__password: str = input("请输入你的密码：")
            if len(self.__password) == 0 and try_time2 < 6:
                print("学号不能为空，请重新输入！")
            elif try_time2 == 6:
                print("输入错误次数过多，请重新运行程序！")
                sys.exit()
            else:
                break
        self.__password_encrypt = rsa_encryption.encrypt_password(self.__password)