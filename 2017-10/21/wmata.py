import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

demo_key = "e1eee2b5677f408da40af8480a5fd5a8"
hdrs = {'api_key': demo_key}
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
# developer.wmata.com -- click on "Try us out"
req = Request(incidents_url, headers=hdrs)
result = urlopen(req)
raw_content = result.read()
content = raw_content.decode('utf8')
data = json.loads(content)

incidents = data["ElevatorIncidents"]
for i in incidents:
    unit_type = i["UnitType"]
    if unit_type == "ELEVATOR":
        station_name = i["StationName"]
        station_code = i["StationCode"]
        print(station_name, station_code)