# -*- coding: utf-8 -*-
import json
import numpy as np
import pandas as pd
from prettytable import PrettyTable

import cookies_tools
from cookies_tools import get_cookies, login_with_cookies

# 请确保安装了以下依赖包：
# - requests
# - pycryptodome

if __name__ == '__main__':
    # cookies = get_cookies.get_cookies_statue()
    # login = login_with_cookies.login(cookies)
    cookies = json.loads(open("data/data.json", "r").read())
    import requests
    from bs4 import BeautifulSoup

    url = "https://jw.cdut.edu.cn/jsxsd/kscj/cjcx_list?kksj=2022-2023-1"

    # 发送HTTP请求并获取网页内容
    response = requests.get(url,cookies=cookies)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')  # 找到table元素

    pt = PrettyTable()

    # 获取表格的列头
    header_row = table.find('tr')
    header_cols = header_row.find_all('th')
    header = [col.get_text(strip=True) for col in header_cols]

    # 添加表格的列头
    pt.field_names = header

    # 获取表格的数据行
    data_rows = table.find_all('tr')[1:]  # 排除第一行（表头）

    data_array = []
    # 添加表格的数据行
    for row in data_rows:
        cols = row.find_all('td')
        row_data = [col.get_text(strip=True) for col in cols]
        data_array.append(row_data)
    # 输出表格
    data = np.array(data_array)
    df = pd.DataFrame(data)
    # 创建存储键值对的字典
    key_value_dict = {}

    table = PrettyTable()
    # 提取第四列和第五列的数据，并转化为键值对存储在字典中
    for row in data:
        key = row[3]  # 第四列作为键
        value = row[4]  # 第五列作为值
        key_value_dict[key] = value
        table.add_row([key, value])

    table.field_names = ["课程名称", "成绩"]

    table.align["课程名称"] = "l"
    table.align["成绩"] = "l"

    # 提取第四列和第五列的数据，并添加到表格中
    # 打印表格
    print(table)
