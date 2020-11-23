import json
import requests

url = 'http://127.0.0.1:5000/Line/norline'
data = {'xaxis': ["6月", "7月", "8月", "9月", "10月", "11月"],'typelist':['商家A'],'yaxis':[268, 278, 369, 310, 504, 1056],'maintitle':'销量图','mintitle':'小标题'}
r = requests.get(url, data=json.dumps(data))
print(r.text)