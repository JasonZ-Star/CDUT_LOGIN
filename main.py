# -*- coding: utf-8 -*-
import json
import os
import tempfile
import webbrowser



from cookies_tools import get_cookies, login_with_cookies
from cookies_tools.get_cookies import Login, get_cookies_statue
from tools import get_transcript
import pandas as pd
# 请确保安装了以下依赖包：
# - requests
# - pycryptodome

user_name = None

filepath = 'data/data.json'

if __name__ == '__main__':
    get_ck = Login()
    cookies = get_cookies_statue()
    login = login_with_cookies.login(cookies)
    if login is not None:
        cookies = json.loads(open(filepath, "r").read())
    transcript = get_transcript.get_transcript(cookies)
    df = pd.DataFrame(columns=['学期', '课程', '成绩'])

    # 将数据填充到DataFrame中
    for semester, courses in transcript.items():
        for course, score in courses:
        # 创建一个包含单个数据点的DataFrame
            new_data = pd.DataFrame({'学期': [semester], '课程': [course], '成绩': [score]})
            df = pd.concat([df,new_data], ignore_index=True)

    # # 显示DataFrame
    # print(df)

    # 计算成绩列的平均值
    average_score = pd.to_numeric(df['成绩'].replace('优', 95), errors='coerce').mean()

    average = pd.DataFrame({'学期': '平均成绩',
                            '课程': '',
                            '成绩': [format(average_score, '.3f')]
                            })

    df = pd.concat([df, average], ignore_index=True)
    # 显示更新后的DataFrame
    print(df)

    # 使用style功能设置数据居中显示
    styled_df = df.style.set_properties(**{'text-align': 'center'})
    if os.path.exists('transcript'):
        styled_df.to_excel('transcript/styled_table.xlsx', index=False)
    else:
        os.makedirs('transcript')
        styled_df.to_excel('transcript/styled_table.xlsx', index=False)
    # 将DataFrame转换为HTML格式，并设置对齐方式
    html_df = df.to_html(index=False, classes='mystyle')




    # CSS样式，设置表头居中和表格样式
    css_style = """
    <style>
        .mystyle {
            text-align: center;
            table-layout: fixed;
            width: 100%;
            border-collapse: collapse;
        }
        .mystyle th, .mystyle td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .mystyle th {
            background-color: #f2f2f2;
        }
        #semester_table th {
            text-align: center;
        }
    </style>
    """

    # 为每个学期添加单独的标注
    html_df = html_df.replace('<table ', '<table class="semester_table" ')

    # 将CSS样式和HTML内容合并
    full_html_content = f"<html><head>{css_style}</head><body>{html_df}</body></html>"

    # 将完整的HTML内容写入到文件
    with open("styled_table.html", "w") as file:
        file.write(full_html_content)

    # 创建一个临时文件
    temp_html_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)

    # 写入HTML内容到临时文件
    temp_html_file.write(full_html_content.encode('utf-8'))

    # 关闭文件
    temp_html_file.close()

    # 使用webbrowser打开临时文件
    webbrowser.open('file://' + temp_html_file.name)