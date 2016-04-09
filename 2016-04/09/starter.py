from __future__ import print_function

import os

try:
    from urllib.request import urlretrieve ## python3
except ImportError:
    print('python2 alert')
    from urllib import urlretrieve ## python2
"""
Pylab 09 April 2016

Analyzing Project Gutenberg's The Innocents Abroad, by Mark Twain (Samuel Clemens) with Python

# https://www.gutenberg.org/ebooks/3176

"""
# Constants

url = 'http://www.gutenberg.org/cache/epub/3176/pg3176.txt'
filename = 'innocents-abroad.txt'


# Setup taskes

# Open the file
# Print out file contents to terminal
# Inspect file structure and format


# Questions:

# 1. Using string slicing, what is the title of this book?




# 2. How many characters are in this txt file?




# 3. How many '\n' are in this text file? When is the first '\n'?




# 4. Pick a few words and figure out how to count their number of incidences?




## Challenge
# 5. How many words are in this text?




# 6. Lower case all of the text. How many words now?




## Extra Challenge
# 7. Can you figure out how to remove all punctuation and special characters from this text file? What is the unique work count now? (hint: use a set )





# 8. Write a function that given any project gutenberg book txt file returns a report that answers questions # 1 - 6.



if __name__ == '__main__':

    if not os.path.isfile(filename):

        urlretrieve(url, filename)
        # use requests if you have pip on your machine
        print('File: %s downloaded' % filename)
    else:
        print('File: %s present and ready to go!' % filename)

        pass
