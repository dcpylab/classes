"""
PyLab 19 March 2016

Analyzing JSON and US Passport Data with python3

Valid passportIssuanceByCalendarYear 
https://catalog.data.gov/dataset/passportissuancebycalendaryear
"""

#### Imports

import os
import json
try:
    from urllib.request import urlopen ## python3 

except ImportError:
    print('python2 alert')
    from urllib import urlopen ## python2

### Constants

url = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:56:10.098Z/validpassportsbyyear.json'
validpassport_json = 'validpassportsbyyear.json'

if not os.path.isfile(validpassport_json):
    with urlopen(url) as f:
        text = f.read()
        decoded_text = text.decode('utf8')
        data =  json.loads(decoded_text)
    print('Requested JSON and converted to python dictionary')

    with open(validpassport_json, 'w+') as f:
        json.dump(data, f)
    print('Saved JSON to file')

else:
    with open(validpassport_json, 'r+') as f:
        data = json.load(f)
    print('File {fn} opened. Time to get to work.'.format(fn=validpassport_json))


### Questions


### What data type is 'data'? What operations can we do on it?



### How many years are in this dataset?



### What is the total number of passports issues in this data set?



### What is number of passports issues in the last ten years? What is the average number issued per year since then?



### Since 2001, has the average number of passports increased or decreased since then?



# PART II

"""
USAcceptanceFacilities for passports
https://catalog.data.gov/dataset/usacceptancefacilities
"""

url2 = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json'


### Write a small script to save this json file to a file. (hint look at code above)
### Advanced: can you write this script as a function? (code reuser)


### How many facilities are in this dataset?


### How many states?


### Ask a question of this data. 


### can you convert this to a csv file and create a map using Google maps?
### https://www.google.com/maps/d/u/0/?hl=en_US&app=mp


