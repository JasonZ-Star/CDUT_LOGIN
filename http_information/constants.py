# 请求头信息
def get_headers():
    return {
        "authority": "cas.paas.cdut.edu.cn",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://cas.paas.cdut.edu.cn",
        "referer": "https://cas.paas.cdut.edu.cn/cas/login?service=http^%^3A^%^2F^%^2Fjw.cdut.edu.cn^%^2Fsso^%^2Flogin"
                   ".jsp^%^3FtargetUrl^%^3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA"
                   "^%^3D^%^3D",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                      "Safari/537.36 Edg/114.0.1823.67"
    }


def get_payload(username, password_encrypt, execution):
    return {
        "username": username,
        "password": password_encrypt,
        "currentMenu": "1",
        "failN": "1",
        "execution": execution,
        "_eventId": "submit",
        'submit': 'Login1'
    }


def get_params():
    return {
        "service": "http^%^3A^%^2F^%^2Fjw.cdut.edu.cn^%^2Fsso^%^2Flogin.jsp^%^3FtargetUrl"
                   "^%^3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA^%^3D^%^3D"
    }


def get_cas_login_url():
    return "https://cas.paas.cdut.edu.cn/cas/login?service=http%3A%2F%2Fjw.cdut.edu.cn%2Fsso%2Flogin.jsp" \
           "%3FtargetUrl%3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA" \
           "%3D%3D"


def get_login_url():
    return "https://jw.cdut.edu.cn/jsxsd/framework/xsMainV.htmlx"