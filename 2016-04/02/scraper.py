#
# Scrape the DailyProgrammer subreddit (/r/DailyProgrammer)
# for all the "easy" challenges.
#
from __future__ import print_function
import sys
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

url = 'https://www.reddit.com/r/DailyProgrammer/new.json'
user_agent_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'

req = Request(url, headers={'User-Agent': user_agent_string})
response = urlopen(req)

if response.getcode() != 200:
    print("Something went wrong:", response.code)
    sys.exit()

contents = response.read()
data = json.loads(contents.decode('utf8'))

posts = data['data']['children']
easy_posts = []

for p in posts:
    post_data = p['data']
    post_title = post_data['title']
    if 'Easy' in post_title:
        easy_posts.append(post_data)

# easy_posts = [p['data'] for p in posts
#               if 'Easy' in p['data']['title']]

for p in easy_posts:
    print(p['title'], ' - ', p['url'])
