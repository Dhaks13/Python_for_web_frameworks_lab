"""
Create a Personal InformaMon Management with Tuple Packing and Unpacking
Create a Python program that captures information about a person, including their
name, age, and address. Utilize tuple packing to store this information in a tuple, and
then use tuple unpacking to retrieve and display the information.
"""
#funtion for getting input and returning it as tuple
def input_packing():
    name = input("Enter Name: ")
    age = int(input("Enter age: "))
    add = input("Enter Address: ")
    return name,age,add

#funtion to unpack the tuple and display the content in it
def unpack_display(tup):
    name = tup[0]
    age = tup[1]
    add = tup[2]
    print(f"\nName : {name}\nAge: {age}\nAddress: {add}\n")


#Calling both the funtions
personal_info = input_packing()
unpack_display(personal_info)
