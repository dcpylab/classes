"""
    What do people think about the oxford comma?

    We're going to be looking at a fivethirtyeight poll of the use of the oxford comma.

    ###### Story:
    https://fivethirtyeight.com/datalab/elitist-superfluous-or-popular-we-polled-americans-on-the-oxford-comma/

    ###### Data:
    https://raw.githubusercontent.com/fivethirtyeight/data/master/comma-survey-data/comma-survey-data.csv

    Contact me:
    Nathan @nate_somewhere

    More learning resources at:
    https://github.com/ndanielsen/beginning-python
"""
from __future__ import print_function
import os
import csv

try:
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability

def file_downloader(filename, url):
    """Downloads and names a file given a filename and url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        file_location = os.path.realpath(filename)
        print('File is located: %s' % (file_location))

if __name__ == '__main__':
    print('Hello world')

    # file_downloader('comma-survey-data.csv', 'https://raw.githubusercontent.com/fivethirtyeight/data/master/comma-survey-data/comma-survey-data.csv')
