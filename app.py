# /*
# * @Author: z.xiangxiang 
# * @Date: 2018-06-04 20:13:05 
# * @Last Modified by: z.xiangxiang
# * @Last Modified time: 2018-06-04 20:15:49
# * @version: 1.0
# */

import pymongo
import time
from flask import Flask, render_template, request, redirect
from dbconfig import MONGO_URL, MONGO_DB, MONGO_TABLE_JUEJIN, MONGO_TABLE_ZHIHU
app = Flask(__name__)

# mongodb
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


@app.route('/')
def page_index():
    return redirect('/index')


@app.route('/index/', methods=['GET', 'POST'])
def page_load():
    if request.method == 'GET':
        time.sleep(1)
        articles_juejin = db[MONGO_TABLE_JUEJIN].find()
        articles_zhihu = db[MONGO_TABLE_ZHIHU].find()
        return render_template('index.html', arts_juejin = articles_juejin, arts_zhihu=articles_zhihu)


if(__name__) == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
