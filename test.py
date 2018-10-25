from datetime import datetime

# now=datetime.now().timestamp()
# now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# data={'OLname':'','LRtime':now,'state':0}
# print(data)

import requests

res=requests.get('http://xuyuhan.oss-cn-shanghai.aliyuncs.com/flare.json')
print(res.text)

