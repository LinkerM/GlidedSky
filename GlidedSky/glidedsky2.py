'''
    爬虫-基础2
'''


import requests
from lxml import etree
import sys
sys.setrecursionlimit(1200)#修改递归最大次数,python默认为1000次

def pagingData(page = 1, total = 0):
	page = page
	url = 'http://glidedsky.com/level/web/crawler-basic-2?page=' + str(page)
	headers = {
		'Cookie': '_ga=GA1.2.1883545492.1573551638; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1576466982,1578882210; _gid=GA1.2.901313813.1578882210; footprints=eyJpdiI6ImxMTlhrWGpXek1yQ1d1aG5FaHB1c1E9PSIsInZhbHVlIjoibk5KQkt4UWlIMUk1Y1orVllXS2xHSDVERVwvSExUTVdEK3lVUHcreWkyVkJWalJaWEtJbXBBbXoxXC9JdENVaFRpIiwibWFjIjoiYzJiMWYyN2RlNjY2YWRkODEzNDI1NzNjMzAxNWY0NTJkMjY1NmQ5YzdhNWNjOWYyODMzY2YyNmM5MDcwYjdhMyJ9; XSRF-TOKEN=eyJpdiI6IlZCUk5lMGZkbXloOVlZNGg3T2J4QUE9PSIsInZhbHVlIjoiSjk4MHIrNVFkdTJRcUhScnRGQ3ljaDczYVRheUpWTTJcLzV0RUtkRjFFY0RSMEgyYTRZN2VjOGdISUtcL053NVRaIiwibWFjIjoiMTgxOTVmMWJiNDU3NTQ2M2Y5YzAzZWVjODY4NDcwZDYxYTZhYjQ5OWQ2MTA2YTlmMDBkYmVlYjc1MmU2Nzc0NyJ9; glidedsky_session=eyJpdiI6ImhiNjJ0XC9PTFwvZzNrVStzNllZXC9MWXc9PSIsInZhbHVlIjoiazcxek5iUzgyYUFsWTgwb044V1c4UnRjcjBOMHZNMVJIWVAwVVRPb3pXUTlTMHdpUTFqa0tlZkN4dTZyTW1wdSIsIm1hYyI6IjI3YmUxNGQ5YWZmZmE2YjIyYTYxYmIzOTNhN2EzN2MyODE4NGJiNTI4ZDcwZGYzNGViNmVmZTVjMjE1NmFiYmEifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1578893822',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
	}
	res = requests.get(url, headers = headers)
	if res.status_code == 200:
		number = 0
		res.encode = 'utf-8'
		html = etree.HTML(res.text)
		number_xpath = html.xpath("//div[@class='col-md-1']/text()")
		number_xpath = [int(y.replace('\n','').replace(' ','')) for y in number_xpath if y]
		for x in number_xpath:
			number += x
		if page > 1000:
			return total
		else:
			total += number
			page += 1
			print(page)
			print(total)
			return pagingData(page, total)

if __name__ == '__main__':
	total = pagingData(1, 0)
	print(total)
