#!/usr/bin/env python
# coding=utf-8 
import time 
import socket 
import pymysql
import requests 
import socket
import pdb  
from multiprocessing.dummy import Pool  

def proxy_check(proxy):
    ip,port,protocol = proxy 
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Referer':'https://www.bing.com/?scope=web&mkt=es-CL&FORM=MOZSBR&pc=MOZI',
        'DNT':'1',
        'Host':'www.bing.com'

    }

    sql = "delete from proxy where ip = '{}'".format(ip)
    proxy = ip + ':' + port
    proxies = {protocol.lower(): 'http://' + proxy}
    try:
        r = requests.get(
           'https://www.bing.com',
            proxies=proxies,
            headers=headers,
#            timeout=5,
            )
        time.sleep(1)

    except Exception as e: 
        print('error')
        cur.execute(sql)
        conn.commit()

    else:
        if r and  len(r.text)>2000:
            print(protocol+"://"+proxy + ' OK')
        else:
            print('error')
            cur.execute(sql) 
            conn.commit(sql)



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

#pdb.set_trace()

pool = Pool(3)
results = pool.map(proxy_check,proxy_lists)

    
cur.close()
conn.close()
