""" Get alphabet from -> https://en.wikipedia.org/wiki/NATO_phonetic_alphabet """

source = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu"

""" First, clean up our source material """

words = source.split(",")

# Using list comprehension
clean_words = [word.lower().strip() for word in words]

# Using for loop
clean_words = []
for word in words:
	clean_words.append(word.lower().strip())
	
# Using map and lambda combo
clean_words = list(map(lambda w: w.lower().strip(), words))

""" Then get the letters of the alphabet in a separate list """

# Using list comprehension
letters = [word[0] for word in clean_words]

# Alternatively, using `string` library
import string
letters = list(string.ascii_lowercase)

""" Zip the two list together to create a dictionary """
nato = dict(zip(letters, clean_words))

def get_phonetic_simple(word):
	""" 
	Translates string into phonetic alphabet.
	"""

	translation = [nato[letter].title() for letter in word]
	
	return ' '.join(translation)

def get_phonetic_complete(word):
	""" 
	Translates string into phonetic alphabet.
	Handles input validation.
	Throww error if `word` contains digits.
	"""
	
	if any(letter.isdigit() for letter in word):
		raise TypeError("Word must not contain any digits!")
		
	if ' ' in word:
		clean_word = ''.join(word.split())

	clean_word = clean_word.lower().strip()

	translation = [nato[letter].title() for letter in clean_word]
	
	return ' '.join(translation)
	
	
word = input("Select a word that you would like to translate: ")
translation = get_phonetic_simple(word)
print("The phonetic spelling of '%s' is: '%s'." % (word, translation))

word_with_spaces = input("Now, select a word with spaces: ")
translation_with_spaces = get_phonetic_complete(word_with_spaces)
print("The phonetic spelling of '%s' is: '%s'." % (
	word_with_spaces, 
	translation_with_spaces
))

word_with_digits = input("Now, select phrase with digits: ")
# This part will through a TypeError because we cannot transate digits
translation_with_digits = get_phonetic_complete(word_with_digits)
