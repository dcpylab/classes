"""
    Pylab 5 Nov 2016
    "Doing Evil (statistical) work."

    We're going to be looking at the data behind this story and see if we can also make sweeping and probably wrong conclusions about nutrition-studies:

    Story:
    http://fivethirtyeight.com/features/you-cant-trust-what-you-read-about-nutrition/

    Github data repo:
    https://github.com/fivethirtyeight/data/tree/master/nutrition-studies

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required

    Contact me:
    Nathan @nate_somewhere

    More learning resources at:
    https://github.com/ndanielsen/beginning-python
"""


import os
import csv

try:
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability

url_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nutrition-studies/raw_anonymized_data.csv"
csv_filename = "raw_anonymized_data.csv"

def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        file_location = os.path.realpath(filename)
        print('File: %s is located: %s' % (filename, file_location))

if __name__ == '__main__':

    #### Hello world! #####
    print('hello world!')

    #### after hello world, uncomment below
    # file_downloader(url_csv, csv_filename)
