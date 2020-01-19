'''
    爬虫-CSS反爬
'''

import requests
from lxml import etree
import re
import sys
sys.setrecursionlimit(1200) #修改递归最大次数,python默认为1000次

def star_number(url, headers, number):
	res = requests.get(url, headers = headers)
	if res.status_code == 200:
		html = etree.HTML(res.text)
		number_list = html.xpath('//div[@class="col-md-1"]')
		for n_data in number_list:
			num = n_data.xpath('./div/text()')#获取数字
			num_str = n_data.xpath('./div/@class')#获取数字的class属性,该属性可以在网页中获取对应关系
			if len(num_str) > len(num):#如果获取到的class比数字少,说明原网页中有直接的数字
				nums = re.findall(num_str[-1] + ':before { content:"(\d+)" }',res.text)#获取该属性的content属性，contont就是实际的数字
				if nums:
					number+=int(nums[0])
				print('源代码中自带的数字',int(nums[0]))
			else:#如果数字和class一样多,需要获取该数字的透明度和位置参数 注：opacity:0说明该数字为隐藏字，是不需要的,left为该数字的位置参数,越小的越前
				numbs = ['x','x','x','x','x','x','x','x','x','x','x','x']#设置一个默认值,将混乱的数字排序后填充进去
				a = 0#循环数字时的手动加上位置参数，位置参数用于后面计算该数字的偏移量
				for x,y in zip(num,num_str):
					position = a#获取网页上数字的位置,由于有重复数字,所以不使用list.index(number)
					judge = re.findall(y + ' { opacity:(\d+) }',res.text)#判断该数字是否透明
					if judge:
						#print(f"{x}数字透明度为0,跳过不需要")
						pass
					else:
						left = re.findall(y + ' { left:(.*?) }',res.text)#获取数字的偏移量
						if left:
							position = position + int(left[0].replace('em',''))#使用数字的位置 + 网页上的偏移量,如果不行可以试试减法,反正这里减法不行
							numbs[position] = x#将之前设置的默认值position替换成数字x
						else:
							numbs[position] = x#如果数字没有偏移,则按原位置替换到numbs上
					a+=1
				str1 = int(''.join([x for x in numbs if x !='x']))#去除多余的x字符.
				number += str1
				print('混乱数字排序后: ',str1)
		next_page = html.xpath('//a[@rel="next"]/@href')
		if next_page:
			return star_number(next_page[0],headers,number)
		else:
			return number
	else:
		print(f'页面访问错误',res.status_code)

if __name__ == '__main__':
	url = 'http://glidedsky.com/level/web/crawler-css-puzzle-1'
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
	'Cookie':'_ga=GA1.2.1883545492.1573551638; _gid=GA1.2.901313813.1578882210; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1578882210,1578964702,1579057875,1579138125; footprints=eyJpdiI6IjRcL1U3aFdQcGQ5VTVQWXpkVVhBM1lBPT0iLCJ2YWx1ZSI6InVWRzNZS1JZV3VEbWNJcVROTERFb004ajY5VTJZcmJ4SkJmRlR2cU44K0ZlVERXYXZwRDFaKzJKWDNFanExOGMiLCJtYWMiOiIzMTg4N2Y2MTY2NDk3NmQyM2QxOWRkZWEzZDFjYzZhOWM4N2NjODExYmYxZmMzMWUyNzYxMmE4N2JkMjdkYjVkIn0%3D; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IkMrTzBuYXgraGNTQnhCNnhJRGxVcXc9PSIsInZhbHVlIjoiNXA1ZlM2MnJ4YkxVMkh5OUtWVVJVRHRUeks3MmNMdlJESmo5YjMwQW5HQTFDTkExZGNPYlp0d3VKemRYYjVoTSIsIm1hYyI6IjkyYjE1MGQwMzUwZWM5MGJmOTRjM2FmMjVlMzM4YjgxMGZmOWJlOTU1ZWQ3NWM4ZDhlZDM1ZDZhZjc0OTgwMjYifQ%3D%3D; glidedsky_session=eyJpdiI6InVqQzdcL09oMG50MVFQcFFmczhGblVBPT0iLCJ2YWx1ZSI6IndtM3RpNmMxWWkydTVxYXcyMVZCRGloYTFlUlFoaHRhRjBVb1dIY2FPYjhIYVlvQkRJM0hlK2FyNDNzaCs1XC9TIiwibWFjIjoiNjM3MWJlMTVkMjY1NTk2MGEwNmFhZWI1NWJiMWVhMGE5NDk5YTdiZWI0Yzg3YmMxYjM3YTAzMTBlNzJlMmQyMSJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1579162374'
	}
	number = star_number(url, headers, 0)
	print(number)
