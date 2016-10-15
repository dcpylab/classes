"""
    Pylab 15 Oct 2016
    "How many babies are born on Feb 29th?"

    We're going to be looking at the data behind these stories and see if it adds up:

    http://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/
    http://fivethirtyeight.com/features/lots-of-parents-dont-want-their-kids-to-be-born-on-leap-day/

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""


import os
import csv

try:
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability

url_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv"
csv_filename = "US_births_2000-2014_SSA.csv"

def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        print('File: %s present and ready to go!' % filename)

# if __name__ == '__main__':
#     file_downloader(url_csv, csv_filename)


import csv

with open(csv_filename, 'r') as file_object:
    reader = csv.reader(file_object)
    data = list(reader)

    #### header row = year,month,date_of_month,day_of_week,births
    # for row in data[1:]:
    #     month = row[1]
    #     date_of_month = row[2]
    #     if month == "2" and date_of_month == "29":
    #         print(row)

    leap_years = ['2000', '2004', '2008', '2012']

    twenty_eight, twenty_nine, first = 0, 0, 0

    for row in data[1:]:
        year = row[0]
        month = row[1]
        date_of_month = row[2]
        birth_count = row[4]
        if year in leap_years:
            if month == "2" and date_of_month == "29":
                twenty_nine += int(birth_count)

            elif month == "2" and date_of_month == "28":
                twenty_eight  += int(birth_count)
                
            elif month == "3" and date_of_month == "1":
                first += int(birth_count)
    print("Total births on twenty eights of Feb: %s" % twenty_eight)
    print("Total births on twenty nine of Feb: %s" % twenty_nine)
    print("Total births on first of March: %s" % first)


# TO DO

# Open the CSV FILE


# COUNT all births on the February 28th, 29th and March 1st
