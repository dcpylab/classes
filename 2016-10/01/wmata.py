# Simple script to find the number of elevators
# out of service on the Green Line using the WMATA API
import json
# now some magic to paper over differences between Python
# 2 and Python 3
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

demo_key = "6b700f7ea9db408e9745c207da7ca827"
elevator_incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"

target_url = elevator_incidents_url + '?api_key=' + demo_key
response = urlopen(target_url)
raw_data = response.read().decode('utf8')  # python 3
data = json.loads(raw_data)
list_of_incidents = data['ElevatorIncidents']

elevator_incidents = []
for i in list_of_incidents:
    if i['UnitType'] == 'ELEVATOR':
        elevator_incidents.append(i)

# elevator_incidents = [i for i in list_of_incidents if i['UnitType'] == 'ELEVATOR']

print('there were', len(elevator_incidents), 'incidents')
print(elevator_incidents[0])
