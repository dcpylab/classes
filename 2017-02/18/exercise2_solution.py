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

#Uncomment to print how it looks our revised_paragraph list
#print(revised_paragraph)

#Split into words and save to list.
words_list = revised_paragraph.split()

#Count words using len()
words = len(words_list)

#Uncomment next print line to print here the amount of words.
#We will print all the information asked at the end too. 

#print('The amount of words in first_paragraph is: ', words)











 
