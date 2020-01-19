'''
	爬虫-验证码-1
'''
from selenium import webdriver #3.141
from selenium.webdriver.support.ui import WebDriverWait # 等待元素加载的
from selenium.webdriver.common.action_chains import ActionChains  #拖拽
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options#配置浏览器属性
import requests
from lxml import etree
import re
import sys
import time
import json

'''
	破解滑块验证码思路:
	selenium登录问题
	iframe网页的定位
	破解方案(1.下载缺口图和完整图，对比两张图的像素后判定偏移量。 2.直接识别缺口图的缺口)
	完整图的下载需要找到css设置
'''
def obtain_cookies():
	'''
		手动登录后获取cookie,保存到text中，需要手动将文件中的true和false加入引号
		也可改成自动登录
	'''
	driver = webdriver.Chrome()
	driver.get('http://glidedsky.com/level/web/crawler-captcha-1?page=1')
	print("睡眠15秒,手动登入账号密码获取cookies")
	time.sleep(15)
	dic_cookies = driver.get_cookies()
	fw = open('/Users/Media/Desktop/python/glidedsky网站抓取/glidesky6.text','w')#将网页的cookies保存在文件中,注意false和true需要加上双引号
	#txt文件复制过来以后,需要将字段手动复制到代码中来,不能直接读取文件添加cookies
	json.dump(dic_cookies,fw)
	fw.close()

def login_html(url):
	'''
		登录网页，破解滑动验证码并返回网页中源代码提取数据
		URL: 需要抓取的网页
		return : 页面抓取数字总和
	'''
	chrome_options = Options() 
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
	driver = webdriver.Chrome()
	driver.get('http://glidedsky.com/login')
	time.sleep(2)
	driver.find_element_by_id('email').clear()
	driver.find_element_by_id('email').send_keys('1159082517@qq.com') 
	driver.find_element_by_id('password').clear()
	driver.find_element_by_id('password').send_keys('poiuytrewq...')
	driver.find_element_by_xpath('//*[@id="app"]/main/div[1]/div/div/div/div[2]/form/div[4]/div/button').click()
    # driver.find_element_by_id('switcher_plogin').click()

    # driver.find_element_by_class_name('btn btn-primary').click()
    # slide(driver)
	# cookies = [{"domain": ".glidedsky.com", "httpOnly": "false", "name": "Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6", "path": "/", "secure": "false", "value": "1579250437"}, {"domain": "glidedsky.com", "expiry": 1579257635.939106, "httpOnly": "true", "name": "glidedsky_session", "path": "/", "secure": "false", "value": "eyJpdiI6Inkwd21ZYzBhd3I1MUZrNTJhYW1JMGc9PSIsInZhbHVlIjoicVdrSU45cFFpaFE4bGVWeGdFeWxZQnNXTGFQWVB5SkRPYmdQTWNNXC9yVVhMYU1ac0FlUlJvS2xRaFhiWlwvWlY1IiwibWFjIjoiZjcxZmJiMmM3ZmY5YzFiOWQ4OWNlMTg2NzdjMDlhOTIyZjQ3MTQzZGEzZTk4ODUxYTk0OWRhMTE2MjI5MmE4OCJ9"}, {"domain": "glidedsky.com", "expiry": 1579257635.939054, "httpOnly": "false", "name": "XSRF-TOKEN", "path": "/", "secure": "false", "value": "eyJpdiI6IjJMSVRVUjRsbktNVHVRNUtQMHg3VFE9PSIsInZhbHVlIjoiUkRqbUFXZWlGVnRqdHNlZ1Q5em5YWjExZ09MWlRqRTQ2VG5hcTdwXC85ajFuZ0RDM3JaMUYwejI0SlV3RHFsamMiLCJtYWMiOiIzZTU5Zjc5MTI4NDAzNDU3ODFmNDRkNGNjOGZmYWY5NGY3MDFlYzBlZjYxZGUyYTRmODdmYTFkZTg0NDg1Y2NkIn0%3D"}, {"domain": ".glidedsky.com", "expiry": 1579250483, "httpOnly": "false", "name": "_gat_gtag_UA_75859356_3", "path": "/", "secure": "false", "value": "1"}, {"domain": ".glidedsky.com", "expiry": 1610786436, "httpOnly": "false", "name": "Hm_lvt_020fbaad6104bcddd1db12d6b78812f6", "path": "/", "secure": "false", "value": "1579250424"}, {"domain": ".glidedsky.com", "expiry": 1579336836, "httpOnly": "false", "name": "_gid", "path": "/", "secure": "false", "value": "GA1.2.2038122858.1579250424"}, {"domain": ".glidedsky.com", "expiry": 1642322436, "httpOnly": "false", "name": "_ga", "path": "/", "secure": "false", "value": "GA1.2.493940517.1579250424"}, {"domain": "glidedsky.com", "expiry": 1594802421.335046, "httpOnly": "true", "name": "footprints", "path": "/", "secure": "false", "value": "eyJpdiI6InN2UVV4OTJuYVB5OHpiRG4zRVAzZ2c9PSIsInZhbHVlIjoic1EzK1ZcLzJJMHVET0tcL2NUeEs5TmxmVjZ1MnBtd1wvVHVnSlA0YU9MR0R5NWxNRUJpdmNoODc4eWx1Slg0R1wvSGUiLCJtYWMiOiI2ZTBhMTI1MGUwNjU1YTExNjVmZTRmNGQ3MmIxNmMxYzViOWFmZjMzYjgzNjNjMDIwMTU3ZTU5NWFhNDEyYTI0In0%3D"}]
	# for i in cookies:
	# 	driver.add_cooki
    # 用谷歌浏览器打开网址
    # driver.switch_to.frame('login_frame')
    # 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
	
	driver.get(url) #登入抓取网页

if __name__ == '__main__':

	# obtain_cookies() # 获取cookies
	url = 'http://glidedsky.com/level/web/crawler-captcha-1?page=1'
	login_html(url)
	