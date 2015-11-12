# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from pic_download.items import PicDownloadItem

class PicDownloadMspiderSpider(CrawlSpider):

    name = 'pic_download_mspider'

    download_delay=1 #防止被ban

    allowed_domains = [] #无抓取时可设为空'http://tieba.baidu.com/p/2798034546/?see_lz=1'

    start_urls = ['http://tieba.baidu.com/p/2798034546?see_lz=1&pn=']

    rules = (
        Rule(LinkExtractor(allow=r'http://tieba\.baidu\.com/p/2798034546\?see_lz=1&pn=\d+'), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        
        #i = PicDownloadItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        #print response

        sel=Selector(response)
        
        images_url=sel.xpath("//img[@pic_type='1']/@src").extract()
        
        print 'the urls:\n'
        print images_url
        print '\n'

        item=PicDownloadItem()
        item['image_url']=[n for n in images_url]
        #item['image_url']=images_url

        yield item