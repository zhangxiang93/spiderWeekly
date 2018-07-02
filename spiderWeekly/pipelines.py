# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import re
import pytz
from datetime import datetime
from spiderWeekly.items import SearchItem, JueItem


class MongoPipeline(object):
    collection_zhihu = 'search_result'
    collection_juejin = 'juejin_result'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.collection_zhihu].remove({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, SearchItem):
            for data in item.get('data'):
                build = datetime.fromtimestamp(data.get('updated'), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
                re_h = re.compile('</?\w+[^>]*')
                desc = re_h.sub('', data.get('excerpt'))
                zhihu_info = {
                    'id': data.get('id'),
                    'title': data.get('title'),
                    'faceImg': data.get('image_url'),
                    'build': build,
                    'desc': desc,
                    'url': data.get('url'),
                    'voteup_count': data.get('voteup_count'),
                    'author': data.get('author').get('name'),
                    'author_page': 'https://www.zhihu.com/people/' + data.get('author').get('url_token'),
                    'comment_count': data.get('comment_count')
                }
                self.db[self.collection_zhihu].update({'id': zhihu_info['id']}, {'$set': zhihu_info}, True)
        if isinstance(item, JueItem):
            if self.db[self.collection_juejin].find().count() != 0:
                self.db[self.collection_juejin].remove({})
            for item in item.get('entrylist'):
                tags = []
                for tag in item.get('tags'):
                    tags.append(tag.get('title'))
                tags = ', '.join(tags)
                juejin_info = {
                    'collect': item.get('collectionCount'),
                    'praise': item.get('commentsCount'),
                    'title': item.get('title'),
                    'url': item.get('originalUrl'),
                    'desc': item.get('content'),
                    'author': item.get('user').get('username'),
                    'creattime': item.get('createdAt'),
                    'tags': tags,
                    'views': item.get('viewsCount')
                }
                self.db[self.collection_juejin].insert(dict(juejin_info))
        return item
