#!/usr/bin/env python
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

url = "https://www.reddit.com/r/dailyprogrammer.json"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
hdrs = {'User-Agent': user_agent}
req = Request(url, headers=hdrs)
response = urlopen(req)
raw_content = response.read().decode('utf8')
data = json.loads(raw_content)

items = data['data']['children']
for item in items:
    content = item['data']
    title = content['title']
    if '[Easy]' in title:
        print(title, content['url'])