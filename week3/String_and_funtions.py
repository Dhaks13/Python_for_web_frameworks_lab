"""
Develop a Python function that accomplishes the following tasks using recursion:
    a. Check if two strings represent each other in reverse order. Print each character
        of a given string in reverse order, displaying each character on a new line.
    b. Count the number of vowels present in a given string
    c. Define the relationship between the length of a string (len) and the number of
        characters printed (num) on the screen. Ensure len is always greater than 0.
"""

def palindrome(str1,str2):
    """
    Funtion to check if the two strings represent each other in reverse order.
    Print each character of a given string in reverse order,
    displaying each character on a new line.

    para:
        str1 - String - first string
        str2 - String - second string

    return type: None
    """
    #Check for palindrome
    if(str1.lower() == str2[::-1].lower()):
        # Print the string
        for i in str2:
            print(i)
    else:
        print("The string is not Palindrome")


def vowels_count(str1):
    """
    Funtion to count the number of vowels in the string
    para:
        str1 - String
    return type: int - vc(vowel count)
    """
    v = ['a','e','i','o','u']  # list of vowels
    vc = 0 # vowel count
    # for each charecter in the string
    for i in str1:
        # if Vowel increment the vc(vowel count)
        if i.lower() in v:
            vc += 1
    #return the vc
    return vc

def char_on_screen(str1):
    """
    Funtion to count the charecters on screen
    to demonstrate the len() funtion

    para:
        str1 - String

    return type: int - count of string
    """
    cos = 0
    for i in str1:
        cos += 1
    return cos


# Get two Stings
string_A = input("Enter a String: ")
string_B = input("Enter another String: ")

# Testing all the funtions and Displaying results
palindrome(string_A,string_B)
print("Vowels in String :", vowels_count(string_A))
print("Vowels in another String :", vowels_count(string_B))
print("Charecters on Screen for String A: ", char_on_screen(string_A), " Length: ",len(string_A))
print("Charecters on Screen for String B: ", char_on_screen(string_B), " Length: ",len(string_B))

