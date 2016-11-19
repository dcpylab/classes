"""
    ### Pylab 19 Nov 2016
    "Does the Washington Post fact checking hold up over time?"

    We're going to be looking at one of looking at the data sources for
    the WP's Fact Checker story: "Giuliani’s claim the White House invited
    Al Sharpton up to 85 times" and see if we can basically recreate their
    process for 2015 and 2016. Does their fact-checker hold up over time?

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

data_files ={
    "whitehouse_waves-2015_12.csv.zip":"https://www.whitehouse.gov/sites/default/files/disclosures/whitehouse_waves-2015_12.csv_.zip",
    "whitehouse_waves-2016_10.csv.zip": "https://www.whitehouse.gov/sites/default/files/disclosures/whitehouse_waves-2016_10.csv_.zip"
    }

def file_downloader_and_unzipper(filename, url):
    """Downloads and names a file given a filename and url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        file_location = os.path.realpath(filename)
        print('File: %s is located: %s' % (filename, file_location))

        # ToDo
        # Unzip file and extract in current working directory


if __name__ == '__main__':

    #### Hello world! #####
    print('hello world!')

    #### after hello world, uncomment below
    for filename, url in data_files.items():
        file_downloader_and_unzipper(filename, url)
