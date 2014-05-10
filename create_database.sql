drop table if exists zds_scapy;
create table zds_scapy(
	id integer primary key autoincrement,
	base_url TEXT(100),
	title TEXT(100),
	url TEXT(100),
	save_path TEXT(100),
	create_time TEXT(50)	
);
drop table if exists base_url;
create table base_url(
	id integer primary key autoincrement,
	url TEXT(100),
	is_used TEXT(2),
	url_desc TEXT(200),
	add_time TEXT(50)
);