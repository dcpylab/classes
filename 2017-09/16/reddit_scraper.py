from __future__ import print_function
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request
import json

user_agent = 'Mozilla/5.0 (X11; CrOS x86_64 9901.12.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.18 Safari/537.36'
reddit_url = 'https://www.reddit.com/r/dailyprogrammer.json'
hdrs = {'User-Agent': user_agent}
reddit_request = Request(reddit_url, headers=hdrs)

reddit_page = urlopen(reddit_request)
content = reddit_page.read().decode('utf8')
data = json.loads(content)

items = data['data']['children']
for i in items:
    item_data = i['data']
    title = item_data['title']
    url = item_data['url']
    if '[Easy]' in title:
        print(title, url)
