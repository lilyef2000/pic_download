# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from pic_download.items import PicDownloadItem


class PicDownloadSpiderSpider(Spider):
    name = "pic_download_spider"
    
    start_urls = (
        'http://tieba.baidu.com/p/2798034546/?see_lz=1',
    )

    def parse(self, response):
        # pass
        sel=Selector(response)
        
        images_url=sel.xpath("//img[@pic_type='1']/@src").extract()
        
        print 'the urls:\n'
        print images_url
        print '\n'

        item=PicDownloadItem()
        item['image_url']=[n for n in images_url]
        #item['image_url']=images_url

        yield item

