# rock papers scissors lizard spock

#rock > scissors
#rock > lizard

#scissors > paper
#scissors > lizard

#paper > rock
#paper > spock

#lizard > paper
#lizard > spock

#spock > scissors
#spock > rock

winners = {
    "rock": ["scissors", "lizard"],
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "lizard": ["paper", "spock"],
    "spock": ["scissors", "rock"]
}

def rps(choice1, choice2):
  if choice1 == choice2:
    print("Tie!")
    return

  if choice1 not in winners:
    print("Choice 1 not valid, dude!")
    return

  if choice2 not in winners:
    print("Choice 2 not valid, dude!")
    return

  player_1_wins_against = winners[choice1]
  player_2_wins_against = winners[choice2]

  if choice2 in player_1_wins_against:
    print("Player 1 wins")
  elif choice1 in player_2_wins_against:
    print("Player 2 wins")
  else:
    print("I don't even know what just happened")


# TEST CASES

rps("rock", "rock")
rps("lizard", "spock")
rps("paper", "scissors")
rps("rock", "paper")
rps("rock", "fish")
