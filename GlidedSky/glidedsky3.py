'''
    爬虫-IP屏蔽1
'''

import requests
from lxml import etree
import sys
import re
sys.setrecursionlimit(1200)#修改递归最大次数,python默认为1000次

def open_url(i, number) :
    html = etree.HTML(getPro(i).text)
    print('-----%s',i)
    if html != None:
        number_list = html.xpath('//div[@class="col-md-1"]/text()')
        if number_list:
            num_list = [int(x.replace(' ', '')) for x in number_list]
            number += sum(num_list)
            # print(number)
            # num_end = html.xpath('//a[@rel="next"]/@href')
            # if num_end:
            if i <= 1000:
                print(number)
                return open_url(i+1, number)
            else:
                return number
    else:
        open_url(i, number)

def getPro(num):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Cookie': '_ga=GA1.2.1883545492.1573551638; _gid=GA1.2.853505022.1573551638; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573551638,1573609456,1573693814; footprints=eyJpdiI6InFhdHRiSEVOa1lnWXc5UUxVclkyN3c9PSIsInZhbHVlIjoiTTQ5VlwvNVwvTUhBclc0VFNtRlllQmpLWDN4SCtyXC9zNGxMSWNmVVBQM2hISnJIUHZmXC9sZFltOFJ3UXJDZUY4YzciLCJtYWMiOiJkYmYyNDc3ZDc5OTk2NWM5OTgwOWViOTY3YzBhM2Y3NTY4MjhlOGJlNTY0YjgxODk4ODc5NGI1MzdhYzc1OGQ0In0%3D; _gat_gtag_UA_75859356_3=1; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1573694532; XSRF-TOKEN=eyJpdiI6IkxoblpwQUYxcU9FUkgwSGtObXZWaHc9PSIsInZhbHVlIjoiSCtyM1wvWWcwVnRKSXVwQldcLzhoWm1JeXNMRXNLampBMGxheFwvTmhCcmdmMVg1R1ZCZFdQOHlTRUZmV1ljRzdlbSIsIm1hYyI6IjUyYzY1NjkyYTNmYzgwYTU3NWQ1ZDJlNWZlOWVmY2NkODViZGIwNGE3ODM4Nzk2YjJmNjAzMDY1ZTM2MWMwNzMifQ%3D%3D; glidedsky_session=eyJpdiI6IkFHcE1QSnFLbnBob0N6VGp3M1AxaVE9PSIsInZhbHVlIjoia3haamo3WUFsT203WXViWEFPdWZMQjhKczdJb1pkVk1NK2toUmF2a2ZBYm41Yzl5Uk1LSkMzKzI4RzlEdVFiOSIsIm1hYyI6ImZjYTBiNjgzMzRhOGQ1OTAyOTIxZTUxOTAwMTM5NWRlMTkxNjhhNzhmNWUxOTZlYzkzZTMwYzNjNTllYmJiYTEifQ%3D%3D'
               }
    targetUrl = 'http://glidedsky.com/level/web/crawler-ip-block-1?page=' + str(num)
    # targetUrl = 'http://httpbin.org/get'
    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyUser = "H66T0EQ13CL82Z2D"
    proxyPass = "69DAEE70A475157F"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {"host": proxyHost, "port": proxyPort, "user": proxyUser,
                                                                "pass": proxyPass, }
    proxies = {"http": proxyMeta, "https": proxyMeta}

    res = requests.get(targetUrl, headers=headers, proxies=proxies, stream=True)
    return res
