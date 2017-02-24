"""
Introduction to Python
DATE - 18 February 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

"""
## Eercise 3: Advanced

1. Open the article_part_one.txt with python.
2. How many words are in part one?
3. How many sentences are in part one?
4. Which words follow 'black' and 'white' in the text? Which ones are used the most for each?

*Hint*: Google open file with python

Note: For a guided and step by step solution explanation in jupyter notebooks go to:
https://github.com/ncclementi/dcpython_exercises/blob/master/02-18-17_application_real_data.ipynb

You will also find useful links and some extra tips to try in your script.

In this case because it was the advanced exercise, I introduce new things that 
we didin't see on the class. hope you have fun!
"""

#Open the file:

with open('article_part_one.txt', 'r') as file:
    article = file.read()

#Uncomment following line to print article.
#print(article)


## How many words are in part one?

#First remove all punctuation to make the count easier. 

import string

punctuation = string.punctuation
#Some extra symbols that are in the text that don't appear in string.punctuatuon
#You can create them using unicode (Check notebook for this) 
extra_punct = '’‘“”—\n'

all_punct = punctuation + extra_punct

#Now let's remove this from the text.

#We will modify article_no_punct but we want to keep intact article. So
article_no_punct = article

for char in all_punct:
    if char in article_no_punct:
        article_no_punct = article_no_punct.replace(char, ' ') 

#Split and count words
words_list = article_no_punct.split()
words_total = len(words_list)

#Uncomment this to print at this point
#print('The total amount of words is: {}'.format(words_total))

# To have extra tips on count how many of each words do you have, check the notebook


## How many sentences are in part one?

#We will modify article_sentences but we want to keep intact article. So
article_sentences = article

#If you take a look at the article you might have noticed that the header
#sentences have no '.' but there are break lines there, so we will replace 
#the '\n' for periods and then but split. 

article_sentences = article_sentences.replace('\n','.')

#Split when periods to count sentences
sentences_article_list = article_sentences.split('.')


#Let's ommit the '' and the elements that are "sentences" that are actually 2
# letters because they were part of an abbreviation. For example '— F' or '"'. 
#These elements have the particularity that their length is always smaller
# than 3, so let's filter that.

list_clean = list(filter(lambda item: len(item)>3 , sentences_article_list))

sentence_total = len(list_clean)

#Uncomment this to print at this point
#print('The total amount of sentences is: {}'.format(sentence_total))


## Which words follow 'black' and 'white' in the text? 
## Which ones are used the most for each?

# Here we will use new stuffs, go to the notebook for links and explanations.

#Set all lower case so we just look for white/black.

words_lower = []
for word in words_list:
    words_lower.append(word.lower())

#We want to know were in the list appears the word white and where the word
# black. We look for those indices doing the following.

indx_white  = [i for i, x in enumerate(words_lower) if x == "white"]
indx_black  = [i for i, x in enumerate(words_lower) if x == "black"]

#Looking for the words that follow white
lst_white =[]
for i in indx_white:
    lst_white.append(words_lower[i+1])

#Looking for the words that follow white
lst_black =[]
for i in indx_black:
    lst_black.append(words_lower[i+1])

#Let's count for each list the repetitions of each word using dictionaries 
#and the get method. 
follows_white = {}
for word in lst_white:
        follows_white[word] = follows_white.get(word,0) + 1

follows_black = {}
for word in lst_black:
        follows_black[word] = follows_black.get(word,0) + 1

#Uncomment the following 2 lines to see how the follows_white and follows_black
#dictionaries look like.

#print(follows_white)
#print(follows_black)

#Let's get the word in each dictionary that has the biggest value. 

most_follow_white = max(follows_white, key=follows_white.get)
most_follow_black = max(follows_black, key=follows_black.get)

#Uncomment next two lines to print las answer
#print("The most used word that follows 'white' is: ",most_follow_white)
#print("The most used word that follows 'black' is: ",most_follow_black)


## PRINTING ALL THE ANSWERS:

print('The total amount of words is: {}'.format(words_total))
print('The total amount of sentences is: {}'.format(sentence_total))
print("The most used word that follows 'white' is: ",most_follow_white)
print("The most used word that follows 'black' is: ",most_follow_black)

