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
30 2 * * 4 sh /home/zxiangxiang/spiderWeekly/spiderWeekly/spiders/*.sh
50 2 * * 4 sh /home/zxiangxiang/spiderWeekly/spiderWeekly/spiders/*.sh
```
这里挂起两个定时任务。（参数配置可网上查看）

## web服务启动
`gunicorn 入口文件名:app`
要在入口文件的`app.run()`加上
```
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```
