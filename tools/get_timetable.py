import requests
from bs4 import BeautifulSoup

url = "https://jw.cdut.edu.cn/jsxsd/xskb/xskb_list.do"


def get_timetable(cookies):
    # 发送GET请求获取网页内容
    response = requests.get(url, cookies = cookies)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    courses = soup.find_all('div', class_name='kbcontent')

    print(courses)
    for course in courses:
        # 课程名称
        name = course.find('font').text

        # 教师
        teacher = course.find('font', title='教师').text

        # 教室
        classroom = course.find('font', title='教室').text

        # 周次和节次
        times = course.find('font', title='周次(节次)').text
        times = times.strip('()').split('-')

        # 其他信息......
