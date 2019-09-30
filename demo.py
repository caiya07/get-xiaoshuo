# -*- coding:utf-8 -*-
import requests,os,re,time
from bs4 import BeautifulSoup

class XIAOSHUO(object):

	def __init__(self):
		self.url = 'http://www.quanshuwang.com/book/44/44683'
		self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

	def get_html(self,url):
		html = requests.get(url=url, headers=self.headers, timeout=10).content.decode('gbk')
		return html

	def main(self,number):
		html = self.get_html(self.url)
		p = '<a href="(http://www.quanshuwang.com/book/.*?)" title=".*?">(.*?)</a>'
		for i in re.findall(p, html):
			print(i[0])
			html = self.get_html(i[0])
			soup = BeautifulSoup(html, 'lxml').find('div', attrs={'id': 'content'}).text
			with open(i[1], 'w', encoding='utf-8')as f:
				f.write(soup[9:-9])
				time.sleep(0.1)

			number = number -1
			if number == 0:
				exit()

if __name__ == '__main__':
	t = XIAOSHUO()
	t.main(20)