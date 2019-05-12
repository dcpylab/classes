import string
import random

def generate_password(length=8,use_upper=False,use_digits=False,use_punctuation=False):

	password = ""
	
	# At a bare minimum, the password should
	# have at least lowercase letteres
	pool = string.ascii_lowercase
	
	if use_upper:
		pool += string.ascii_uppercase
	
	if use_digits:
		pool += string.digits
	
	if use_punctuation:
		pool += string.punctuation
	
	for i in range(length):
		character = random.choice(pool)
		password += character 
	
	return password
	
password = generate_password(30,True,True,True)

print("My generated password is = %s" % password)
