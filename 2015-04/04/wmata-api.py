#!/usr/bin/env python2

API_KEY = 'kfgpmgvfgacx98de9q3xazww'
INCIDENTS_URL = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents?api_key={API_KEY}'

import urllib2 # requests is better, but urllib2 is built-in
import json
import time


class APIError(Exception):
    pass


def main():
    try:
        result = urllib2.urlopen(INCIDENTS_URL.format(API_KEY=API_KEY))
    except (urllib2.HTTPError, urllib2.URLError) as e:
        raise APIError(e)
    except:
        raise AssertionError("This should _really_ not happen")

    incidents_data = json.load(result)
    incidents = incidents_data['ElevatorIncidents']

    for inc in incidents:
        if inc['StationCode'] == 'D02':
            inc["WeCareAboutThis"] = True

    for inc in incidents:
        if inc.get('WeCareAboutThis', None):
            print inc['StationName']
            print inc['LocationDescription']
            print inc['SymptomDescription']
            print ""



if __name__ == '__main__':
    try:
        while True:
            main()
            time.sleep(2)
    except APIError:
        print "I'm sorry, we're having trouble connecting to WMATA."
        print "We apologise for the inconvenience."
    # except:
    #     print "Your code is broken. Please fix it."
