import json
import os
import rsa_encryption
import pprint
import requests



def get_cookies(username, password):
    password_encrypt = rsa_encryption.encrypt_password(password)
    # 检查data.json文件是否存在
    file_path = "data/data.json"
    if os.path.exists(file_path):
        if os.path.getsize(file_path) == 0:  # 文件为空
            cookies_not_exist = True
            print("不存在cookies文件，将创建cookies文件")
        else:
            cookies_not_exist = False
            flag = input("是否需要更新cookies?(y/n)")
            if flag == "y":
                cookies_not_exist = True
            elif flag == "n":
                cookies_not_exist = False
            else:
                print("输入错误，将不更新cookies")
                cookies_not_exist = False
    else:
        cookies_not_exist = True
    if cookies_not_exist:
        print("文件或cookie不存在，正在创建，结束时创建或写入文件")
        # 1.获取登录页面
        # 1.1.构造请求头
        headers = {
            "authority": "cas.paas.cdut.edu.cn",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://cas.paas.cdut.edu.cn",
            "referer": "https://cas.paas.cdut.edu.cn/cas/login?service=http^%^3A^%^2F^%^2Fjw.cdut.edu.cn^%^2Fsso^%^2Flogin.jsp^%^3FtargetUrl^%^3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA^%^3D^%^3D",
            "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                          "Safari/537.36 Edg/114.0.1823.67"
        }
        # CAS登录验证URL
        cas_login_url = "https://cas.paas.cdut.edu.cn/cas/login?service=http%3A%2F%2Fjw.cdut.edu.cn%2Fsso%2Flogin.jsp%3FtargetUrl%3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA%3D%3D"

        # 1.2创建session对象，获取登录页面的cookies
        se = requests.session()

        # 使用session对象发送get请求，获取登录页面的隐藏参数execution
        response1 = se.get(cas_login_url, headers=headers)
        login_page = response1.text
        execution_start = login_page.find('name="execution" value="') + len('name="execution" value="')
        execution_end = login_page.find('"', execution_start)
        execution = login_page[execution_start:execution_end]

        # 2.提交登录表单（用户名、密码、隐藏参数execution以及params）
        payload = {
            "username": username,
            "password": password_encrypt,
            "currentMenu": "1",
            "failN": "1",
            "execution": execution,
            "_eventId": "submit",
            'submit': 'Login1'
        }
        params = {
            # 为重定向后的url添加参数
            "service": "http^%^3A^%^2F^%^2Fjw.cdut.edu.cn^%^2Fsso^%^2Flogin.jsp^%^3FtargetUrl"
                       "^%^3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA^%^3D^%^3D"
        }

        # 2.1使用session对象发送post请求，提交登录表单，获取响应，不允许重定向以获取响应头中的Location
        response = se.post(cas_login_url, data=payload, params=params, allow_redirects=False)

        # 2.2判断响应状态码是否为302，如果是则说明登录成功，否则说明登录失败
        if response.status_code == 302:
            # 访问响应头中带有ticket的Location，获取重定向后的url
            url_with_ticket = response.headers["Location"]
            # print("url_with_ticket:"+ url_with_ticket)
            confirm_response = se.get(url_with_ticket, headers=headers)
            print(confirm_response.status_code)

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

    else:
        print("文件存在，正在读取")
        print("读取成功,你的原cookies为：")
        with open("data/data.json", "r") as file:
            cookies = json.load(file)
        pprint.pprint(cookies)
        return cookies
