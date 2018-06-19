import random
print("rock...")
print("paperrrrr...")
print("scissor...")

player1 = input("Player, Make your move:")
print("***NO cheating************* \n" *20)


r = random.randint(1,3)
if r == 1:
	computer = "rock"
elif r == 2:
	computer ="scissor"
else:
	computer="paper"
print("computer choose" , computer)


if player1=="rock" and computer=="scissor":
	print("player1 Wins!!!!!")

elif player1=="rock" and computer=="paper":
	print("computer Wins!!!!!!!")

elif player1 =="paper" and computer=="scissor":
	print("computer2 Wins!!!!!!!!")

elif player1 =="paper" and computer=="rock":
	print("player1 Wins!!!!!!!!")

elif player1 =="scissor" and computer=="rock":
	print("computer Wins!!!!!!!!".upper())

elif player1 =="scissor" and computer=="paper":
	print("player1 Wins!!!!!!!!".upper())

elif player1==computer:
	print("draw")

else:
	print("something wrong try again")