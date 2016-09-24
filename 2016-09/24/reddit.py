#
# Scrape the /r/DailyProgrammer subreddit, and return a list
# of all the Easy tasks, with links to them
#
from __future__ import print_function
try:
    from urllib2 import Request, urlopen
except ImportError:  # we're using Python 3
    from urllib.request import Request, urlopen
import json

reddit_url = 'https://www.reddit.com/r/DailyProgrammer.json'
user_agent_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0'
my_headers = {'User-Agent': user_agent_string}
# customize the HTTP request we're going to make
request = Request(reddit_url, headers=my_headers)
response = urlopen(request)
# assume the response contains UTF-8 textual content
contents = response.read().decode('utf8')
data = json.loads(contents)
posts = data['data']['children']

for p in posts:
    p_data = p['data']
    p_title = p_data['title']
    p_url = p_data['url']
    if 'Easy' in p_title:
        print(p_title, '\n\t', p_url, '\n')
