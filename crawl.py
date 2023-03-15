import time

import queue
import simplejson
import threading
import subprocess
import requests
import warnings
import json



def crawlurls(target):
    #使用第二台服务器的db2存储爬取的结果
    
    #r = redis.Redis(connection_pool=pool)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.0 Safari/537.36'}
    headers_xu = json.dumps(headers)
    postdata = 'hello'
    postdata_xu  = json.dumps(postdata)
    
    t = target
    cmd = ["/home/kali/test/crawlergo", "-c", "/home/kali/test/chrome-linux/chrome","-i","-fv","default=hello","-fkv","mail=222@qq.com","-fkv","name=admin","-fkv","pass=123456","--custom-headers", headers_xu,"--post-data",postdata,"-t", "20","-f","smart","--fuzz-path", "--output-mode", "json", t]
    rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('----------开始爬取----------')
    output, error = rsp.communicate()
    print(output.decode())
    try:
	    result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
    except:
	    return
    #爬取到的有效域名
    req_list = result["req_list"]
    sub_domain = result["sub_domain_list"]

    print(req_list)

    #将有效域名写入redis
    for i in req_list:

        print(i['url'])
        print('存入数据库成功')
    #return不能写在for循环里面,否则会提前结束
    return 0


if __name__ == "__main__":
    target = "http://testphp.vulnweb.com/"
    crawlurls(target)