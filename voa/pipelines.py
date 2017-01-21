import MySQLdb
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VoaPipeline(object):
    def dbsql(self,item):
        db = MySQLdb.connect("your host", "user", "your password", "your schema")
        consor = db.cursor()
        #INSERT INTO `mainschema`.`all` (`title`, `date`, `categories`, `tags`, `url`) VALUES ('q', 'w', 'r', 't', 'u');
        sql = "INSERT INTO `mainschema`.`all` (`title`, `date`, `categories`, `tags`, `url`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (item['vtitle'], item['vdate'], item['vcategory'], item['vtag'],item['vlink'])
        print sql
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
