import scrapy
import datetime
import voa.items
import re
class VoaSpider(scrapy.Spider):
    name = "voa"
    allowed_domains = ["voanews.com"]
    def start_requests(self):
        begin = datetime.date(2016, 1, 1)
        end = datetime.date(2016, 12, 31)
        page = []
        for i in range((end - begin).days + 1):
            day = begin + datetime.timedelta(days=i)
            page.append(scrapy.Request("http://www.voanews.com/z/602.html?"+"d="+str(day.day)+"&m="+str(day.month)+"&y="+str(day.year)))
        return page
    def parseTag(self,response):
        item = response.meta['item']
        jsstr = str(response.xpath("/html/body/script[2]/text()").extract())
        jsonstr = (re.findall(r'utag_data={.*};',jsstr)[0])[10:-1]
        item['vcategory'] = ""
        catgs = re.findall(r'categories:".*",',jsonstr)
        if catgs :
            item['vcategory'] = (catgs[0]).split("\"")[1]
        item['vtag'] = ""
        tags = re.findall(r'tags:".*"',jsonstr)
        if tags :
            item['vtag'] = (tags[0]).split("\"")[1]
        return item
    def parse(self, response):
        links = response.xpath(".//div[@class='media-block horizontal with-date width-img size-3']")
        items = []
        for index, link in enumerate(links):
            item = voa.items.VoaItem()
            item['vtitle'] = str(link.xpath(".//span[@class='title']/text()").extract())[3:-2]
            item['vdate'] = str(link.xpath(".//span[@class='date']/text()").extract()).split("'")[1]
            item['vlink'] = "http://www.voanews.com"+str(link.xpath("./div[@class='content']/a/@href").extract()).split("'")[1]
            items.append(item)
        for item in items:
            yield scrapy.Request(item['vlink'],meta={'item':item},callback=self.parseTag)
