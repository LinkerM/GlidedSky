'''
    爬虫-字体反爬-1
'''


import requests
from lxml import etree
import re
import base64
from fontTools.ttLib import TTFont
import sys
sys.setrecursionlimit(1200) #修改递归最大次数,python默认为1000次

def star(url, headers, number_num):
	res = requests.get(url, headers = headers)
	html = etree.HTML(res.text)
	font_data = re.findall('base64,(.*?)\) format',res.text)#查找字体加密文件
	dict_s = down_tff(font_data[0],'/Users/Media/Desktop/python/glidedsky网站抓取/')
	# dict_s = down_tff('AAEAAAAKAIAAAwAgT1MvMkEnQdAAAAEoAAAAYGNtYXAAVgDAAAABpAAAAEhnbHlmdUQ+YgAAAgQAAAPWaGVhZBc34PoAAACsAAAANmhoZWEHCgOTAAAA5AAAACRobXR4BwEBNgAAAYgAAAAabG9jYQTKBcIAAAHsAAAAGG1heHAAEQA4AAABCAAAACBuYW1lQTDOUQAABdwAAAGVcG9zdAB+AHoAAAd0AAAAOAABAAAAAQAAYHwXFF8PPPUAAwPoAAAAANpETpEAAAAA2kROkQAU/4gDhANwAAAAAwACAAAAAAAAAAEAAANw/4gAAAPoABQAIAOEAAEAAAAAAAAAAAAAAAAAAAACAAEAAAALADYABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAwJTAZAABQAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAPz8/PwAAADAAOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAD6ABkAisAMQBYACgAHQAUABwAOAAxAC0ALAAAAAAAAgAAAAMAAAAUAAMAAQAAABQABAA0AAAABAAEAAEAAAA5//8AAAAw//8AAAABAAQAAAAFAAMAAgAEAAkACgABAAcABgAIAAAALABTAGkAjwDGAOgBGAFNAWQBswHrAAUAZP+IA4QDcAADAAYACQAMAA8AABMhESEBIQEBEQkDJwEBZAMg/OACzv2EAT4BXv7CAR7+wv7CIAE+/sIDcPwYA7b+Z/4+AzL+Z/4+AZn+ZykBmQGZAAACADH/8wH6AusADwAXAAA3JjU0NzYzMhcWFRQHBiMiExAjIhEQMzJvPj47bGs7Pj47a2v2i4yMi1Jku7tiXV5iurtkXwF+ATD+0P7LAAABAFgAAAHqAt0ACwAANzMRIzU2NzMRMxUhWKOCWz1Gk/5uTAIjOhEj/W9MAAEAKAAAAfkC6wAWAAA3ADU0JyYjIgcnNjMyFxYVFAE2MzMVISwBUCEkQlFHNWR0Yjo5/uFZH8v+MzYBJrNCJilVNGw7O2O6/vAHTwABAB3/8wHzAusAJQAANzcWMzI3NjU0IzUyNTQnJicGByc2MzIXFhUUBxUWFxYVFAcGIyIdLlBmQikq5MshIjlSRjFfbl86PINEKy1FQWWPVzxUJSU+k0aMNSAfAgNGOlgwMlaAMQQQLzNIYDo3AAIAFAAAAgsC3QAHABIAAAE1NDcjBgcHBSMVIzUhNQEzETMBUwYEGCOnAZhhV/7BATFlYQET4RNyMDz6ScrKPAHX/jYAAQAc//MB9QLdAB4AADc3FjMyNzY1NCcmIyIHJxMhFSEHNjMyFxYVFAcGIyIcLVFjQiwuKSlGOUExFwFl/usSNDlhO0FJRWKIVDxRLjFOTi0sKx4BV07UHTg+c3RGQgAAAgA4//MB/wLrAAkAIgAAJTY1NCMiBxYzMhMmIyIDNjMyFxYVFAcGIyInJjU0NzYzMhcBhSSEVEIRjTVeLki4BUleXzU3PjxYbkFGUkh1ZUZoL0qiXusCLTj+z1k6PHBoREJbYLDKaFtLAAEAMQAAAfwC3QAKAAAzEhMhNSEVBgcGB8YRvf6dAct6LiYJAYYBCU43nZ2D6QADAC3/8wH9AugAGQAnADUAADcmNTQ3NSY1NDc2MzIXFhUUBxUWFRQHBiMiEzQnJiMiBwYVFBcWFzYDNjU0JyYnBhUUFxYzMm9Ch2M5OVdcNzZifD9BZmXjISM5MyAhMiNQTBYnOiRkZCwrQj8qN1WBSQVEZVM0MzY1VmVMBUh4UTY3Ai84JSYhITU7KRwgQ/6JIjdCLBsoQGY6JyYAAAIALP/zAfQC6wALACQAAAEmIyIHBhUUFxYzMgcWMzITBiMiJyY1NDc2MzIXFhUUBwYjIicBng+RNSMkISJAVO0ySa8JSWBeNTc+PFhuQkZRR3JoSAG85y0vSkwrLOM4ATJbOzxwaERCV12p0WxeSwAAAAAADACWAAEAAAAAAAAAFAAAAAEAAAAAAAEACQAUAAEAAAAAAAIABwAdAAEAAAAAAAUACwAkAAEAAAAAAAYAEQAvAAEAAAAAAAsAFQBAAAMAAQQJAAAAKABVAAMAAQQJAAEAEgB9AAMAAQQJAAIADgCPAAMAAQQJAAUAFgCdAAMAAQQJAAYAIgCzAAMAAQQJAAsAKgDVQ3JlYXRlZCBieSBHbGlkZWRTa3lHbGlkZWRTa3lSZWd1bGFyVmVyc2lvbiAxLjBHbGlkZWRTa3ktUmVndWxhcmh0dHA6Ly9nbGlkZWRza3kuY29tLwBDAHIAZQBhAHQAZQBkACAAYgB5ACAARwBsAGkAZABlAGQAUwBrAHkARwBsAGkAZABlAGQAUwBrAHkAUgBlAGcAdQBsAGEAcgBWAGUAcgBzAGkAbwBuACAAMQAuADAARwBsAGkAZABlAGQAUwBrAHkALQBSAGUAZwB1AGwAYQByAGgAdAB0AHAAOgAvAC8AZwBsAGkAZABlAGQAcwBrAHkALgBjAG8AbQAvAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAABkAFQAUABYAEwAbABoAHAAXABg=','/Users/Media/Desktop/python/glidedsky网站抓取/')
	n_list = html.xpath('//div[@class="col-md-1"]/text()')
	n_list = [x.replace('\n','').replace(' ','') for x in n_list if x]
	for i in n_list:
		num = ''
		for str1 in i:
			if str1 in dict_s:
				num += dict_s[str1]
		print(f'替换之后的真数据{num}')
		number_num += int(num)
	next_page = html.xpath('//a[@rel="next"]/@href')
	if next_page:
 		return star(next_page[0], headers, number_num)
	else:
 		return number_num

def down_tff(font_data, font_name):
	online = base64.b64decode(font_data)
	with open(font_name + 'test.ttf', 'wb') as f:
	 	f.write(online)

	font = TTFont(font_name + 'test.ttf') # 打开本地的ttf文件
	font.saveXML(font_name +'test.xml')  # 转换成xml
	#ori_font.getGlyphNames这个是获取文件中name属性的,这里用不上
	ori_list1 = replace_number(font.getGlyphOrder()[1:])
	s_list = []
	for x, y in font.getBestCmap().items():
		s_list.append(y)
	s_list = replace_number(s_list)
	dic_c = {}
	for x,y in zip(ori_list1, s_list):
		dic_c[x] = y
	return dic_c

def replace_number(lists):
	list2 = []
	for i in lists:
		u = i.replace('zero','0').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').\
		replace('seven','7').replace('eight','8').replace('nine','9')
		list2.append(u)	
	return(list2)

if __name__ == '__main__':
	url = 'http://glidedsky.com/level/web/crawler-font-puzzle-1'
	headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'no-cache',
	'Connection':'keep-alive',
	'Host':'glidedsky.com',
	'Pragma':'no-cache',
	'Referer':'http://glidedsky.com/login',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
	'Cookie':'_ga=GA1.2.1883545492.1573551638; _gid=GA1.2.901313813.1578882210; footprints=eyJpdiI6IklmOSs4dXBENExRczdXZytzeG5VN2c9PSIsInZhbHVlIjoiZlRnU1wvMGpHVjJPR0hqUDhPa3hkOWZiOG5qcDQ2TEVRZEZWTFIzSlZPd0N1VlVyR3ZwY1VaVmd4aTJRZDY4UjciLCJtYWMiOiIyZGQ2YzIzNWQyMGU3MWIwM2JlYTZkYTMyNTFjZDRiYmIxNzdmM2EzYjhhNTcxMWM1ZDg2ZDY3NmZmNzc5ZmM3In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1576466982,1578882210,1578964702,1579057875; XSRF-TOKEN=eyJpdiI6InVmT3NHWDRiZ1dVQWdXSHd4XC9vTWlnPT0iLCJ2YWx1ZSI6Ik1EVDFHZUZHeXErQkFTaWV3YkNJb1loeHpcL3ZGZklHaHpcL01jZlUrQ3QxXC9udnBlTlIzczh4Q0IxZk4rSVczelYiLCJtYWMiOiIwNzM4M2ZjNDY3OWQzZjNmZWQyYWQ1OGNmYjY2NzkxYjczZTJiNTBkMjk4ZmM4M2UwYzZiOWUyY2Y2ZjkzMzAyIn0%3D; glidedsky_session=eyJpdiI6IlUza3h4RHhVNVZJbW9qQjlRbEIwa2c9PSIsInZhbHVlIjoiQUwwcmRITWZrcDJsaTdcL3RlQms0XC9Xbng2a2NNOHA4dTZNcm5xd2tIYWc2ZDJsM1Q0WWRJTWZ5Q1ZkZVJWR1dYIiwibWFjIjoiZjI4NjY5NTBjMDAyZDQ3M2VmNGJkYmI5ZTMyMGFjMTQwMWU4MWQ5NzI3N2YzZTY0ZTJjNjQ5MzJkZmRmMzU0ZCJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1579057891'
	}
	number = 0
	number = star(url, headers, 0)
	print(number)
