
import pangram
# pangram = "The quick brown fox jumps the lazy dog."
pungram = input("Please type your pangram: ")

print("Is this a pangram?", pungram)
print("Computer says:", pangram.is_pangram(pungram))
