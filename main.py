# -*- coding: utf-8 -*-
import json

from cookies_tools import get_cookies, login_with_cookies
from tools import get_transcript

# 请确保安装了以下依赖包：
# - requests
# - pycryptodome

if __name__ == '__main__':
    cookies = get_cookies.get_cookies_statue()
    login = login_with_cookies.login(cookies)
    if login is not None:
        cookies = json.loads(open("K:\\Code_Files\\LOGIN\\data\\data.json", "r").read())
    get_transcript.get_transcript(cookies)

