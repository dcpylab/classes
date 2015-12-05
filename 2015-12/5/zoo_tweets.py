"""
Tweet Analysis

5 December 2015

National Zoo Tweet Analysis Homework

by NAthan for the pylab

nathan.danielsen@gmail.com

"""
import os
import csv # What does this do?

zoo_csv = 'zoo_tweets.csv' 

### Task 1a
### Open and read the csv file using the csv.reader function
### Hint: https://docs.python.org/2/library/csv.html
### Hint2: What is the delimiter in this file?

tweet_text = []

with open(zoo_csv, 'rb') as csvfile:
    tweetreader = csv.reader(csvfile, delimiter='|')     
    for row in tweetreader:
        tweet_text.append(row)

# print tweet_text

### Task 1b
### Create a list called tweet_list
### Using a for-loop, append all tweet_text in each row to tweet_list 
### Hint: This be the second (elem 2) of the list



### Task 2
### Assign a variable called header for the first row.
### Assign a variable called rows to all rows after the first. ie row 0
### How many tweets or rows are in this csv file?
### When is the time span of the tweets (first versus last)?

header = tweet_text[0]

rows = tweet_text[1:]

# print rows[0]

### Task 3
### Make an empty list called retweets
### Can you make a separate list of all retweets? 
### Can you make make a list of tweets_at using a list comprehension?
### Hint: use a for loop to identify if a tweet starts with '.@'

retweets = []
# 'RT'

for row in rows:
    num, created_at, text = row
    if text[:2] == 'RT':
        retweets.append(row)

sample = 'RT @KateGraves: Excited about the new Appalachian salamander exhibit @NationalZoo @smithsonian http://t.co/k71eQrLzV1'

# print sample[:2]

# print len(retweets)

tweets_at = []

for row in rows:
    num, created_at, text = row
    if text[:2] == '.@':
        tweets_at.append(row)

# print len(tweets_at)

### Task 4
### Make another empty list called hash_tags
### Using split() on each tweet, can you identify all the hashtags in each tweet add
### add them to the list called hash_tags?
### Hint: you'll need a a for loop and an if statement word[0] == '#'

hash_tags = []

for row in rows:
    num, created_at, text = row

    for word in  text.split():
        if word[0] == '#':
            hash_tags.append(word)

# print hash_tags

set_hashtag = set(hash_tags)

# print sorted(set_hashtag)

### Task 5
### Create an empty list called panda_tweets
### Make another list with all tweets that mention #pandastory
### 
panda_tweets = []

for row in rows:
    num, created_at, text = row
    for word in  text.split():
        text = text.lower()

        if word == '#pandastory' or word == '#beibei' or word == '#baobao':
            panda_tweets.append(text)

# print panda_tweets


panda_words = ['panda', 'bei', 'bao', 'mei']

hashtag_set = set()

# for htag in sorted(set_hashtag):
#     [hashtag_set.add(htag) for word in panda_words if word in htag]
    
if 'panda' in '#pandastory':
    print 'its in there'




### Bonus
### Is there are day of the week that gets the most tweets with the #pandastory hashtag from the Zoo?



if __name__ == '__main__':
    import urllib

    url = 'https://raw.githubusercontent.com/ndanielsen/beginning-python/master/class/nov-18/hw/zoo_tweets.csv'

    filename = 'zoo_tweets.csv' 

    if not os.path.isfile(filename):

        urllib.urlretrieve(url, filename)
        # use requests if you have pip on your machine
        print 'File: %s downloaded' % filename
    else:
        print 'File: %s present and ready to go!' % filename

        pass
