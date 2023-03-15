from flask import Flask, request
import requests
import datetime
import logging

app = Flask(__name__)


def push_ftqq(content):
    #自己的发送接口
    resp = requests.post("https://sc.ftqq.com/SCU91897T93980154c7b485b1602e06351f663b9a5e8292ef0785a.send",
                  data={"text": "xray vuln alarm", "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)

@app.route('/bugstore', methods=['POST'])
def xray_webhook():
    #print("ddd")
    vuln = request.json
    #print(type(vuln))
    # 因为还会收到 https://chaitin.github.io/xray/#/api/statistic 的数据
    if "detail" not in str(vuln):
        return "ok"
    content = """## Niupiscan 发现了新漏洞

url: {url}

插件: {plugin}

发现时间: {create_time}

请及时查看和处理
""".format(url=vuln["data"]["detail"]["addr"], plugin=vuln["data"]["plugin"],
           create_time=str(datetime.datetime.fromtimestamp(vuln["data"]["create_time"] / 1000)))
    try:
        #print(str(vuln['data']['create_time']))
        push_ftqq(content)
    except Exception as e:
        logging.exception(e)
    return 'ok'


if __name__ == '__main__':
    app.run(host='103.143.11.144', port=13435)
    
    
    
