"""
    Pylab 17 Sept 2016
    "Which city block in DC received the most parking tickets in May 2016?"
    Nathan @nate_somewhere

    Class notes:

    Python3 required
    Internet connection required
    Text editor required
"""


import os
from urllib.request import urlretrieve

def pagename_to_filename(pagename, extension=".csv"):
    "changes pagename to filename with extension"
    filename_wo_extension = '_'.join(w.lower() for w in pagename.split())
    return filename_wo_extension + extension

def file_downloader(file_tuple):
    "Downloads and names a file given a tuple in the format (filename, download_url)"
    pagename, url = file_tuple
    filename = pagename_to_filename(pagename)

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    else:
        print('File: %s present and ready to go!' % filename)

import csv

def csv_file_opener(filename):
    "Opens csv file and returns a list of dictionaries"
    # Hint: https://docs.python.org/3/library/csv.html#csv.DictReader
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# if file is the main one being executed.
if __name__ == '__main__':

    parkings_violation = ("Parking Violations in May 2016", "http://opendata.dc.gov/datasets/b86079c597e14bc199f2fff0025a1f77_4.csv")
    block_centroids = ("Block Centroids", "http://opendata.dc.gov/datasets/ba2539327dcf448789dc65a55ebe3d16_5.csv")
    # file_downloader(parkings_violation)
    # file_downloader(block_centroids)

    data = csv_file_opener('parking_violations_in_may_2016.csv')

    from pprint import pprint
    # pprint(data)

    ticket_counter = {}

    for ticket in data:
        location_name = ticket['LOCATION']

        if location_name in ticket_counter.keys():
            ticket_counter[location_name] += 1

        else: # does not exist
            ticket_counter[location_name] = 1

    # pprint(ticket_counter)
    # sort from biggest to smallest

    ticket_tuple = list(ticket_counter.items())

    sorted_tickets = sorted(ticket_tuple, key=lambda x: x[1], reverse=True)

    def sort_tickets(x):
        return x[1]

    pprint(sorted_tickets[:10])



        # if
        # else



    # example_list = [1, 2, 3, 4, 5]
    # example_dict = {1: "some value", 'avalue': "another value", ('one', 'another'): 1}
    # parking_page_name = parkings_violation[0]

    # ToDo

    # created a joined table on STREETSEGID

    # count and filter until we have some answers
