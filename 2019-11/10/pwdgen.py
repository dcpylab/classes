import string
import random
import argparse

def generate_password(length, use_upper, use_digits, use_punct):
	pool = string.ascii_lowercase
	pwd = []
	if use_upper:
		pool += string.ascii_uppercase
	if use_digits:
		pool += string.digits
	if use_punct:
		pool += string.punctuation
	
	for i in range(1, length + 1):
		value = random.choice(pool)
		pwd.append(value)
	return ''.join(pwd)
	
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("length", type=int,
						help="How long do you want your password to be?")					
	parser.add_argument("-u", "--upper", action='store_true',
						help="True if you want to use upper case.")
	parser.add_argument("-d", "--digit", action='store_true',
						help="True if you want to use digits.")		
	parser.add_argument("-p", "--punct", action='store_true',
						help="True if you want to use punctuation.")
						
	args = parser.parse_args()
	pwd = generate_password(
		args.length,
		args.upper,
		args.digit,
		args.punct
	)
	print("Your password: '%s'!" % pwd)

if __name__=='__main__':
	main()
