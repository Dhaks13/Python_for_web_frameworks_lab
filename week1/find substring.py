"""
Create a Python program that takes two strings as input and determines if the second
string is a substring of the first one.
"""

#get user string input
string = input("Enter the String: ")
substr = input("Enter the string to find: ")
#print the index of where the substring exisits
index = string.find(substr)
if(index!=-1):
    print("The string is found at: ", string.find(substr))
else:
    print("The sub-string not found")
print()
