import sqlite3


def dbs_init():
	conn = sqlite3.connect('zds_scapy.db')
	cur = conn.cursor()
	# cur.execute('drop table zds_scapy')
	# cur.execute('drop table base_url')

    #is_used 这个字段是用来说明这个帖子的链接是否已经用了的, 0 未用 1 已用
	with open('create_database.sql', 'r') as f:
		cur.executescript(f.read())
		cur.close()
	conn.close()

if __name__ == '__main__':
	dbs_init()
	pass