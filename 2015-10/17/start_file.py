
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

if __name__ == '__main__':

    print "Hello PYlab"