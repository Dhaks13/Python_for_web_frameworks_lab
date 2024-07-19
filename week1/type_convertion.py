"""
Write a Python program that takes user input as a string, converts it to an integer,
performs a mathematical operation (e.g., addition or multiplication) with another
integer, and then prints the result.
"""

#the Number is stored as string
a = input("Enter any number: ")

"""
\\ a*5 (or) a+5 raises error as 'a' is a string type
\\ a to be converted to int type to perform these operations
"""

#converting a to integer using int() func
a = int(a)

#performing addition and multiplication operation with 5 and printing it.
print("a + 5 = ",a+5)
print("a * 5 = ",a*5)
print()
