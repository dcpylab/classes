import string

def get_translator():
	source = """
	Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf,
	Hotel, India, Juliett, Kilo, Lima, Mike, November,
	Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform,
	Victor, Whiskey, X-ray, Yankee, Zulu
	"""
	nato_words = []
	for word in source.split(","):
		nato_words.append(word.lower().strip())
	alpha_words = list(string.ascii_lowercase)
	translator = dict(zip(sorted(alpha_words), sorted(nato_words)))
	return translator

def translate(word):
	translator = get_translator()
	translated_word = []
	for letter in word:
		nato_word = translator[letter.lower()]
		translated_word.append(nato_word)
	return ', '.join(translated_word)

word = input("What word would you like to translate? ")
output = translate(word)
print(output)
