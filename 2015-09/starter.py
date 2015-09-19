
# PYlab 2015-0919 
# session led by Nathan Danielsen

# Starter Code
 
import urllib

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/daily-show-guests/daily_show_guests.csv'

filename = 'daily_show_guests.csv'

if not os.path.isfile(filename):

	urllib.urlretrieve(url, 'daily_show_guests.csv')
	# use requests if you have pip on your machine

else:
	pass

