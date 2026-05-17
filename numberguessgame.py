#!/usr/bin/python3

# Number guessing game

# Initialization and import:
import math
import random
import sys
print_number = False
if sys.argv[1:]==["--show-number"]:
	print_number= True
number = int(random.randint(1, 100))
if print_number:
	print(number)

# Game logic:


guess_number = 1
while True:
	guess = int(input(f"What is your guess (number {guess_number})? "))
	guess_number = guess_number + 1

	if guess  == number:
		print(f"Congratulations! Your guess ({number}) is correct!")
		sys.exit(0)
	elif (guess > number + 20 or guess < number - 20) and guess < 100:
		print("Sorry, thats not quite right! You're cold.")
	elif (guess > number + 10 or guess < number - 10) and guess < 100:
       		print("Sorry, thats not quite right! You're warmer.")
	elif (guess > number + 5 or guess < number - 5) and guess < 100:
        	print("Sorry, thats not quite right! You're hot.")
	elif (guess > number or guess < number) and guess < 100:
        	print("Sorry, thats not quite right, but you're so hot it might melt your face off!.")
	elif guess > 100:
		print("?! That is not a valid guess!")

# Tada! I hope you've enjoyed this game.
