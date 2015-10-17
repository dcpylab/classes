import os 
import urllib
import csv

# write a function that 
# downloads a csv and returns the open csv file
# as a list of lists\

urlcsv = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/fandango/fandango_scrape.csv'

fandangocsv = 'fandango_scrape.csv'


def get_data(url=None, filename=None):
    """
    write a function that downloads a csv and returns the open csv file as a list of lists\
    """


    have_file_status = os.path.isfile(filename)

    if have_file_status:
        pass

    else:
        urllib.urlretrieve(url, filename)

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        raw_data = list(reader)
        return raw_data

print get_data(url=urlcsv, filename='awsomecsv.csv')


