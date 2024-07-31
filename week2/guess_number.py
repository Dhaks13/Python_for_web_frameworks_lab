"""
Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
appears again until the guess is correct, on successful guess, user will get a "Well
guessed!" message, and the program will exit.
"""
#importing the random number generating module
import random

#looping for try/play again
while True:
    num = random.randint(1,9) #Random number genration
    user = int(input("Enter 0 to exit :\nEnter your Guessed Number(1-9):")) #Getting user input 
    # Conditonal Statements to make further decisions
    if (user == 0):
        print("Exiting...")
        break
    elif (user == num):
        print("Congratulations! Well guessed!")
        print("Playing again!")
    else:
        print("Better luck next time!")
        
