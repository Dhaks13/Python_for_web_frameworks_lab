"""
Write a python program to convert Fahrenheit to Celsius and vice versa.
"""

#Function to convert Fahrenheit to Celsius
def convert_F_to_C(F):
    return (F-32)*5/9

#Function to convert Celsius to Fahrenheit
def convert_C_to_F(C):
    return (C*9)/5+32

#To Create a Menu Repetatively
while(True):
    print("Temperature Convertion:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    ch = int(input("Enter your Choice(1-3):"))
    if(ch==1):
        temp = float(input("Enter the temperatue in F:"))
        print(temp,"F is equal to",round(convert_F_to_C(temp),2),"C\n")
    elif(ch==2):
        temp = float(input("Enter the temperatue in C:"))
        print(temp,"C is equal to",round(convert_C_to_F(temp),2),"F\n")
    elif(ch==3):
        print("Exiting...\n")
        break
    else:
        print("Enter a Valid choice!!!\n")
