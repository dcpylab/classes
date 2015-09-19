# goo.gl/LYa7h3
# PYlab 2015-0919 
# 
# session led by Nathan Danielsen

# Starter Code
import os
import urllib
import csv

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/daily-show-guests/daily_show_guests.csv'

filename = 'daily_show_guests.csv'

if not os.path.isfile(filename):

    urllib.urlretrieve(url, filename)
    # use requests if you have pip on your machine

else:
    # print 'already here: ', filename
    pass

# print('hello world!!!')

data = []

with open(filename, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        data.append(row)

header = data[0]

rows =  data[1:]

# How many actors and actresses are in the data set?

print header # ['YEAR', 'GoogleKnowlege_Occupation', 'Show', 'Group', 'Raw_Guest_List']

num_actors = 0

for row in rows:
    year, occuptation, show, group, guests = row

    if occuptation == 'actor':
        num_actors += 1

    elif 'actor' in occuptation.split():
        num_actors += 1

    elif occuptation == 'actress':
        num_actors += 1
    
    elif 'actress' in occuptation.split():
        num_actors += 1

# How many occupations are in this dataset?

list_occuptations = []

for row in rows:
    year, occuptation, show, group, guests = row
    occuptation = occuptation.lower()
    list_occuptations.append(occuptation)

# print set(list_occuptations)

set_occuptions = set()

for row in rows:
    year, occuptation, show, group, guests = row
    occuptation = occuptation.lower()
    set_occuptions.add(occuptation)

# print set_occuptions


# how many different occupdations are in this dataset?

occuptation_dict = {}

for row in rows:
    year, occuptation, show, group, guests = row

    if occuptation in occuptation_dict.keys():
        occuptation_dict[occuptation] += 1
    
    else:
        occuptation_dict[occuptation] = 1

# print occuptation_dict

from collections import Counter

c = Counter()

for row in rows:
    year, occuptation, show, group, guests = row
    occuptation = occuptation.lower()
    c[occuptation] += 1

# print c 

# from collections import Counter

# c = Counter(occuptation for year, occuptation, show, group, guests in rows )

# print c


# list_occuptations = []

# for row in rows:
#     year, occuptation, show, group, guests = row
#     occuptation = occuptation.lower()
#     list_occuptations.append(occuptation)

# ### list comprehension (evquilant to above)

# print [occuptation.lower() for year, occuptation, show, group, guests in rows ]

# from collections import Counter

# c = Counter(occuptation.lower() for year, occuptation, show, group, guests in rows )

# print c.most_common(5)



from collections import Counter

c = Counter(guests.lower() for year, occuptation, show, group, guests in rows )

# print c.most_common(5)

#### Quesiton: for each occupation, what are the names of the people who have appeared?


from collections import defaultdict

d = defaultdict(list)


for row in rows:
    year, occuptation, show, group, guests = row

    d[occuptation].append(guests)


print d['actor']








