# <center>CDUT_LOGIN：成都理工大学教务处模拟登陆</center>
通过Python（目前只写了这一种）模拟登陆教务处  
## Requirements
请确保安装了以下依赖包：
requests库, pycryptodome库, 测试版本Python3.11, 其他版本不保证能够运行
## Brief Introduction
### 目前包含三个文件：  
get_cookies.py: 用于登陆获取cookies  
rsa_encryption.py：用于将用户输入的密码转换为服务器可以识别的加密密码（注意如果pycryptodome库无法正常使用，请自行搜索解决）  
main.py：主程序，获得并存储cookie在data/data.json中


