from collections import defaultdict

import requests
from bs4 import BeautifulSoup

stuId = input("请输入学号：")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "null",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"
}

url = "http://rpsjw.cdut.edu.cn/qzbb/reportJsp/showReport.jsp"
params = {
    "rpx": "/148656-XSCJDXSD.rpx"
}
data = {
    "selShowType": "all",
    "kclx": "0",
    "xsxh": stuId
}
response = requests.post(url, headers=headers, params=params, data=data, verify=False)

