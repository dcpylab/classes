#!/usr/bin/env python
#
# Simple WMATA API script -- we want to find out
# the number of elevators out of service on the Green Line
#
import json
try:
    from urllib2 import urlopen, Request
    from urllib import urlencode
except ImportError:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode


def get_wmata_info(url, params=None):
    demo_api_key = '6b700f7ea9db408e9745c207da7ca827'
    hdrs = {'api_key': demo_api_key}
    if params != None:
        encoded_params = urlencode(params)
        url = url + "?" + encoded_params
    request = Request(url, headers=hdrs)
    result = urlopen(request)
    raw_data = result.read()
    data = json.loads(raw_data.decode('utf8'))
    return data


incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
incidents_data = get_wmata_info(incidents_url)

list_of_incidents = incidents_data['ElevatorIncidents']

station_list_url = 'https://api.wmata.com/Rail.svc/json/jStations'  # ?LineCode
stations_data = get_wmata_info(station_list_url, {'LineCode': 'GR'})
list_of_stations = stations_data['Stations']

station_codes_on_green_line = set()
for station in list_of_stations:
    code = station['Code']
    station_codes_on_green_line.add(code)

for incident in list_of_incidents:
    if incident['UnitType'] == 'ELEVATOR' and incident['StationCode'] in station_codes_on_green_line:
        print(incident['StationName'], incident['LocationDescription'])
