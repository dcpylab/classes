#
# Script to scrape the `reddit.com/r/DailyProgrammer`
# subreddit and list all the 'Easy' challenges
#
import json
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

url = 'https://www.reddit.com/r/dailyprogrammer.json'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0'
hdrs = {'User-Agent': user_agent}
req = Request(url, headers=hdrs)
result = urlopen(req)
# we need `.decode('utf8')` to interpret the raw data
# as text -- look up UTF-8 for more details
raw_data = result.read().decode('utf8')
json_data = json.loads(raw_data)
challenges = json_data['data']['children']

for c in challenges:
    if 'Easy' in c['data']['title']:
        print(c['data']['title'], c['data']['url'])
