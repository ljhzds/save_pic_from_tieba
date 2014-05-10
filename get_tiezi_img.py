import sqlite3
import re
import os
import sys
import time

import requests 

'''
代码功能是把百度贴吧的一个帖子里面的楼主发的图片全部保存，并记录到数据库中
'''

def get_base_url():

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

if __name__ == '__main__':

	get_base_url()

