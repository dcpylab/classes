#!/usr/bin/env python
"""
Quick and dirty script to demonstrate pulling some data
from the WMATA API

From class on 2015-03-28
"""

API_KEY = 'kfgpmgvfgacx98de9q3xazww'  # WMATA demo key
REQUEST_URI = ('https://api.wmata.com/StationPrediction.svc/json/' +
               'GetPrediction/{StationCodes}?api_key={API_KEY}')

from urllib2 import urlopen
import json

url = REQUEST_URI.format(StationCodes='All', API_KEY=API_KEY)
print "Requesting:", url

response = urlopen(url)
if response.getcode() != 200:
    raise AssertionError("Did not return a successful response!")

response_json = response.read()
response_data = json.loads(response_json)

trains = response_data['Trains']

trains_at_metro_center = [t for t in trains
                          if t['LocationName'] == 'Metro Center']

for t in trains_at_metro_center:
    print t['Line'], "\t", t['Min'], "\t", t['DestinationName']
