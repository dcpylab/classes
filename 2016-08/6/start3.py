# goo.gl/LYa7h3
# PYlab 2015-0919
#
# session led by Nathan Danielsen
"""
Open DC Data - looking at Arts and Culture Organization 501(c)3 in the city
http://opendata.dc.gov/datasets/6321de8c38394f269937bb897f9a9853_52

Python 3
"""

# Starter Code
import os
import urllib.request
import csv

url = 'http://opendata.dc.gov/datasets/6321de8c38394f269937bb897f9a9853_52.csv'

filename = 'arts-and-culture-organizations.csv'

if not os.path.isfile(filename):

    urllib.request.urlretrieve(url, filename)
    # use requests if you have pip on your machine
else:
    # print 'already here: ', filename
    pass

# with open(filename, 'r') as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         print(row)
