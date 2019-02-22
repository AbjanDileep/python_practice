p1 = input("Player 1's turn: \n")
p2 = input("Player 2's turn: \n")
#player1 condition
if p1 == "rock" and p2 == "paper":
	print("Player 2 wins..!!")
elif p1 == "rock" and p2 == "scissors":
	print("Player 1 wins..!!")
elif p1 == "scissors" and p2 == "paper":
	print("Player 1 wins..!!")
elif p1 == "scissors" and p2 == "rock":
	print("Player 2 wins..!!")
elif p1 == "paper" and p2 == "scissors":
	print("Player 1 wins..!!")
elif p1 == "paper" and p2 == "rock":
	print("Player 2 wins..!!")
else:
	print("It's a tie..!!")	