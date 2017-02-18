"""
Introduction to Python
DATE - 18 February 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

# print('hello world')
#
# # Comments in python use a '#'
#
# # Exercise: Comments
# print('uncomment me')
# print('thanks for coming on this nice day')
# BASIC DATA TYPES

# Numbers
# https://docs.python.org/2/tutorial/introduction.html#numbers

5  # Integer
5.0  # Float (decimal)
x = 5  # creates an object

y = 2345

type(x)  # check the type: int (not declared explicitly)
type(5)  # assigning it to a variable is not required
type(5.0)  # float
type(True)  # bool

### Exercise: Checking Data Type
text = 'What type of data type am I?'



# math operations

1 + 2  # Addition
7 - 5  # Division
5 * 7  # Multiplication
10 / 3  # Division
10 / 3.0  # Floor division
16 % 5  # Modulo (remainder)
2**10  # Exponent

# variable assignment
a = 1
b = 2
c = 6

### Exercise: A little math
#1 Assign a variable 'd' that equals 'a' plus 'b' minus 'c'

d = a + b -c

#2 What value is d?

# print(d)

#3 Assign a variable 'e' that is 'd' divided by 6.0

e = d / 6.0

#4 what is the value of e?

# print(e)

# STRINGS
# https://docs.python.org/3/tutorial/introduction.html#strings

s = str(42)

s  # convert another data type into a string (casting)
s = 'I like you'

# examine a string
s[0]  # returns 'I'
len(s)  # returns 10

# string slicing like lists
s[0:7]  # returns 'I like'
s[6:]  # returns 'you'
s[-1]  # returns 'u'

# EXERCISE: Book Titles (Part 1)
# 1) Extract the book title from the string
# 2) Save each book title to a variable (ie book1_title)
# 3) How many characters/elements are in each title?

book1 = "Beyond the Door by Dick, Philip K., 1928-1982"

book1_title = book1[:16]
# print(book1_title)

book2 = "The Variable Man by Dick, Philip K., 1928-1982"

book2_title = book2[:17]
# print(book2_title)
# print(len(book2_title))

book3 = "The Skull by Dick, Philip K., 1928-1982"

book3_title = book3[:9]
# print(book2[:-30] )

################

# split a string into a list of substrings separated by a delimiter

s = 'I like you'
s.split(' ')  # returns ['I','like','you']
s.split()  # same thing

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4  # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# EXERCISE: Book Titles (Part 2)
# 1. How words are in the title of book1?
# BONUS: Comparison:  Does book1_title have more words then book3_title3?
# HINT: https://docs.python.org/3/library/stdtypes.html#comparisons
book1 = "Beyond the Door by Dick, Philip K., 1928-1982"

book1_title = book1[:16]
list_of_title = book1_title.split()
# print(len(list_of_title))

#### Application with Real Data
# Looking at a recent Atlantic Magazine piece:
# https://www.theatlantic.com/magazine/archive/2017/01/my-president-was-black/508793/

header = """
    My President Was Black
    A history of the first African American White House—and of what came next

    By Ta-Nehisi Coates
    Photograph by Ian Allen
    """

# EXERCISES: Part I
#1 - Extract the title
#2 - Extract the introduction
#3 - Extract the author
#4 - Extract the photographer

# Hint: Google something called repr

# print(repr(header))

header_list = header.split('\n')

title = header_list[1].strip()

first_paragraph = """
In the waning days of President Barack Obama’s administration, he and his wife, Michelle, hosted a farewell party, the full import of which no one could then grasp. It was late October, Friday the 21st, and the president had spent many of the previous weeks, as he would spend the two subsequent weeks, campaigning for the Democratic presidential nominee, Hillary Clinton. Things were looking up. Polls in the crucial states of Virginia and Pennsylvania showed Clinton with solid advantages. The formidable GOP strongholds of Georgia and Texas were said to be under threat. The moment seemed to buoy Obama. He had been light on his feet in these last few weeks, cracking jokes at the expense of Republican opponents and laughing off hecklers. At a rally in Orlando on October 28, he greeted a student who would be introducing him by dancing toward her and then noting that the song playing over the loudspeakers—the Gap Band’s “Outstanding”—was older than she was. “This is classic!” he said. Then he flashed the smile that had launched America’s first black presidency, and started dancing again. Three months still remained before Inauguration Day, but staffers had already begun to count down the days. They did this with a mix of pride and longing—like college seniors in early May. They had no sense of the world they were graduating into. None of us did.
"""

# EXERCISES: Part II
#1 - How many words are in the first paragraph?
#2 - How many sentences are in the first paragraph?
#3 - How many times is the word 'Obama' is in the first paragraph?
#4 - If you remove all of the punctuation and lower case all text, how many words?

revised_paragraph = first_paragraph.replace('?', '.').replace('\n', '')
split_paragraph = revised_paragraph.split('.')

count = 0
for sentence in split_paragraph:
    if sentence != '':
        count += 1

print(count)

# EXERCISES: Part III Advanced
#1 - In the text file, article_part_one.txt, open it with python.
#2 - How many words are in part one?
#3 - How many sentences are in part one?
#4 - Which words follow 'black' and 'white' in the text? Which ones are used the most for each?

# Hint: Use google open file with python
