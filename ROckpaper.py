print("rock...")
print("paper...")
print("scissor...")

player1 = input("Player1, Make your move:")
print("***NO cheating************* \n" *20)





player2 = input("Player 2, Make your move:")

if player1=="rock" and player2=="scissor":
	print("player1 Wins!!!!!")

elif player1=="rock" and player2=="paper":
	print("player2 Wins!!!!!!!")

elif player1 =="paper" and player2=="scissor":
	print("player2 Wins!!!!!!!!")

elif player1 =="paper" and player2=="rock":
	print("player1 Wins!!!!!!!!")

elif player1 =="scissor" and player2=="rock":
	print("player2 Wins!!!!!!!!")

elif player1 =="scissor" and player2=="paper":
	print("player1 Wins!!!!!!!!")

elif player1==player2:
	print("draw")

else:
	print("something wrong try again")