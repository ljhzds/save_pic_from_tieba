import sqlite3
import re
import os
import sys
import time

import requests 

'''
代码功能是把百度贴吧的一个帖子的链接记录到数据库中
'''

def save_base_url():

	conn = sqlite3.connect('zds_scapy.db')
	cur = conn.cursor()

	if(len(sys.argv) < 2):
		print('请输入目标url地址...')
		return 0
	for argv in sys.argv[1:]:
		print(argv)
		add_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))

		cur.execute('insert into base_url(url, is_used, url_desc, add_time) values(?, ?, ?, ?)', (argv, '0', '', add_time))

	cur.close()
	conn.commit()
	conn.close()
	print('get_base_url end...')

def get_base_url():

	base_url_list = []

	conn = sqlite3.connect('zds_scapy.db')
	cur = conn.cursor()

	for row in cur.execute('select * from base_url where is_used=:is_used ', {"is_used": '0',}):
	# for row in cur.execute('select * from base_url ')
		base_url_list.append(row[1])
	return base_url_list

def scapy_base_url(urls):
	for url in urls:
		print(url)
	pass
	#待添加的功能，从只看楼主页面里面找到图片的地址，将图片URLS以及此楼的帖子存到表里。
	#然后用requests.get.content读取写到JPG文件。如果还行的话实现翻页。

if __name__ == '__main__':

	save_base_url()
	url_list = get_base_url()
	scapy_base_url(url_list)

