#Games

print("\n\n****** ROCK, PAPER, SCISSORS GAME **********\n\n")

p1 = input("Player 1's turn: \n").lower()
print("\n\n************ NO CHEATING *********\n\n"*60)
p2 = input("Player 2's turn: \n").lower()

if p1:
	if p2:
		if p1 == "rock" or p1 == "paper" or p1 == "scissors":
			if p1 == p2:
				print("It's a tie..!!")

			if p1 == "rock":
				if p2 == "paper":
					print("Player 2 wins..!!")
				elif p2 == "scissors":
					print("Player 1 wins..!!")
				else:
					print("Invalid Input")

			if p1 == "scissors":
				if p2 == "paper":
					print("Player 1 wins..!!")
				elif p2 == "rock":
					print("Player 2 wins..!!")
				else:
					print("Invalid Input")

			if p1 == "paper":
				if p2 == "scissors":
					print("Player 2 wins..!!")
				elif p2 == "rock":
					print("Player 1 wins..!!")
				else:
					print("Invalid Input")
		else:
			print("Invalid Input")

	else:
		print("Please Enter Input")
else:
	print("Please Enter Input")

