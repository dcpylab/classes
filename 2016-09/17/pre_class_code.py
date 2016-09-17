"""
    Pylab 17 Sept 2016
    "Which block in DC received the most parking tickets in May 2016?"
    Nathan

    Class notes:

    Python3 required
    Internet connection required
    Text editor required
"""


import os
import csv
from urllib.request import urlretrieve

parkings_violation = ("Parking Violations in May 2016", "http://opendata.dc.gov/datasets/b86079c597e14bc199f2fff0025a1f77_4.csv")
block_centroids = ("Block Centroids", "http://opendata.dc.gov/datasets/ba2539327dcf448789dc65a55ebe3d16_5.csv")


def pagename_to_filename(pagename, extension=".csv"):
    "Confirms pagename to filename without "
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
        # print('File: %s present and ready to go!' % filename)
        pass

def csv_file_opener(filename):
    "Opens csv file and returns a list of dictionaries"
    # Hint: https://docs.python.org/3/library/csv.html#csv.DictReader
    # watch out for the BOM
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# if file is the main one being executed.
if __name__ == '__main__':
    file_downloader(parkings_violation)
    file_downloader(block_centroids)

    ## test_page_name_works
    test_page_name = "Test Page Name"
    assert pagename_to_filename(test_page_name) == 'test_page_name.csv'

    parking_file = pagename_to_filename(parkings_violation[0])
    block_file = pagename_to_filename(block_centroids[0])

    parking_data = csv_file_opener(parking_file)

    from pprint import pprint
    # pprint(parking_data)

    from collections import Counter
    count_street_ids = Counter(ticket['STREETSEGID'] for ticket in parking_data)
    # pprint(count_street_ids.most_common(10))

    empty = [ticket for ticket in parking_data if ticket['STREETSEGID'] == '' ]
    # pprint(empty)
    # might want to take a look here: http://opendata.dc.gov/datasets/aa514416aaf74fdc94748f1e56e7cc8a_0

    # drop the empty ones ---
    del count_street_ids['']

    block_data = csv_file_opener(block_file)
    # pprint(parking_data)
    dict_street_ids_counts = dict(count_street_ids)

    # pprint(dict_street_ids_counts)

    for street in block_data:
        street_id = street['STREETSEGID']
        # mapping = dict_street_ids_counts[street_id]
        # print(mapping)
        get_count = dict_street_ids_counts.get(street_id, 0)
        street['COUNT'] = get_count

    ## let's take a look to see if we have any duplicates
    # c = Counter(street['STREETSEGID'] for street in block_data)
    # pprint(c.most_common(5))

    # let's do redo in a simple way to avoid duplicates

    unique_block_data = []
    already_seen_streed_ids = set()

    for street in block_data:
        street_id = street['STREETSEGID']
        # mapping = dict_street_ids_counts[street_id]
        # print(mapping)
        if not street_id in already_seen_streed_ids:
            get_count = dict_street_ids_counts.get(street_id, 0)
            street['COUNT'] = get_count
            unique_block_data.append(street)
            already_seen_streed_ids.add(street_id)


    ## let's take a look to see if we have any duplicates
    c = Counter(street['STREETSEGID'] for street in unique_block_data)
    # pprint(c.most_common(5))


    def sort_block_data_count(block_element):
        return block_element.get('COUNT', 0)

    blocked_data_sorted = sorted(unique_block_data, key=sort_block_data_count, reverse=True)

    # lambda function
    # blocked_data_sorted = sorted(block_data, key=lambda k: k.get('COUNT', 0), reverse=True)

    # pprint(blocked_data_sorted[:10])

    top_locations_readable = [[block['BLOCKNAME'], block['COUNT']] for block in blocked_data_sorted[:10]]


    top_locations_to_map = [[block['BLOCKNAME'], block['COUNT'], block['X'], block['Y'] ] for block in blocked_data_sorted[:10]]
    top_locations_to_map.insert(0 ,['BLOCKNAME', 'COUNT', 'X', 'Y'])
    pprint(top_locations_to_map)

    with open("top_ticket_locations.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(top_locations_to_map)

    # use google maps:
    # https://www.google.com/maps/d/u/0/viewer?mid=1WwqeHj2jk7zQPTqU2xV3iRdLoT8
