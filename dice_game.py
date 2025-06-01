#Dice Rolling Game
from random import randint

#Initialize player score
p1_score = 0
p2_score = 0

#Game Loop
while p1_score <100 and p2_score <100:
    #Player 1 turn
    roll = randint(1,6)
    print("Player 1 rolls:",roll)
    p1_score+= roll
    #Check if Player 1 has rolled a 6 if yes then he gets another turn
    while roll == 6:
        roll = randint(1,6)
        print("Player 1 rolls again:", roll)
        p1_score += roll
    print("Player 1's score:", p1_score)
    #Check if Player 1 has won
    if p1_score >= 100:
        print("Player 1 wins!")
        break
    #Player 2 turn
    roll = randint(1,6)
    print("Player 2 rolls:", roll)
    p2_score += roll
    #Check if Player 2 has rolled a 6 if yes then he gets another turn
    while roll == 6:
        roll = randint(1,6)
        print("Player 2 rolls again:", roll)
        p2_score += roll
    print("Player 2's score:", p2_score)
    #Check if Player 2 has won
    if p2_score >= 100:
        print("Player 2 wins!")
        break
#End of Game