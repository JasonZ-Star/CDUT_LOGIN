# -*- coding: utf-8 -*-
import get_cookies
# 请确保安装了以下依赖包：
# - requests
# - pycryptodome

if __name__ == '__main__':
    username = input("请输入你的学号：")
    password = input("请输入你的密码：",)
    cookies = get_cookies.get_cookies(username, password)



