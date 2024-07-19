"""
Develop a Python func7on to determine if a given string is a palindrome. Ignore
spaces, punctuation, and capitalization in the comparison.
"""

#geting the string from user and keep a cpy
string = input("Enter any string: ")
cpy = string
#Performing some operation to remove space, pantuation and make lowercase
cpy=cpy.replace(" ","").replace(",","").replace(".","").replace("!","")
cpy=cpy.lower()
#string in reverse format using string slicing
revstr = cpy[::-1]
print(revstr," ", cpy)
if(revstr==cpy):
    print(string, " is a Palindrome")
else:
    print(string, " is not a Palindrome")
print()
