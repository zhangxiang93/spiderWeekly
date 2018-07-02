#! /bin/sh
export PATH=$PATH:/usr/local/bin
# 跳转至Scrapy项目目录
cd /home/zxiangxiang/spiderWeekly/spiderWeekly/spiders
# 后台运行抓取，并将日志输出到run.log文件
nohup scrapy crawl zhihu >> logs/zhihu.log 2>&1 &