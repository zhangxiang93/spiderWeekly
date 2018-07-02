# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from spiderWeekly.items import SearchItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_search = '前端'

    search_url = 'https://www.zhihu.com/search?type=column&q={query}'
    user_url = 'https://www.zhihu.com/api/v4/columns/{user}/articles?include={include}'
    user_include = 'data[*].admin_closed_comment,comment_count,suggest_edit,is_title_image_full_screen,can_comment,upvoted_followees,can_open_tipjar,can_tip,voteup_count,voting,topics,review_info,author.is_following'

    def start_requests(self):
        yield Request(self.search_url.format(query=self.start_search), self.parse_search)

    def parse_search(self, response):
        f = open('../../static/zhuanlan.json')
        result = json.load(f)
        # result = response.xpath('//div[@class="List-item"]/div/div/div/a/@href').extract()
        for v in result:
            start = result[v].find('zhuanlan.zhihu.com') + 19
            yield Request(self.user_url.format(user=result[v][start:], include=self.user_include), self.parse_user)

    def parse_user(self, response):
        results = json.loads(response.text)
        item = SearchItem()

        for field in item.fields:
            if field in results.keys():
                item[field] = results.get(field)
        yield item
