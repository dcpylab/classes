
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

# print row[0]


# how many films from 2015?

# print len(rows)


films_2015 = []

for row in rows:
    film, stars, rating, votes = row
    if '(2015)' in film:
        films_2015.append(film)

# print len(films_2015)





### DATA CHECK 1
"""
Of the 437 films with at least one review, 
98 percent had a 3-star rating or higher and 
75 percent had a 4-star rating or higher.
"""

temp_list = []

for row in rows:
    film, stars, rating, votes = row
    votes = int(votes)
    if votes > 0:
        temp_list.append(row)

total = float(len(temp_list))

# print rows[0]
"""
98 percent had a 3-star rating or higher and 
75 percent had a 4-star rating or higher.
"""


threestar = 0
fourstar = 0

for row in temp_list:
    film, stars, rating, votes = row
    stars = float(stars)
    if stars >= 3:
        threestar += 1
    if stars >= 4:
        fourstar += 1

print threestar / total
print fourstar / total









