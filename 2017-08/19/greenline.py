#
# Simple script to ask WMATA how many
# elevators are out of service on the
# Green Line today
#
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import json

demo_key = "e1eee2b5677f408da40af8480a5fd5a8"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

our_headers = {'api_key': demo_key}
req = Request(incidents_url, headers=our_headers)
result = urlopen(req)

content = result.read()
str_content = content.decode('utf8')
data = json.loads(str_content)
incidents = data['ElevatorIncidents']

for i in incidents:
    if i['UnitType'] == 'ELEVATOR':
        print(i['StationName'],
              i['LocationDescription'])
