"""
Create a Python program for a simple console-based Rock-Paper-Scissors game
where a user can play against the computer.
Constraints:
• The program should provide a menu for the user to select Rock, Paper, or Scissors.
• The computer's choice should be randomly generated.
• The game should implement the standard Rock-Paper-Scissors rules:
    o Rock crushes Scissors.
    o Scissors cut Paper.
    o Paper covers Rock.
• The program should display the user's choice, the computer's choice, and the
        result of the round.
• The game should con7nue un7l the user chooses to exit.
• Implement input valida7on to handle invalid choices from the user.
"""
#import required module
import random as r

#function to return the choice value
def choice(ch):
    if ch==1:
        return "Rock"
    elif ch==2:
        return "Paper"
    else:
        return "Scissors"

#Setting up Score card
score_c = 0
score_u = 0

# Game in loop, Exit only when user likes
while True:
    #Game Options with Scoreboard
    print(f"""Welcome to Rock-Paper-Scissors Game!
    1. Rock
    2. Paper
    3. Scissors
    4. Exit
score: CPU -{score_c}  USER - {score_u}
""",end="")
    #Getting user choice
    ch = int(input("Enter your choice: "))
    #Exit condition and invalid input conditon
    if ch== 4:
        print("Exiting..")
        break
    elif ch>4:
        print("Invlid Input")
        continue

    #CPU Plays ON GAME
    comp = r.randint(1,3)
    win_case = 3 if (ch+2)%3==0 else (ch+2)%3   # Make the win case equal to comp
    #Game Stats display and classification of winner and loosers
    if ch == comp:
        print("Your choice and computer choice: ", choice(ch))  #print chioce
        print("Game Draw!") #print results
    elif comp == win_case:
        print("Your choice : ",  choice(ch), "\nCPU choice: ", choice(comp)) #print chioce
        print("You Won!") #print results
        score_u += 1    #Update Scores
    else:
        print("Your choice : ",  choice(ch), "\nCPU choice: ", choice(comp)) #print chioce
        print("You Lost!") #print results
        score_c += 1    #Update Scores
