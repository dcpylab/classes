# simple program to ask the WMATA API how many
# elevators are out of service on the green line
# today
# step 0: get a key from http://developer.wmata.com

demo_key = "6b700f7ea9db408e9745c207da7ca827"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

headers = {'api_key': demo_key}
request = Request(incidents_url, headers=headers)
result = urlopen(request)
raw_data = result.read().decode('utf8')
incident_data = json.loads(raw_data)

# here we request station information so we can
# find incidents on the green line
station_info_url = "https://api.wmata.com/Rail.svc/json/jStations?LineCode=GR"
request = Request(station_info_url, headers=headers)
result = urlopen(request)
raw_data = result.read().decode('utf8')
station_data = json.loads(raw_data)

station_codes = []
stations = station_data['Stations']
for station in stations:
    station_codes.append(station['Code'])

incidents = incident_data['ElevatorIncidents']
for incident in incidents:
    unit_type = incident['UnitType']
    station_code = incident['StationCode']
    if unit_type == 'ELEVATOR' and station_code in station_codes:
        print(incident['StationName'],
              incident['StationCode'])
