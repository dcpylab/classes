import string
import random

def generate_pwd(length, use_upper, use_digits, use_punct):
	pool = string.ascii_lowercase
	
	if use_upper:
		pool += string.ascii_uppercase
	if use_digits:
		pool += string.digits
	if use_punct:
		pool += string.punctuation
	
	pwd = ""
	
	for i in range(length):
		character = random.choice(pool)
		pwd += character
	
	return pwd

length = input("How long do you want your password to be? ")

pwd_digit_punct = generate_pwd(int(length), use_digits=True, use_punct=True, use_upper=False)
pwd_digit_upper = generate_pwd(int(length), use_digits=True, use_punct=True, use_upper=True)
pwd_no_punct_or_digit = generate_pwd(int(length), use_digits=False, use_punct=False, use_upper=True)

print("Your password w/ digits & punct is %s!" % pwd_digit_punct)
print("Your password w/ digits & upper is %s!" % pwd_digit_upper)
print("Your password w/ digits & upper is %s!" % pwd_no_punct_or_digit)

