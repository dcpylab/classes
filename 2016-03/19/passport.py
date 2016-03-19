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
    # print('File {fn} opened. Time to get to work.'.format(fn=validpassport_json))

# print(type(data)) ### it's a list

# print(type(data[0])) ### it's a dictionary

# print(dir(data[0])) ### What is the director of methods and property of the object.

# print(type(data[0].keys()[0])) 

### Questions

### What data type is 'data'? What operations can we do on it?

# print(type(data)) ### it's a list



### How many years are in this dataset?

# print(len(data))

### What is the total number of passports issues in this data set?


# print(data[0]['Count'])

# total = 0

# for year_dict in data:
#     total += year_dict['Count']

# print(total)

### What is the average passports issues per year?


# average = total / len(data)

# print(average)

### What is number of passports issues in the last ten years? 


total = 0

for year_dict in data:
    if year_dict['Year'] > 2002: #the year is greater than 2002:
        total += year_dict['Count']

# print(total)

### Since 2001, has the average number of passports increased or decreased since then?


### go through all the year

before_total = 0
before_count = 0

after_total = 0
after_count = 0

for year_dict in data:

    #### if the year is before 2001, then count it
    if year_dict["Year"] < 2001:
        before_total += year_dict['Count']
        before_count += 1

    #### else if it is after, then count it
    else: 
        after_total += year_dict['Count']
        after_count += 1

# print(after_total/ after_count )

# print(before_total/ before_count )


# PART II

"""
USAcceptanceFacilities for passports
https://catalog.data.gov/dataset/usacceptancefacilities
"""

url2 = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json'


### Write a small script to save this json file to a file. (hint look at code above)
### Advanced: can you write this script as a function? (code reuser)

def add_numbers(num1, num2):
    return num1 + num2

def json_saver(url, filename):
    """
    Input: Takes in a url and a filename

    Something happens

    Output: Returns a list of dictionaries. 
    """

    if not os.path.isfile(filename):
        with urlopen(url) as f:
            text = f.read()
            decoded_text = text.decode('utf8')
            data =  json.loads(decoded_text)
        print('Requested JSON and converted to python dictionary')

        with open(filename, 'w+') as f:
            json.dump(data, f)
        print('Saved JSON to file')

    else:
        with open(filename, 'r+') as f:
            data = json.load(f)
    return data

data = json_saver(url2, 'passportfacilitites.json')


### How many facilities are in this dataset?

print(len(data))

### How many states or teritories? 


from collections import Counter


lst = [facility_dict['StateCode'] for facility_dict in data]

c = Counter(lst)

print(c)

### Ask a question of this data. 


### can you convert this to a csv file and create a map using Google maps?
### https://www.google.com/maps/d/u/0/?hl=en_US&app=mp


