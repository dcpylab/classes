"""
Introduction to Parsing Real World Text with Python
DATE - 13 May 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

# print('hello world')
#
# # Comments in python use a '#'
#
# # Exercise: Comments
# print('uncomment me')
# print('thanks for coming on this nice rainy day')
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

book2 = "The Variable Man by Dick, Philip K., 1928-1982"

book3 = "The Skull by Dick, Philip K., 1928-1982"










################################################################################

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







################################################################################


#### Application with Real Data
# Looking at a recent White House Press Briefing:
# https://www.whitehouse.gov/the-press-office/2017/05/12/press-briefing-press-secretary-sean-spicer-5122017-47

header = """
The White House
Office of the Press Secretary
For Immediate Release May 12, 2017
Press Briefing by Press Secretary Sean Spicer, 5/12/2017, #47
    """

# EXERCISES: Part I
#1 - Extract the Office
#2 - Extract the Date
#3 - Extract the Briefing Number
#4 - Extract the Extract Briefing by Who

# Hint: Google something called repr
# Hint: What is \n?










################################################################################


introduction_words = """
MR. SPICER:  Wow, we got a full house today.  Good afternoon.  It's good to be back with you.  Apparently I was a little missed.

We're one week out from the President's first foreign trip, so I wanted to make sure, as we prepare for that trip, that I bring out National Security Advisor, General McMaster, to give you a preview of what the team has been doing to prepare for the President's trip.  Our goal is to kind of start that process now, and then next week bring the General back and give you a more detailed update as to what the President is going to be doing in each of the areas, and some of the highlights from the trip.  We'll, obviously, additionally, have background briefings for you as well to give the team that's going to be traveling, the press corps, some logistical updates.

So without further ado, General McMaster.
"""

# EXERCISES: Part II
#1 - How many words are in the introductionary words?
#2 - How many sentences are in the introductionary words?
#3 - How many times is the word 'President' is in the introductionary words?
#4 - If you remove all of the punctuation and lower case all text, how many words?










################################################################################
question_response = """
Q    Is the President considering cancelling the daily press briefings?

MR. SPICER:  I think he’s a little dismayed, as well as a lot of people, that we come out here and try to do everything we can to provide you and the American people with what he’s doing on their behalf, what he’s doing to keep the nation safe, what he’s doing to grow jobs, and yet, we see time and time again an attempt to parse every little word and make it more of a game of “gotcha” as opposed to really figure out what the policies are, why something is being pursued or what the update is on this.

And I think that’s where there’s a lot of dismay, and I don’t think it’s something that just alone the President feels.

Q    Can I ask you one final logistical question?

MR. SPICER:  Sure, one final.  It’s Friday.

"""

# EXERCISES: Part III
#1 - How can you identify a speaker and a question?
#2 - How many questions and responses are in question response?
#3 - Can you pair each question with a response?










################################################################################

# EXERCISES: Part IV Advanced
#1 - In the text file, briefing.txt, open it with python.
#2 - How many words are in entire text?
#3 - How many sentences?
#4 - How many questions are asked?
#5 - How many identified speakers? Who speaks the most words?
#6 - How many "questions" actually contain questions?
#7 - Can you pair true questions with the chain of responses?
#8 - In each question-response chain, what are the most common words?

# Hint: Use google open file with python
