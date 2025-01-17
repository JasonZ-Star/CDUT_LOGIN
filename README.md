# CDUT_LOGIN：成都理工大学教务处模拟登陆
## Introduction:
通过Python（目前只写了这一种）模拟登陆教务处并获取成绩单，当然既然都能够登陆了，选课也是可以操作的，可自行研究提交pr
如果可以的话，希望能够给个star，谢谢！
## Usage:
```text
请确保安装了requirements.txt中的所有库，运行以下命令安装
```
```shell
pip install -r requirements.txt
```

测试版本**Python3.12.8**, 其他版本不保证能够运行
## Brief Introduction:
#### 文件夹详解：  
#### cookies_tools: 主要是与cookies操作有关的文件
_get_cookies.py_: 用于登陆获取cookies  
_login_with_cookies.py_: 用获得的cookies登陆
#### http_information: 包含了Http请求时的一些常量，如请求头
_constants.py_: 包含headers，payload，等
#### tools: 包含了用于获取成绩以及课表的等工具
_get_timetable.py_ : 用于获取课程表  
_get_transcript.py_ : 用于获取课程成绩，以字典的形式返回  
_rsa_encryption.py_ : 用于将用户输入的密码转换为服务器可以识别的加密密码（注意如果pycryptodome库无法正常使用，请自行搜索解决）  
#### transcript: 保存获取到的成绩为excel文件
### Main Program:
_main.py_: 位于根目录下，主程序，获得并存储cookie在data/data.json中


