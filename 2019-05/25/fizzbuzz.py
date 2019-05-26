

def fizz_buzz(starting_range, ending_range):

	for i in range(starting_range, ending_range + 1):
	
		if i % 5 == 0 and i % 3 == 0: 		# multiple of 3 and 5
			print("FizzBuzz")
		
		elif i % 3 == 0: 					# multiple of 3
			print("Fizz")
			
		elif i % 5 == 0: 					# multiple of 5
			print("Buzz")

		else:
			print(i)
			
starting_range = 1
ending_range = 100

print("Printing `FizzBuzz` for range %d to %d" % (
	starting_range,
	ending_range
))
			
fizz_buzz(starting_range, ending_range)
