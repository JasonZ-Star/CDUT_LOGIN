# -*- coding: utf-8 -*-
import json
import get_timetable
import get_transcript

# 请确保安装了以下依赖包：
# - requests
# - pycryptodome

if __name__ == '__main__':
    # cookies = get_cookies.get_cookies_statue()
    # login = login_with_cookies.login(cookies)
    cookies = json.loads(open("data/data.json", "r").read())
    get_transcript.get_transcript(cookies)

