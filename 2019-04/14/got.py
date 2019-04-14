from __future__ import print_function
import json

try:
	# Python 3
    from urllib.request import urlopen, Request
except ImportError:
	# Python 2
    from urllib2 import urlopen, Request

# https://www.anapioficeandfire.com/Documentation

headers = {'User-Agent': 'Mozilla/5.0'}

endpoints = {
	'characters': 'https://www.anapioficeandfire.com/api/characters/?page=%d&pageSize=%d',
	'houses': 'https://www.anapioficeandfire.com/api/houses/',
	'books': 'https://www.anapioficeandfire.com/api/books/'
}

pages = 20
num_characters = 50
all_characters = []

for page in range(1, pages + 1):

	url = endpoints['characters'] % (page, num_characters)

	request = Request(url, headers = headers)
	response = urlopen(request)
	contents = response.read()

	characters = json.loads(contents)
	
	print("Collected characters from page %d" % page)
	
	all_characters.extend(characters)

print("The total number of characters is %d" % len(all_characters))

# Filtering using a list comprehension
dead_char = [ch['name'] for ch in all_characters if ch['died'] != '']

# Filtering using a higher order function
def is_dead(character):
	if character['died'] != "":
		return True
	return False

dead_char = list(filter(is_dead, all_characters))

print("The number of dead characters is %d" % len(dead_char))
print("The number of alive characters is %d" % (len(all_characters) - len(dead_char)))

# print("The URL for characters is %s" % endpoints['characters'])
# print("The URL for books is %s" % endpoints['books'])
# print("The URL for houses is %s" % endpoints['houses'])
 