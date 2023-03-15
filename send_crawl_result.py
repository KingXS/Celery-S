from flask import Flask, request
import requests
import datetime
import logging
import json

app = Flask(__name__)


def push_ftqq(content):
    #自己的发送接口
    resp = requests.post("https://sc.ftqq.com/SCU91897T93980154c7b485b1602e06351f663b9a5e8292ef0785a.send",
                  data={"text": "牛皮爬虫爬取结果通知", "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)

@app.route('/bugstore', methods=['POST'])
def xray_webhook():
    vuln = request.json
    vuln = json.loads(vuln)
    # 因为还会收到 https://chaitin.github.io/xray/#/api/statistic 的数据
#    if "vuln_class" not in vuln:
#        return "ok"
    content = """## 爬虫运行结果通知
result: {result}
请及时查看和处理
""".format(result = vuln["result"])
    try:
        push_ftqq(content)
    except Exception as e:
        logging.exception(e)
    return 'ok'


if __name__ == '__main__':
    app.run(host='103.143.11.144', port=13435)
