#
# scrape the DailyProgrammer subreddit
#
import re
import sys
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

target_url = 'https://www.reddit.com/r/DailyProgrammer/'
# we need to pretend that we are a web browser, otherwise
# reddit blocks our requests
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'
hdrs = {'User-Agent': user_agent}
req = Request(target_url, headers=hdrs)

result = urlopen(req)
code = result.getcode()
if code != 200:
    print("Error! Code:", code)
    sys.exit(1)

data = result.read().decode('utf8')
matches = re.findall(r'<a[^>]*?>[^<]*?\[Easy\][^<]*</a>', data)
for m in matches:
    print(m)
