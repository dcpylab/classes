
def fizz_buzz(max_num):

	output = []

	for num in range(1, max_num + 1):
	
		if (num % 3) == 0 and (num % 5) == 0:
			output.append("FizzBuzz")
		elif num % 3 == 0:
			output.append("Fizz")
		elif num % 5 == 0:
			output.append("Buzz")
		else:
			output.append(num)

	return output
		
output = fizz_buzz(100)

for i in output:
	print(i)
