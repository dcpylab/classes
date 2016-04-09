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

Feel free to reach out with questions
nathan.danielsen@gmail.com

"""
# Constants

url = 'http://www.gutenberg.org/cache/epub/3176/pg3176.txt'
filename = 'innocents-abroad.txt'


# Setup taskes

# Open the file
# Print out file contents to terminal
# Inspect file structure and format

with open(filename, 'r') as f:
    book_data = f.read()
    # print(book_data)


# Questions:



# 2. How many characters (a,b,c,1,3,4) are in this txt file?

# print(len(book_data))




# 3. How many '\n' are in this text file? When is the first '\n'?


# print(unicode(book_data))
# print(help(type("hello")))
# print(book_data.count('\n'))
# book_data_short = book_data[:75]
# print(book_data_short.count('g'))
# print(book_data.count('the'))
# str.count(sub, start= 0,end=len(string))


# book_data_short = book_data[:75]


# print(repr(book_data_short))

by_author = book_data.find(', by')
end_of_first_line = book_data.find('\n')
# print( book_data[by_author:end_of_first_line])


# Project Gutenberg's The Innocents Abroad, by Mark Twain (Samuel Clemens)

def get_title_author(book_data):
    # first the end of the first line
    end_of_first_line = book_data.find('\n')

    # find the Title
    gutenberg_intro = "Gutenberg's "
    title_start = book_data.find(gutenberg_intro) + len(gutenberg_intro)

    # find the author

    by_str = ', by '
    by_author = book_data.find(by_str)
    position_author = by_author + len(by_str)

    title  = book_data[title_start: by_author ]
    author = book_data[position_author:end_of_first_line]

    return {'title': title, 'author': author }

# print(get_title_author(book_data))

dummy_book_data = "Project Gutenberg's God Emperor of Dume, by Frank Herbert\n\n"

# print(get_title_author(dummy_book_data))


# 1. Using string slicing, what is the title of this book?

# book_data.index


# Input:
    # The entire open book file -- or a shorter slice of the book


# Output:
    # Title of the book



# 4. Pick a few words and figure out how to count their number of incidences?

# print(book_data.count('the'))
#
book_data_lower = book_data.lower()
#
# print(book_data_lower.count('the'))
book_data_lower = book_data_lower.replace('\n', '')

book_words_list = book_data_lower.split(' ')




## Challenge
# 5. How many words are in this text?

print(len(book_words_list))


# 6. Lower case all of the text. How many words now?




## Extra Challenge
# 7. Can you figure out how to remove all punctuation and special characters from this text file?
# 7b. What is the unique word count now? (hint: use a set )

unique_items = set(book_words_list) ## for unique words

myword_dict = {} # for counting words





# 8. Write a function that given any project gutenberg book txt file returns a report that answers questions # 1 - 6.



if __name__ == '__main__':

    if not os.path.isfile(filename):

        urlretrieve(url, filename)
        # use requests if you have pip on your machine
        print('File: %s downloaded' % filename)
    else:
        # print('File: %s present and ready to go!' % filename)

        pass
