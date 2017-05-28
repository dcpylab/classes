import json
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

demo_key = "e1eee2b5677f408da40af8480a5fd5a8"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
hdrs = {'api_key': demo_key}
request = Request(incidents_url,
                  headers=hdrs)
response = urlopen(request)
raw_response = response.read().decode('utf8')
data = json.loads(raw_response)

incidents = data['ElevatorIncidents']
for i in incidents:
    station_name = i['StationName']
    station_code = i['StationCode']
    print(station_name, station_code)
