import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


demo_key = "e1eee2b5677f408da40af8480a5fd5a8"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
hdrs = {'api_key': demo_key}
req = Request(incidents_url, headers=hdrs)
result = urlopen(req)
raw_data = result.read().decode('utf8')
data = json.loads(raw_data)
incidents = data["ElevatorIncidents"]

for i in incidents:
    if i["UnitType"] == "ELEVATOR":
        print(i["StationName"], i["DateOutOfServ"], i["TimeOutOfService"], i["StationCode"])
