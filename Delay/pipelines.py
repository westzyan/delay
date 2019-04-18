# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

from Delay import settings
class DelayPipeline(object):
    def __init__(self):
        self.f = open("delay.json","w")
    def process_item(self, item, spider):
            content = json.dumps(dict(item)) + ",\n"
            self.f.write(content)
            return item
    def close_spider(self,spider):
        self.f.close()

class dbpipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8')

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
            """insert into delay(routerName, fingerprint, contact, ip, onionRouterPort,  directoryServerPort, countryCode,platform )
            value (%s, %s, %s, %s,%s, %s, %s, %s)""",
            (item['routerName'],
            item['fingerprint'],
            item['contact'],
            item['ip'],
            item['onionRouterPort'],
            item['directoryServerPort'],
            item['countryCode'],
            item['platform']))
            # 提交sql语句
            self.connect.commit()
        finally:
            # 出现错误时打印错误日志
            print("错误")
        return item
    def close_spider(self,spider):
        self.connect.close()