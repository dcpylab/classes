"""
Introduction to Python
DATE - 18 February 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

"""
Exercise 1:

Using the first paragraph:
1. How many words are in the first paragraph?
2. How many sentences are in the first paragraph?
3. How many times is the word 'Obama' is in the first paragraph?
4. If you remove all of the punctuation and lower case all text, how many words?


Note: For a guided and step by step solution explanation in jupyter notebooks go to:
https://github.com/ncclementi/dcpython_exercises/blob/master/02-18-17_application_real_data.ipynb

You will also find useful links and some extra tips to try in your script.
"""

first_paragraph = """
In the waning days of President Barack Obama’s administration, he and his wife, Michelle, hosted a farewell party, the full import of which no one could then grasp. It was late October, Friday the 21st, and the president had spent many of the previous weeks, as he would spend the two subsequent weeks, campaigning for the Democratic presidential nominee, Hillary Clinton. Things were looking up. Polls in the crucial states of Virginia and Pennsylvania showed Clinton with solid advantages. The formidable GOP strongholds of Georgia and Texas were said to be under threat. The moment seemed to buoy Obama. He had been light on his feet in these last few weeks, cracking jokes at the expense of Republican opponents and laughing off hecklers. At a rally in Orlando on October 28, he greeted a student who would be introducing him by dancing toward her and then noting that the song playing over the loudspeakers—the Gap Band’s “Outstanding”—was older than she was. “This is classic!” he said. Then he flashed the smile that had launched America’s first black presidency, and started dancing again. Three months still remained before Inauguration Day, but staffers had already begun to count down the days. They did this with a mix of pride and longing—like college seniors in early May. They had no sense of the world they were graduating into. None of us did.
"""

#Uncomment the following line to see the output of repr(header)
#print(repr(header))

# Part 1: How many words are in the first paragraph?

#Splitting and saving to a list.
paragraph_list = first_paragraph.split()

#Uncomment to print how it looks our split_paragraph list
#print(paragraph_list)


#We want to keep first_paragraph without changes, so we create a copy and work with that.
revised_paragraph = first_paragraph

#Remove "em dashes" (unicode: (Ctrl+Shift+u)+2014)
for element in revised_paragraph:
    if element == '—':
        revised_paragraph = revised_paragraph.replace(element, ' ')

#Uncomment to print how it looks our revised_paragraph.
#print(revised_paragraph)

#Split into words and save to list.
words_list = revised_paragraph.split()

#Count words using len()
words = len(words_list)

#Uncomment next print line to print here the amount of words.
#We will print all the information asked at the end too. 

#print('The amount of words in first_paragraph is: ', words)


# Part 2: How many sentences are in the first paragraph?

#We want to keep first_paragraph without changes, so we create a copy, in this
#case the copy will have replce  ? by . and also \n by '' . 

#First replace ? by .
sentence_paragraph = first_paragraph.replace('?', '.')
#Now replace \n by ''
sentence_paragraph = sentence_paragraph.replace('\n', '')

#Split the paragraph into sentences
sentence_list = sentence_paragraph.split('.')

#Uncomment to print how it looks our sentence_list
#print(paragraph_list)

#Let's remove the '' elements
for element in sentence_list:
    if element == '':
        sentence_list.remove(element)

#Now our sentences_list just contains the sentences, let's use len() to count
# the amount of sentences.
sentences = len(sentence_list)

#Uncomment next print line to print here the amount of sentences.
#We will print all the information asked at the end too. 

#print('The amount of sentences in first_paragraph is: ', sentences)

#Part 3 : How many times is the word 'Obama' is in the first paragraph?
#The following is a comment
'''
If you read the paragraph you might have notice that in some parts the Word
Obama appears as "Obama's". We want to count that case; therefore, we will look
for the string 'Obama' in wach word of the word_list. If the string is in the
word we will add 1 to the variable obama_count (initialized in 0). 
'''
#code
obama_count = 0
for word in words_list:
    if 'Obama' in word:
        obama_count +=1   

#Uncomment next print line to print here the amount of sentences.
#We will print all the information asked at the end too. 

#print('The word Obama in first_paragraph appears {} times.'.format(obama_count))

# Part 4: If you remove all of the punctuation and lower case all text, how many words?

#Lower case the whole paragraph and save into lower_paragrpah
lower_paragraph = first_paragraph.lower()

#Remove punctuation

#First we import the string constants available in python.  
import string

#Let's print the string punctuation (uncomment next line to print).
#print(string.punctuation)

#loop in the character of string.punctuation and we replace the characters that appear
#in our lower_paragraph for a space. 
for character in string.punctuation:
    lower_paragraph = lower_paragraph.replace(character, ' ')

#If you print the new lowe_paragraph you'll notice that we missed some characters
#We will remove them too, for detail explanation go to the jupyter notebook link
# located in the header at the top of this script.  

more_punct = '’‘“”—\n'
for character in more_punct:
    lower_paragraph = lower_paragraph.replace(character, ' ')

#With all the possible punctuation removed, now let's count words.
no_punctuation_list = lower_paragraph.split()
words_no_punctuation = len(no_punctuation_list)

#PRINTING ALL THE INFO REQUIRED TOGETHER:

print('The amount of words in first_paragraph is: ', words)
print('The amount of sentences in first_paragraph is: ', sentences)
print('The word Obama in first_paragraph appears {} times.'.format(obama_count))
print('The amount of words in the paragraph with no punctuation is: ', words_no_punctuation)  
