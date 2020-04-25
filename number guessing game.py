from random import randint

"""Python Guessing Game"""

#Welcome the player to the game
name = input("Enter your name: ")
name = name.title()
print(f'***{name} you are welcome to number guessing game.***')
print()
print(f'Well, {name}. You only have 5 chances to guess the number \nright before the game is over.')
print()

#Get upper bound value from the pkayer
flag = True
while flag:
	upper_bound = input("Enter an upper bound: ")
	if upper_bound.isdigit():
		upper_bound = int(upper_bound)	
		flag = False
	else:
		print("Invalid input")
		
#Generate random secret number with player upper bound 
secret_number = randint(1, upper_bound)
#counter
count = 0

#Make the player guess the number
playerGuess = ""
while playerGuess != secret_number and count != 5:
	playerGuess = input(f"Guess a number between 1 and {upper_bound}: ")
	count += 1
	playerGuess = int(playerGuess)
	
	if playerGuess < secret_number:
		print(f"Too low, try again\nYou have {5 - count} attemps  left")
		
	elif playerGuess > secret_number:
		print(f"Too high, try again\nYou have {5 - count} attempts left")
		
	else:
		break
		
if playerGuess == secret_number:
	print(f"Congrats, it took you {count} attempt to guess the number right")
else:
	print(f"The secret number is {secret_number}")
					 		