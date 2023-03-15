import time
from celery_app import app
import redis
import queue
import simplejson
import threading
import subprocess
import requests
import warnings
import json



@app.task
def niupiscan(req):
	proxies = {
	'http': 'http://127.0.0.1:6662',
	'https': 'http://127.0.0.1:6662',
	}
	urls0 =req['url']
	headers0 =req['headers']
	method0=req['method']
	data0=req['data']
#	try:
#		if(method0=='GET'):
#			print(method0 + "GET判断正确")

#		elif(method0=='POST'):
#			print(method0 + "POST判断正确")

#	except:
#		print(method0 + ":该请求方法无法识别")


	try:
		if(method0=='GET'):
			a = requests.get(urls0, headers=headers0, proxies=proxies,timeout=30,verify=False)
			print("get请求成功")
		elif(method0=='POST'):
			a = requests.post(urls0, headers=headers0,data=data0, proxies=proxies,timeout=30,verify=False)
			print("post请求成功")
		
	except:
		print(method0 + ":该请求方法无法识别")
	return(0)


#def add(x, y):
#    print(add)
#    time.sleep(2)
#    return x + y
