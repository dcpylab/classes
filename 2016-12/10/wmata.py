import json
# Allow making web requests whether in Python 2 or 3
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

demo_key = "6b700f7ea9db408e9745c207da7ca827"
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

hdrs = {"api_key": demo_key}
req = Request(incidents_url, headers=hdrs)

response = urlopen(req)
# Pull data out of the response -- see https://docs.python.org/3/library/urllib.request.html
# for details
data = response.read()
# `.read()` returns a bytestring, we just assume it's UTF-8
# because it's 2016 dammit
data = data.decode('utf8')
# Parse the data as JSON
json_data = json.loads(data)
# Extract incidents from our parsed data
incidents = json_data["ElevatorIncidents"]
# TODO: Filter out incidents that are not on the Green Line.
for incident in incidents:
    if incident["UnitType"] == "ELEVATOR":
        print(incident["StationName"])
