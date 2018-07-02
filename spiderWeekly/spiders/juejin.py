# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from spiderWeekly.items import JueItem


class JuejinSpider(Spider):
    name = 'juejin'
    allowed_domains = ['juejin.im']
    start_urls = ['http://juejin.im/']

    search_url = 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_rank?src=web&limit={limit}&category=5562b415e4b00c57d9b94ac8'
    limit = 50

    def start_requests(self):
        yield Request(self.search_url.format(limit=self.limit), self.parse_search)

    def parse_search(self, response):
        results = json.loads(response.text).get('d')
        item = JueItem()

        for field in item.fields:
            if field in results.keys():
                item[field] = results.get(field)
        yield item
