#
# Script to scrape Reddit's '/r/DailyProgrammer' subreddit and extract the 'Easy'
# challenges, along with links to them
#
from __future__ import print_function
import re
from collections import defaultdict
import bs4
import requests

response = requests.get(
	'http://www.reddit.com/r/DailyProgrammer/',
	headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'})

print("We got {} cookies: ", len(response.cookies))
for c in response.cookies:
	print("\t", c)

soup = bs4.BeautifulSoup(response.content, 'html.parser')
link_tags = soup.find_all('a', 'title')
categories = defaultdict(list)
for link in link_tags:
	match = re.search("\[(\w+)\]", link.text)
	if match != None:
		category = match.group(1)
		categories[category].append(link)
	
for category in categories:
	links = categories[category]
	print(category, ":")
	for link in links:	
		print("\t", link.text, link.attrs['href'])



