import json,os,base64
import requests



def req_norLine(url,data,imagename):
    url = 'http://127.0.0.1:5000/Line/norline'
    data = {'xaxis': ["6月", "7月", "8月", "9月", "10月", "11月"],'typelist':['商家A'],'yaxis':[268, 278, 369, 310, 504, 1056],'maintitle':'销量图','mintitle':'小标题'}
    r = requests.get(url, data=json.dumps(data))
    res = json.loads(r.text)
    with open(imagename, 'wb') as f:
        f.write(base64.b64decode(res['result']))



def req_mulLine(url,data,imagename):
    url = 'http://127.0.0.1:5000/Line/mulline'
    data = {'xaxis': ["6月", "7月", "8月", "9月", "10月", "11月"],'typelist':['商家A','商家B'],'yaxis':[[268, 278, 369, 310, 504, 1056],[55, 60, 16, 20, 15, 80]],'maintitle':'销量图','mintitle':'小标题'}
    r = requests.get(url, data=json.dumps(data))
    res = json.loads(r.text)
    with open(imagename, 'wb') as f:
        f.write(base64.b64decode(res['result']))


req_mulLine(url='',data='',imagename='test1.png')