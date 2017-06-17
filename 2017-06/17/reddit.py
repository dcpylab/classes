# Scraper to look at the "Daily Programmer"
# subreddit and return a list of the "Easy"
# challenges there.
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

user_agent_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0"
custom_headers = {"user-agent": user_agent_string}
req = Request("http://www.reddit.com",
              headers=custom_headers)
reddit_page = urlopen(req)
reddit_page_content = reddit_page.read().decode('utf8')
print(reddit_page_content)
