#
# Scrape the Washington Metro API
#
import json

demo_key = '6b700f7ea9db408e9745c207da7ca827'
url = 'https://api.wmata.com/Incidents.svc/json/Incidents'

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

headers = {
    'api_key': demo_key,
    'User-Agent': 'testscript 001',
}

request = Request(url, headers=headers)
response = urlopen(request)
if response.getcode() != 200:
    # a status code of 200 means it was OK
    print("Something went wrong! We got a status code of:", response.getcode())

raw_response_content = response.read()
response_content = raw_response_content.decode('utf8')
data = json.loads(response_content)

incidents = data['Incidents']
incidents_on_green_line = [x for x in incidents if 'GR' in x['LinesAffected']]
descriptions_on_green_line = [x['Description'] for x in incidents_on_green_line]
# descriptions_on_green_line = [x['Description'] for x in incidents if 'GR' in x['LinesAffected']]
for i in incidents_on_green_line:
    print(i['Description'])
