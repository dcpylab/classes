
# PYlab 2015-1017
# session led by Nathan Danielsen
# Article: http://fivethirtyeight.com/features/fandango-movies-ratings/
# DATA Source https://github.com/fivethirtyeight/data/tree/master/fandango



# Starter Code

import os 
import urllib
import csv

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/fandango/fandango_scrape.csv'

filename = 'fandango_scrape.csv'

if not os.path.isfile(filename):

    urllib.urlretrieve(url, filename)
    # use requests if you have pip on your machine

else:
    pass

# raw_data = []

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    raw_data = list(reader)


    # for row in reader:
    #     raw_data.append(row)

# print raw_data
header = raw_data[0]
rows = raw_data[1:]

# What are data types for each column?

print row[0]













