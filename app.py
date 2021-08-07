from flask import *
import pymongo
from pymongo import *
app = Flask(__name__)
app.debug = True
app.secret_key = 'test'
cluster = MongoClient("mongodb://Ranuga:ranuga2008@cluster0-shard-00-00.odlbl.mongodb.net:27017,cluster0-shard-00-01.odlbl.mongodb.net:27017,cluster0-shard-00-02.odlbl.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-spv504-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster['Blog']
collection = db['Blog']
@app.route('/')
def home() -> 'html':
    if collection.find_one() is None:
        blogs = [{'Head':'there is no blogs yet','Desc':'there is no blogs yet'}]
        return render_template('home.html',blogs=blogs)
    blogs = []
    for blog in collection.find():
        blogs.append(blog)
    return render_template('home.html',blogs=blogs)

@app.route('/add/blog',methods=['POST','GET'])
@app.route('/add/blog/',methods=['POST','GET'])
def add_blog() -> 'html':
    if request.method == 'POST':
        head = request.form['head']
        desc = request.form['desc']
        collection.insert_one({'Head':head,'Desc':desc})
        return redirect('/')
    else:
        return  render_template('add_blog.html')

if __name__ == '__main__':
    app.run()
