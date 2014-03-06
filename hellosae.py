#coding:utf-8
from flask import Flask
from flask import request,render_template
import MySQLdb as mdb
import os
import sae.const

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/upload', methods = ['GET','POST'])
def upload():
	name = request.args['name']
	tel = request.args['tel']
	content = request.args['content']
	try:
		conn = mdb.connect(host= sae.const.MYSQL_DB , port=sae.const.MYSQL_PORT,user=sae.const.MYSQL_USER,passwd=sae.const.MYSQL_PASS ,db=sae.const.MYSQL_DB,charset='utf8')	
	except:
		return render_template('wrong.html')
	cursor = conn.cursor()
	sqli = "insert into test(name,tel,content) values (%s,%s, %s)"
	val = (name,tel,content)
	cursor.execute(sqli,val)
	conn.commit()
	cursor.close()
	conn.close()
	return render_template('good.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

application = sae.create_wsgi_app(app)	
