"""Python Hangman game"""
import random

hangman_board =  ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
 
word_list = ['this', 'new', 'capacity', 'programming',
'ecology', 'and', 'one', 'the', 'things', 'that', 
'know', 'comes', 'mind', 'very', 'quickly', 'when', 
'people', 'hear', 'ecology', 'this', 'move', 'sort', 
'equate', 'ecology', 'and', 'environmentalism', 'Could', 
'you', 'say', 'something', 'about', 'what', 'the', 'similarity', 
'and', 'difference', 'Where', 'does', 'ecology', 'and', 
'environmentalism', 'begin', 'Well', 'tell', 'students', 
'teach', 'general', 'ecology', 'undergraduates', 'And']

def get_random_word():
	word_index = random.randint(1, len(word_list)-1)
	word = word_list[word_index]
	
	return word

def guessLetter_or_guessWord():
	print(f"""Choose one option from below, you only have 
{len(hangman_board)} attempt for guessing the whole 
word and {len(hangman_board)} attempt for guessing 
letter by letter\n\t1.Guess whole word\n\t2.Guess letter by letter
""")
	flag = True
	while flag:
		option = input("Enter your choice: ")
		if option.isdigit() and int(option) in [1, 2]:
			option = int(option)	
			return option
			flag = False
		else:
			print("Invalid input")
			print()

def player_choice():
	secret_word = get_random_word().lower()
	option = guessLetter_or_guessWord()
	
	if option == 1:
		print('You choose to guess whole word')
		print()
		attempt = 0
		guess = ""
		board_index = 0
		
		while guess != secret_word and attempt != len(hangman_board):
			guess = input("input your guess: ").lower()
			attempt += 1
			if guess == secret_word:
				print("Congrats, you guess right")
				break
			else:
				print(f"You missed, try again\n{7 - attempt} left")
				print(hangman_board[board_index])
				board_index += 1
		if guess != secret_word:
			print("Game over!\nYou hanged")
			print(f"The word is '{secret_word}'")
					
	else:
		print('You choose to guess letter by letter')
		print()
		blank = ["_"] * len(secret_word)
		guessed_letter  = ""
		attempt2 = 0
		board_index2 = 0
		print(" ".join(blank))
		print(f"Missed letters: {guessed_letter}")
		while blank != secret_word and attempt2 != len(hangman_board):
			guess = input("input your guess: ").lower()
			if guess in guessed_letter:
				print("Already guessed, try again")
				print(" ".join(blank))
				print(f"Missed letters: {guessed_letter}")
				print()
				if guess not in guessed_letter:
					guessed_letter = guessed_letter + guess
			elif guess in secret_word:
				if guess not in guessed_letter:
					guessed_letter = guessed_letter + guess
				print("Correct")
				for i in range(len(secret_word)):
					if guess == secret_word[i]:
						blank[i] = guess
				print(" ".join(blank))
				print(f"Missed letter: {guessed_letter}")
				print()
				if ''.join(blank) == secret_word:
					blank = ''.join(blank)
			elif guess not in guessed_letter and guess not in secret_word:
				guessed_letter = guessed_letter + guess
				print("Wrong!")
				print(hangman_board[board_index2])
				board_index2 += 1
				attempt2 += 1
				if attempt2 == len(hangman_board) - 1:
					print(f"You have {len(hangman_board) - attempt2} attempt left")
					print()
				elif attempt2 == len(hangman_board):
					print("Your attempt is exhausted")
					print()
				else:
					print(f"You have {len(hangman_board) - attempt2} attempts left")
					print()
				print(" ".join(blank))
				print(f"Missed letters: {guessed_letter}")
		if blank == secret_word:
			print("Congratulations. You finished guessing the letters")
			print(f"And it took you {attempt2} attempt to guess the whole word")
		else:
			print("Sorry, you couldn't make it\nYou hanged")
			print(f"The word is '{secret_word}'")
player_choice()

while True:
	flag = True
	while flag:
		print()
		player = input("Do you want to play again? (yes/no): ").lower()
		print()
		if player.isalpha() and player in ['y', 'yes', 'n', 'no']:
			flag = False
		else:
			print("Invalid input")
				
	if player in ["yes", "y"]:
		player_choice()
	else:
		break