import json
import os
import rsa_encryption
import pprint
import requests
import http_information.constants


def get_cookies_statue():
    # 检查data.json文件是否存在
    file_path = "data/data.json"
    if os.path.exists(file_path):
        flag = input("cookies存在，是否需要更新cookies?(Y/N)：\n")
        flag = flag.upper()
        if flag == "Y":
            return get_cookies()
        elif flag == "N":
            print("\n你的cookies为：")
            pprint.pprint(json.load(open("data/data.json", "r")))
            return json.load(open("data/data.json", "r"))
    else:
        print("文件或cookie不存在，正在创建，结束时创建或写入文件")
        return get_cookies()


def get_cookies():
    file_path = "data/data.json"
    username = input("请输入你的学号：\n")
    password = input("请输入你的密码：\n", )
    password_encrypt = rsa_encryption.encrypt_password(password)
    if os.path.exists(file_path):
        os.remove(file_path)
    # 1.获取登录页面
    # 1.1.构造请求头
    headers = http_information.constants.get_headers()
    # CAS登录验证URL
    cas_login_url = http_information.constants.get_login_url()

    # 1.2创建session对象，获取登录页面的cookies
    se = requests.session()

    # 使用session对象发送get请求，获取登录页面的隐藏参数execution
    response1 = se.get(cas_login_url, headers=headers)
    login_page = response1.text
    execution_start = login_page.find('name="execution" value="') + len('name="execution" value="')
    execution_end = login_page.find('"', execution_start)
    execution = login_page[execution_start:execution_end]

    # 2.提交登录表单（用户名、密码、隐藏参数execution以及params）
    payload = http_information.constants.get_payload(username, password_encrypt, execution)
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
            print("登录成功！")
            # 2.4将cookies保存到文件中
            with open("data/data.json", "w") as file:
                json.dump(requests.utils.dict_from_cookiejar(se.cookies), file)
            print("\n你的新cookies为：\n")
            pprint.pprint(json.load(open("data/data.json", "r")))
            return json.load(open("data/data.json", "r"))
        else:
            print("确认登录失败！")
            print("请清空data/data.json文件中的内容，重新运行程序！")
            return None
    else:
        print("登录失败！")
        if response.status_code == 401:
            print("用户名或密码错误！")
        elif response.status_code == 500:
            print("请清空data/data.json文件中的内容，重新运行程序！")
        return None
