#!/usr/bin/env python
# coding=utf-8
import pymysql
import requests
import pdb

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='toor',
    db='spider',
    charset='utf8'
    )

cur = conn.cursor()
cur.execute('select ip,port,protocol from proxy')
proxy_lists = cur.fetchall() 

pdb.set_trace()


for ip, port, protocol in proxy_lists:
    sql = "delete from proxy where ip = '{}'".format(ip)
    proxy = ip + ':' + port
    proxies = {protocol.lower(): 'http://' + proxy}
    try:
        r = requests.get(
            'http://ip.cn',
            proxies=proxies,
            timeout=5,
            )

    except:
        print(proxy + " error1")
        cur.execute(sql)
        conn.commit()
        continue

    if r.text.find(ip) == -1:
        print(proxy + ' error2')
        cur.execute(sql)
        conn.commit()
    else:
        print(proxy + ' OK')

cur.close()
conn.close()
