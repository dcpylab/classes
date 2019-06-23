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

parser = argparse.ArgumentParser()

parser.add_argument("min",type=int,help="What is the min number you want?")
parser.add_argument("max",type=int,help="What is the max number you want?")

args = parser.parse_args()

fizz_buzz(args.min, args.max)
