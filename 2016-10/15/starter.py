"""
    Pylab 15 Oct 2016
    "How many babies are born on Feb 29th?"
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

if __name__ == '__main__':
    file_downloader(url_csv, csv_filename)
