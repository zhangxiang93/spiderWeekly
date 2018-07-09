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
0 2 * * fri cd /home/*/spiderWeekly/spiderWeekly/spiders && /usr/local/bin/scrapy crawl ***
0 2 * * fri cd /home/*/spiderWeekly/spiderWeekly/spiders && /usr/local/bin/scrapy crawl ***
```
这里挂起两个定时任务，上面是定于每周五凌晨2点跑数据。（参数配置可网上查看）
重启服务
```
/sbin/service crond restart
```
重载配置
```
/sbin/service crond reload
```
查看服务状态
```
service crond status
```
设置`crontab`开机启动
```
ntsysv
```
进入一个图形控制界面，上下箭头调选项，空格键切换确定取消（*表确定选中），`tab`键切换底部确定取消键

## web服务启动
`gunicorn 入口文件名:app`
要在入口文件的`app.run()`加上
```
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

## 排序
`pymongo`实现数据库排序操作