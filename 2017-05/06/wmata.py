#!/usr/bin/env python
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
demo_key = "e1eee2b5677f408da40af8480a5fd5a8"

header_data = {'api_key': demo_key}
req = Request(incidents_url, headers=header_data)
result = urlopen(req)
raw_data = result.read().decode('utf8')

data = json.loads(raw_data)
incidents = data['ElevatorIncidents']

for i in incidents:
    print(i['StationName'])
