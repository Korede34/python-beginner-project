import random
import time

def displayIntro():
	print('You are in a land full of dragons. In front of you,') 
	print('you see two caves. In one cave, the dragon is friendly') 
	print('and will share his treasure with you. The other dragon') 
	print('is greedy and hungry, and will eat you on sight.') 
	print()
displayIntro()

def chooseCave():
	print('Which cave will you go into? (1 or 2)')
	flag = True
	while flag:
		cave = input()
		if cave in ['1', '2']:
			flag = False
			return cave
		else:
			print("Invalid input, Try again")
option = chooseCave()
	
def checkCave(player_option):
	 print('You approach the cave...')
	 time.sleep(1)
	 print('It is dark and spooky...')
	 time.sleep(1)
	 print('A large dragon jumps out in front of you! He opens his jaws')
	 print()
	 time.sleep(1)
	 
	 friendly_cave = random.randint(1, 2)
	 if player_option == str(friendly_cave):
	 	print("Give you his treasure!")
	 else:
	 	print("Gobbles you down in one bite!")
checkCave(option)

while True:
	print("Do you want to play again (yes or no)")
	playAgain = input()
	if playAgain in ['y', 'yes']:
		displayIntro()
		chooseCave()
		checkCave(option)
	else:
		break

	