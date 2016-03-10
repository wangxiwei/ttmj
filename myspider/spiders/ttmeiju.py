# -*- coding: utf-8 -*-
import scrapy
from myspider.items import ttmeijvItem


class TtmeijuSpider(scrapy.Spider):
    name = "ttmeiju"
    allowed_domains = ["ttmeiju.com"]
    start_urls = (
        'http://www.ttmeiju.com/summary.html',
    )

    def parse(self, response):
        for tr in response.xpath('//tr'):
            item = ttmeijvItem()
            num = tr.xpath('td[1]/text()').extract()
            title = tr.xpath('td[2]/a/text()').extract()
            url = tr.xpath('td[2]/a/@href').extract()
            status = tr.xpath('td[3]/text()').extract()
            update_date = tr.xpath('td[4]/text()').extract()
            return_date = tr.xpath('td[5]/text()').extract()
            if num:
                item['num'] = num[0]
            if title:
                item['title'] = title[0]
            if url:
                item['url'] = url[0]
            if status:
                item['status'] = status[0]
            if update_date:
                item['update_date'] = update_date[0]
            if return_date:
                item['return_date'] = return_date[0]
            # item['num'] = ','.join(num)
            # item['title'] = ','.join(title)
            # item['url'] = ','.join(url)
            # item['status'] = ','.join(status)
            # item['update_date'] = ','.join(update_date)
            # item['return_date'] = ','.join(return_date)
            yield item

        pass
