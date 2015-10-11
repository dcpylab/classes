"""
The key idea of this programme is to equate the strings 'rock', 'paper',
'scissors', 'lizard', 'Spock' to numbers as followed

0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors

The rules of the game is as followed

Scissors cut Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitate Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporises Rock
Rock crushes Scissors
"""

import random	# used for opponent response

#helper function

def name_to_number(name):
	"""
	convert name to number using dictionary type
	the function returns an integer
	name must be a string variable
	"""
	
	convert = {"rock":0, "Spock":1, "paper":2, "lizard":3, "scissors":4}

	# possible choices
	#selection = ["rock", "Spock", "paper", "lizard", "scissors"]
	#selection = convert.keys()
	#value = convert.values()

	#if name in selection:	# check if name is a valid selection
	if name in convert:
		converted = convert[name]
		#return converted
		return convert[name]
	else:
		print("Invalid choice")

def number_to_name(number):
	# convert number to name using dictionary type
	# the function returns a string

	convert = {0:"rock", 1:"Spock", 2:"paper", 3:"lizard", 4:"scissors"}

	if (number >= 0) and (number < 5):	# check number is in range
	#if number in convert:
		converted = convert[number]
		return converted
	else:
		print("Invalid number")

def give_reason(first, second):
	"""
	The function gives the reason of the game outcome using dictionary
	The two parameters are integers, first is the winner choice,
	second is the loser choice.  The order cannot be altered
	The function returns a string
	"""
	# R P S L S game rules
	game_rule = {(4, 2):"Scissors cut paper",
			(2, 0):"Paper covers rock",
			(0, 3):"Rock crushes lizard",
			(3, 1):"Lizard poisons Spock",
			(1, 4):"Spock smashes scissors",
			(4, 3):"Scissors decapitate lizard",
			(3, 2):"Lizard eats paper",
			(2, 1):"Paper disproves Spock",
			(1, 0):"Spock vaporises rock",
			(0, 4):"Rock crushes scissors"}

	# check whether the two parameter values are in range
	# boolean values
	firstInRange = (first >= 0) and (first < 5)
	secondInRange = (second >= 0) and (second < 5)

	if firstInRange and secondInRange:
		return game_rule[(first, second)]
	else:
		print("Paramter values out of range")

# game function

def rpsls(player_choice):
	"""
	This is the main function of the programme
	The function generates choice and compares against the choice of
	the player, then determines the outcome of the game and prints it
	to the console
	"""
	print('\n')
	print("Player chooses " + player_choice)

	player = name_to_number(player_choice)
	computer = random.randrange(0, 5)	# random computer choice

	computer_choice = number_to_name(computer)

	print("computer chooses " + computer_choice)

	# calculate the difference
	diff = player - computer

	if diff != 0:
		result = diff % 5
	#if not(diff == 0):	# different choices
		if (result) < 3:	# computer chooses anticlockwise
			print(give_reason(player, computer))
			print("Player wins!")
		else:		# computer chooses clockwise
			print(give_reason(computer, player))
			print("Computer wins!")
		return result
	else:		# same choices
		print("Player and computer tie")
		return diff
	
"""
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
"""
def main():
	player_score = 0
	computer_score = 0
	
	for i in range(6):
		game_result = rpsls('rock')
		if game_result == 1 or game_result == 2:
			player_score += 1
		elif game_result == 3 or game_result == 4:
			computer_score += 1
		else:
			pass

	print("player score: %d" % player_score)
	print("computer score: %d" % computer_score)
main()
