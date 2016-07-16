# Simple script to query the WMATA API and
# find out how many elevators are out of
# service on the Green Line today.

# For convenience and not having to install things, we
# use the standard library's URL-opening functions. In
# Python 2 this is `urllib2`, and in Python 3 this is
# `urllib.request`
import json
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

demo_key = '6b700f7ea9db408e9745c207da7ca827'
incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'

hdrs = {'api_key': demo_key}
req = Request(incidents_url, headers=hdrs)

result = urlopen(req)
raw_data = result.read()
data = json.loads(raw_data.decode('utf8'))
incidents = data['ElevatorIncidents']
names = set()
for i in incidents:
    station_name = i['StationName']
    names.add(station_name)

print(len(incidents))
print(len(names))
