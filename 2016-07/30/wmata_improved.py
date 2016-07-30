'''
Simple script to find out the number of
elevators out of service on the Green Line
today, using the WMATA API
'''
import json
try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import urlopen, Request
    from urllib import urlencode

API_KEY = '6b700f7ea9db408e9745c207da7ca827'


def make_api_request(url, params=None):
    if params:
        encoded_params = urlencode(params)
        if url.endswith('?'):
            url += '&' + encoded_params
        else:
            url += '?' + encoded_params

    headers = {'api_key': API_KEY}
    request = Request(url, headers=headers)
    result = urlopen(request)
    if result.getcode() != 200:
        raise AssertionError(result.getcode())

    raw_data = result.read().decode('utf8')
    data = json.loads(raw_data)
    return data

station_list_url = 'https://api.wmata.com/Rail.svc/json/jStations'
station_list_data = make_api_request(station_list_url, {'LineCode': 'GR'})
stations = station_list_data['Stations']
station_codes = set(s['Code'] for s in stations)

incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
incidents_data = make_api_request(incidents_url)
incidents = incidents_data['ElevatorIncidents']

for i in incidents:
    if i['UnitType'] == 'ELEVATOR' and i['StationCode'] in station_codes:
        print(i)
