import string
import random
	
def get_password(
		length,
		use_lower, 
		use_upper, 
		use_digit, 
		use_punctuation
	):
	
	# A minimum length of 5
	actual_length = max(5, length)
	
	pool = string.ascii_lowercase
	
	if use_upper:
		pool += string.ascii_uppercase
	if use_digit:
		pool += string.digits
	if use_punctuation:
		pool += string.punctuation
	
	pwd = ""
	
	for _ in range(actual_length + 1):
		pwd += random.choice(pool)
		
	return pwd

password = get_password(
	length=3, 
	use_lower=True,
	use_upper=True,
	use_digit=True,
	use_punctuation=False
)

print("My password is " + password)









