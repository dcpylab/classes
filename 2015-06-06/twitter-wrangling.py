#!/usr/bin/env python
from __future__ import print_function
import sys
if sys.version_info[0] == 3:
    import urllib.request as urlopen
else:
    import urllib2 as urlopen
import json
import pprint
import collections

# this is a comment
DATA_URL = "https://ceraweek2015.shore.uno/api/entries/?limit=3000&type%3Agroups=all-delegates&date-from=1429480800000&date-to=1429912800000&format=json"

response = urlopen.urlopen(DATA_URL)
raw_data = response.read()
decoded_data = raw_data.decode("utf8")
data = json.loads(decoded_data)

print("We have", len(data), "entries to analyze")
# pprint.pprint(data[0])

seen_names = collections.Counter()
for tweet in data:
    user_data = tweet["user"]
    display_name = user_data["displayname"]
    seen_names[display_name] += 1

for name, count in seen_names.most_common(10):
    print(name, ":", count)
