##############################################
#Simple Rock, Paper, Scissors game in Python #
#Created 26/05/20                            #
#Justin Holder                               #
##############################################

# Import required module, 'Random' so we can use the 'randint' function to select random integers.

from random import randint

# Create a list of playing options

t = ["Rock", "Paper", "Scissors"]

#setup players - computer and the user
#assign a random play to to the computer
computer = t[randint(0,2)]

# Set the player to False
player = False

while player == False:
# Now set player to True
	player = input ("Rock, Paper,Scissors? ")
	if player == computer: # If player and computer make the same options
		print("Draw!") 
	elif player == "Rock": # Outline options if player chooses Rock
		if computer == "Paper":
			print("You lose!", computer, "covers", player)
		else:
			print("You win!", player, "smashes", computer)
	elif player == "Paper": # Outline options if player chooses Paper
		if computer == "Scissors":
			print("You lose", computer, "cuts", player)
		else:
			print("You win!", player, "covers", computer)
	elif player == "Scissors": # Outline options if player chooses Scissors
		if computer == "Rock":
			print("You lose!", computer, "smashes", player)
		else:
			print("You win!", player, "cuts", computer)
	else:
		print("Not a valid play! Check your spelling.")
	# Player was True, now set back to False so loop can repeat.
	player = False
	computer = t[randint(0,2)]
	
	