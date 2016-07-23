# Simple scraper for DailyProgrammer subreddit
# that lists all the 'Easy' challenges, with links
# to them
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

json_url = 'https://www.reddit.com/r/DailyProgrammer/new.json'
user_agent_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'
hdrs = {'User-Agent': user_agent_string}
req = Request(json_url, headers=hdrs)
result = urlopen(req)
raw_data = result.read()
data = json.loads(raw_data.decode('utf8'))
sub_data = data['data']
sub_data_children = sub_data['children']

for child in sub_data_children:
    child_data = child['data']
    title = child_data['title']
    url = child_data['url']
    if '[Easy]' in title:
        print(title, url)
