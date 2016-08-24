# -*- coding: utf-8 -*-
import pymysql   
import pdb

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html  


class ProxypoolPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'toor',
            db = 'spider',
            charset = 'utf8'
            )

        self.cur = self.conn.cursor()



    def process_item(self, item, spider):
        item['location'] = [ i.strip() for i in item['location']] 
        try:
            for i in range(len(item['ip'])):
                sql = "insert into proxy values ('{}','{}','{}','{}',now())".format(item['ip'][i],item['port'][i],item['protocol'][i],item['location'][i])
#                pdb.set_trace()
                self.cur.execute(sql)
            self.conn.commit()   

        except:
            print('sql error')

        return item  

