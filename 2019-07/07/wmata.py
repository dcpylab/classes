from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json

API_ACCESS_TOKEN = '7a28147b7bc643b8a6bfe2c55c680c27'

headers = {'api_key': API_ACCESS_TOKEN}

endpoint = {
	'lines': 'https://api.wmata.com/Rail.svc/json/jLines',
	'stations': 'https://api.wmata.com/Rail.svc/json/jStations?%s'
}

def get_lines():
	""" 
	Return a list of metro lines as a list of dictionaries.
	"""
	request = Request(endpoint['lines'], headers=headers)
	response = urlopen(request)
	contents = response.read()
	contents_json = json.loads(contents)
	return contents_json['Lines']
	
def get_stations(line_code):
	"""Given a line_code, return the list of stations for that line."""
	params = {'LineCode': line_code}
	url_encoded_params = urlencode(params)
	request = Request(
		endpoint['stations'] % url_encoded_params,
		headers=headers
	)
	response = urlopen(request)
	contents = response.read()
	contents_json = json.loads(contents)
	return contents_json['Stations']

lines = get_lines()
stations = get_stations('YL')

print("Lines:\n", lines)
print("Stations:\n", stations)
