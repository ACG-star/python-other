"""
@File    :   homework307.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Description
------------          --------   --------    -----------
2023/3/7 0007 13:01  FuGui      1.0         归属地接口
"""

# https://www.ip138.com/sj/
# https://www.ip138.com/mobile.asp?     mobile=18437797131  &   action=mobile
# 常见字符的ASCII码值如下：空格的ASCII码值为32；
# 数字0到9的ASCII码值分别为48到57；
# 大写字母“A”到“Z”的ASCII码值分别为65到90；
# 小写字母“a”到“z”的ASCII码值分别为97到到122。
# div class=table
#     table
#          tbody
#                tr
#                   td----------------------列名
#                   td
#                       a(只取第一个)------电话、运营商、区号、邮编
#                       span----------------归属地
#


import requests
from urllib import parse
from bs4 import BeautifulSoup
import re


def download_img():
    school_url = 'https://www.hait.edu.cn/'
    response = requests.get(school_url).content.decode('utf-8')
    # print(response)
    bs_school = BeautifulSoup(response, 'html5lib')
    img_urlList = bs_school.select('.news_pic')  # 列表格式
    # print(img_urlList)
    for img_url in img_urlList:
        rule = re.compile('src=(.*)')
        imgsrc = re.search(rule, str(img_url))
        url = imgsrc.group()[5:-3]  # /__local/1/4B/21/AABA170FCEA0EE9B7266B41F563_1B7ED923_25E98.jpg
        file_name = url.split('/')[-1:][0]
        result_jpg = school_url + url
        img_path = "./image" + file_name
        with open(img_path, 'wb') as f:
            f.write(requests.get(result_jpg).content)
    return 1


def get_info(source):
    s = BeautifulSoup(source, "lxml")  # html5
    for row in s.select(".table>tr"):
        pass  # 待开发…………………………


def get_source(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42"
    }
    try:
        r = requests.get(url, headers=head)
        r.encoding = r.apparent_encoding  # 定义编码格式
        r.raise_for_status()  # 返回码校验
        return r.text
    except Exception as e:
        print(e)


def get_url(url, p_number):
    parm = {
        "mobile": p_number,
        "action": "mobile"
    }
    pn = parse.urlencode(parm)  # 将键值对构建为网址参数(&参数由连接)
    # print(pn)  # mobile=111&action=mobile
    url = url + pn
    return url


def judge_re_number():
    n = input("请输入一个手机号：")
    if re.match(r'1[3,4, 5,7,8,9]\d{9}', n) and len(n) == 11:
        print("您输入的的手机号码是：{}".format(n))
        # 中国联通：
        # 130，131，132，155，156，185，186，145，176
        if re.match(r'13[0,1,2]\d{8}', n) or \
                re.match(r"15[5,6]\d{8}", n) or \
                re.match(r"18[5,6]\d{8}", n) or \
                re.match(r"145\d{8}", n) or \
                re.match(r"176\d{8}", n):
            print("该号码属于：中国联通")
        # 中国移动
        # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
        # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
        elif re.match(r"13[4,5,6,7,8,9]\d{8}", n) or \
                re.match(r"147\d{8}|178\d{8}", n) or \
                re.match(r"15[0,1,2,7,8,9]\d{8}", n) or \
                re.match(r"18[2,3,4,7,8]\d{8}", n):
            print("该号码属于：中国移动")
        else:
            # 中国电信
            # 133,153,189
            print("该号码属于：中国电信")
    else:
        print("请输入正确的手机号")
        return judge_re_number()
    return n


# 仅能从外在格式判断是否合法，只能保证时11位数字，是否为号码未能判断；例：000 0000 0000也会通过
def judge_p_number():
    p_number = input("请输入待查询的11位手机号码：")
    for pn in p_number:  # 使用ASCII码校验字符，使用函数ord
        if 47 < ord(pn) <= 57:  # 新写法，可以不使用and
            continue
        else:
            print("号码格式错误请重新输入！！")
            return judge_p_number()
    if len(p_number) != 11:
        print("号码格式错误请重新输入！！")
        return judge_p_number()
    else:
        return p_number


if __name__ == '__main__':
    # 号码归属地接口
    p_n = judge_re_number()  # # p_n = judge_p_number()
    u_url = get_url("https://www.ip138.com/mobile.asp?", p_n)
    # print(u_url)
    print(get_source(u_url))
    # # source = get_source(u_url)


    # 学校官网图片
    # download_img()
