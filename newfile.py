secret_number = 3
guess_number = 0

while guess_number < 3:
	guessed_number = int(input("Guess: "))
	guess_number = guess_number + 1
	
	if guessed_number == secret_number :
		print("You have won!")
		break 
	if guess_number == 3:
		print("You loss!")
