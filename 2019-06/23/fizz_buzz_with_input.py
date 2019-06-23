import argparse

def fizz_buzz(min_num, max_num):
	for i in range(min_num, max_num + 1):
		if (i % 3 == 0) and (i % 5 == 0):
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")	
		else:
			print(i)

min_num = eval(input("What is the min num you want? "))
max_num = eval(input("What is the max num you want? "))

fizz_buzz(min_num, max_num)
