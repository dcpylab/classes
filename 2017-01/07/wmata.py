#
# Simple script to talk to the WMATA API
# and tell us how many elevators are out
# of service on the Green Line
#
demo_key = "6b700f7ea9db408e9745c207da7ca827"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"  # [?StationCode]"

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import json

hdrs = {'api_key': demo_key}
request = Request(incidents_url, headers=hdrs)
response = urlopen(request)
raw_data = response.read()
text_data = raw_data.decode('utf8')
data = json.loads(text_data)

incidents = data['ElevatorIncidents']
for incident in incidents:
    if incident['UnitType'] == 'ELEVATOR':
        print(incident)
