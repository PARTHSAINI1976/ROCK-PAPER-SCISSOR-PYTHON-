import random

list = ["rock","paper","scissor"]

PLAYER_1 = random.choice(list)
print("THE PLAYER 1 CHOOSES :", PLAYER_1)

PLAYER_2 = random.choice(list)
print("THE PLAYER 2 CHOOSES :", PLAYER_2)

if(PLAYER_1 == PLAYER_2):
    print("NO ONE WINS")

elif(PLAYER_1 == "rock" and PLAYER_2 == "scissor"):
    print("PLAYER1 WINS!")

elif(PLAYER_1 =="paper" and PLAYER_2 == "rock"):
    print("PLAYER1 WINS!")

elif(PLAYER_1 == "scissor" and PLAYER_2 == "paper"):
    print("PLAYER1 WINS!")

elif(PLAYER_1 =="rock" and PLAYER_2 =="paper"):
    print("PLAYER2 WINS!")

elif(PLAYER_1 == "paper" and PLAYER_2 == "scissor"):
    print("PLAYER2 WINS!")

elif(PLAYER_1 =="scissor" and PLAYER_2 == "rock"):
    print("PLAYER2 WINS!")

else:
    print("!VALUE ERROR!")