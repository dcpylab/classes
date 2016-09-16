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
        print('File: %s present and ready to go!' % filename)

def csv_file_opener(filename):
    "Opens csv file and returns a list of dictionaries"
    # Hint: https://docs.python.org/3/library/csv.html#csv.DictReader
    pass

# if file is the main one being executed.
if __name__ == '__main__':
    file_downloader(parkings_violation)
    file_downloader(block_centroids)


    # ToDo

    # created a joined table on STREETSEGID

    # count and filter until we have some answers
