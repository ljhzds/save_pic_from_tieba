import sys
import re
import os
import os.path
import requests
from bs4 import BeautifulSoup

def get_imgs(url):

	'''
	输入一个百度贴吧帖子只看楼主的首页，然后，找这个帖子楼主发的所有图片，
	保存到以这个帖子主题为名字的文件夹里
	'''

	print('获取该链接的图片开始:', url)
	i = 1
	PAGE_NUM = 1
	# pattern = r'<img class="BDE_Image".*?\.jpg" pic_ext="jpeg"'
	pattern = r'共<span class="red">\d+</span>页</li>'
	for page in range(1,3):
		if(page > int(PAGE_NUM)):
			print('已经找到最后一页...')
			break
		target = url + '&pn=' + str(page)
		print(target)
		r = requests.get(target)
		# 如果是首页就建一个文件夹，并且找到总页数
		if(page == 1):
			soup = BeautifulSoup(r.text)
			topic = soup.title.text
			if os.path.exists(topic) == False:
				os.mkdir(topic)
			os.chdir(os.path.join(os.getcwd(), topic))
			print(os.getcwd())
			#total_page_num
			tpg_define = re.findall(pattern, r.text)
			for tpg in tpg_define:
				PAGE_NUM = tpg[19:-13]
				print('总页数是:', PAGE_NUM)
				break

		soup = BeautifulSoup(r.text)
		results = soup.find_all('img', class_='BDE_Image')
		for result in results:
			# print(result, type(result))
			# print(result.attrs)
			dict_of_bdimg = result.attrs
			img_src = dict_of_bdimg['src']
			if('pic_ext' in dict_of_bdimg.keys()):
				img_type = dict_of_bdimg['pic_ext']
			else:
				img_type = 'jpg'
			print(img_src, img_type)
			img_get = requests.get(img_src)
			print(img_get.status_code)
			print('第{0}张图片'.format(i))
			file_name = str(i)+'.'+img_type
			if os.path.isfile(file_name):
				print('已经存在这张图片:', file_name)
				continue
			with open(file_name, 'wb') as f:
				f.write(img_get.content)
				i += 1
	
	print('处理完毕，请检查目录:', topic)


if __name__ == '__main__':
	url = sys.argv[1]
	# url = 'http://tieba.baidu.com/p/2896671767?see_lz=1'
	print(url)
	get_imgs(url)

