import MySQLdb
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VoaPipeline(object):
    def dbsql(self,item):
        db = MySQLdb.connect("your host", "user", "your password", "your schema")#数据库链接
        consor = db.cursor()
        sql = "INSERT INTO `mainschema`.`all` (`title`, `date`, `categories`, `tags`, `url`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (item['vtitle'], item['vdate'], item['vcategory'], item['vtag'],item['vlink'])
        #写入数据库
        try:
            consor.execute(sql)
            db.commit()
            print "successful!"
        except Exception,e:
            print e
            db.rollback()
        db.close()
    def process_item(self, item, spider):
        self.dbsql(item)
        return item
