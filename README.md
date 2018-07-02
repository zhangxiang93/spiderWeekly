## Python + Scrapy
前端技术文章爬取工具

## 数据库
MongoDB

## 定时任务
安装`crontab`
```
yum install -y vixie-cron
```
输入
```
crontab -e
```
完成定时配置
再输入
```
crontab -l
```
查看
```
30 2 * * 4 sh /home/zxiangxiang/spiderWeekly/spiderWeekly/spiders/zhihu.sh
50 2 * * 4 sh /home/zxiangxiang/spiderWeekly/spiderWeekly/spiders/juejin.sh
```

## web服务启动
`gunicorn myproject:app`
