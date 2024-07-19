"""
Write a Python program to exhibit the functional behavior of all the arithmetic
operators (+, -, *, /, //, **) and their order of precedence using COMPOUND
assignments in all the mathematical expressions.
"""

a = int(input("enter a number:"))
b = int(input("Enter another number:"))

#performing COMPOUND Addition
a+=b
print("a+=b, a=>",end="")
print(a)

#performing COMPOUND Subtraction
a-=b
print("a-=b, a=>",end="")
print(a)

#performing COMPOUND multiplication
a*=b
print("a*=b, a=>",end="")
print(a)

#performing COMPOUND division
a/=b
print("a/=b, a=>",end="")
print(a)

#performing COMPOUND floor division
a//=b
print("a//=b, a=>",end="")
print(a)

#performing COMPOUND exponent operation
a**=b
print("a**=b, a=>",end="")
print(a)

