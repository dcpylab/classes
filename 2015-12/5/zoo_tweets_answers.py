"""
Tweet Analysis

5 December 2015

National Zoo Tweet Analysis Homework


"""
import os
import csv # What does this do?

zoo_csv = 'zoo_tweets.csv' 

### Task 1a
### Open and read the csv file using the csv.reader function
### Hint: https://docs.python.org/2/library/csv.html
### Hint2: What is the delimiter in this file?


with open(zoo_csv, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    data = list(spamreader)


### Task 1b
### Create a list called tweet_list
### Using a for-loop, append all tweet_text in each row to tweet_list 
### Hint: This be the second (elem 2) of the list

tweet_list = []

with open(zoo_csv, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        tweet_list.append(row[2])

# print tweet_list


### Task 2
### Assign a variable called header for the first row.
### Assign a variable called rows to all rows after the first. ie row 0
### How many tweets or rows are in this csv file?
### When is the time span of the tweets (first versus last)?


header = data[0]
rows = data[1:]

# print len(rows)

# print rows[0][1]
# print rows[-1][1]


# Tue Nov 17 21:07:26 +0000 2015

from datetime import datetime, timedelta

first =  rows[0][1]
last  =  rows[-1][1]


first_tweet =  datetime.strptime(first,'%a %b %d %H:%M:%S +0000 %Y')

last_tweet = datetime.strptime(last,'%a %b %d %H:%M:%S +0000 %Y')

# print last_tweet - first_tweet



### Task 3
### Make an empty list called retweets
### Can you make a separate list of all retweets? 
### Can you make make a list of tweets_at using a list comprehension?
### Hint: use a for loop to identify if a tweet starts with '.@'

retweets = []

for tweet in tweet_list:
    if tweet[:2] == '.@':
        retweets.append(tweet)

tweets_at = [tweet for tweet in tweet_list if tweet[:2] == '.@']



### Task 4
### Make another empty list called hash_tags
### Using split() on each tweet, can you identify all the hashtags in each tweet add
### add them to the list called hash_tags?
### Hint: you'll need a a for loop and an if statement word[0] == '#'


hash_tags = [word.lower() for tweet in tweet_list for word in tweet.split() if word[0] =='#' ]

# print hash_tags

# print set(hash_tags)

### Task 5
### Make another list with all tweets that mention #pandastory

sorted_hash_tags =  sorted(set(hash_tags))


pandastory_tweets = hash_tags = [tweet for tweet in tweet_list for word in tweet.split() if word == '#pandastory']

# print pandastory_tweets

### can we do better?


# print sorted_hash_tags

panda_words = ['panda', 'bei', 'bao', 'mei']

hashtag_set = set()

for htag in sorted_hash_tags:
    [hashtag_set.add(htag) for word in panda_words if word in htag]
    



# print hashtag_set
# panda_hash = set(panda_hashtag_list)

# print panda_hash


panda_tweets = hash_tags = [tweet for tweet in tweet_list for word in tweet.split() if word in hashtag_set]

# print hashtag_set, '\n'
# print len(panda_tweets)

### with lower case

panda_tweets = hash_tags = [tweet for tweet in tweet_list for word in tweet.split() if word.lower() in hashtag_set]

print len(panda_tweets)



### Bonus
### Is there are day of the week that gets the most tweets with the #pandastory hashtag from the Zoo?



if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/ndanielsen/beginning-python/master/class/nov-18/hw/zoo_tweets.csv'

    filename = 'zoo_tweets.csv' 

    if not os.path.isfile(filename):

        urllib.urlretrieve(url, filename)
        # use requests if you have pip on your machine
        print 'File: %s downloaded' % filename
    else:
        pass
