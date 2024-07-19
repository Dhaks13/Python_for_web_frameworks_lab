"""
Write a Python program to exhibit the functional behavior of all the arithmetic
operators (+, -, *, /, //, **) and their order of precedence.
"""

a = int(input("enter a number:"))
b = int(input("Enter another number:"))

#performing Addition
c=a+b
print(a,"+",b,"=",c)

#performing Subtraction
d=a-b
print(a,"-",b,"=",d)

#performing multiplication
m=a*b
print(a,"x",b,"=",m)

#performing division
d=a/b
print(a,"/",b,"=",d)

#performing floor division
f=a//b
print(a,"//",b,"=",f)

#performing exponent operation
e=a**b
print(a,"**",b,"=",e)

#using multiple operator to study the order of precedence
"""
Order:
() -> Paranthesis
** -> Expoential (right to left)
* (or) / -> Multipilcation (or) Division
+ (or) - -> Addition (or) Subration
"""
expression = (a-b)*d+c-a**f*(a//c)
"""
Here order is:
1. (a-b)
2. (a//c)
3. a**f
4. (a-b)*d
5. (a**f)*(a//c)
6. ((a-b)*d)+c
7. (((a-b)*d)+c)-((a**f)*(a//c))
"""
print("(",a,"-",b,")*",d,"+",c,"-",a,"**",f,"*(",a,"//",c,") = ",expression)
print("Steps:")
print("(a-b) =>",(a-b))
print("(a//c) =>",(a//c))
print("a**f =>",a**f)
print("(a-b)*d =>",(a-b)*d)
print("(a**f)*(a//c) =>",(a**f)*(a//c))
print("((a-b)*d)+c =>",((a-b)*d)+c)
print("(((a-b)*d)+c)-((a**f)*(a//c)) =>",(((a-b)*d)+c)-((a**f)*(a//c)))
