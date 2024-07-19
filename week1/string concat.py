"""
Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length
of the given string is less than 3, leave it unchanged.
"""

#get input for the user
string = input("Enter the string:")

#geting length of string
length = len(string)

#Applying the condition
if(length>=3):
    #comparing the last 3 char from str to "ing"
    if(string[-3:]=="ing"):
        #add 'ly' at last
        string += 'ly'
    else:
        #add 'ing' at last
        string += 'ing'

#printing the modified string
print("The Modified string: ",string)
