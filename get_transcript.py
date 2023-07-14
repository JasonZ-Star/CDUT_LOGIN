import requests
from bs4 import BeautifulSoup
from collections import defaultdict

url = "https://jw.cdut.edu.cn/jsxsd/kscj/cjcx_list"

def get_transcript(cookies):
    # 发送HTTP请求并获取网页内容
    response = requests.get(url, cookies=cookies)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')  # 找到table元素

    # 获取表格的列头
    header = [col.get_text(strip=True) for col in table.find('tr').find_all('th')]

    # 获取表格的数据行
    data_array = [[col.get_text(strip=True) for col in row.find_all('td')] for row in table.find_all('tr')[1:]]

    # 创建存储键值对的字典
    transcript_dict = defaultdict(list)
    for row in data_array:
        col4, col5 =  row[3], row[4]
        key = row[1]
        transcript_dict[key].append([col4, col5])

    print(dict(transcript_dict))
    # 提取第一列、第四列和第五列的数据
