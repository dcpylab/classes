# talk to the wmata API, ask it how 
# many elevators are out of service on the green line
demo_key = "e13626d03d8e4c03ac07f95541b3091b"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

import json
from urllib.request import urlopen, Request

req = Request(incidents_url, headers={"api_key": demo_key})
result = urlopen(req)
raw_data = result.read()
data = json.loads(raw_data)

incidents = data["ElevatorIncidents"]
for incident in incidents:
    type_of_incident = incident["UnitType"]
    if type_of_incident == "ELEVATOR":
        print(incident)


