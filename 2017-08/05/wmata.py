#
# Simple script to talk to WMATA's API and
# tell us how many elevators are out of service
# on the Green Line today.
#
from __future__ import print_function
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

demo_key = "e1eee2b5677f408da40af8480a5fd5a8"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

hdrs = {'api_key': demo_key, 'favorite_color': 'Forest Green'}
req = Request(incidents_url, headers=hdrs)
result = urlopen(req)
contents = result.read().decode('utf8')
data = json.loads(contents)

incidents = data['ElevatorIncidents']
for incident in incidents:
    if incident['UnitType'] == 'ELEVATOR':
        print(incident['StationName'],
              incident['LocationDescription'])
