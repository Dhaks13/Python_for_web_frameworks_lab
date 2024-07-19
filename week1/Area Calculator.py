"""
Write a python program to calculate area of circle, rectangle and triangle.
"""
import math as m

#to Calculate area of circle 
def cir(R):
    return (m.pi)*R*R

#to Calculate area of Rectangle
def rect(L,B):
    return L*B

#to calculate area of Triangle
def tri(B,H):
    return 0.5*B*H

#To Create a Menu Repetatively
while(True):
    print("\nArea calculator:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")
    ch = int(input("Enter your Choice(1-4):"))
    if(ch==1):
        r=float(input("Enter the Radius:"))
        print("Area = ", round(cir(r),2))
    elif(ch==2):
        l=float(input("Enter the Length:"))
        b=float(input("Enter the Breath:"))
        print("Area = ", round(rect(l,b),2))
    elif(ch==3):
        b=float(input("Enter the Base Length:"))
        h=float(input("Enter the Height:"))
        print("Area = ", round(tri(b,h),2))
    elif(ch==4):
        print("Exiting...\n")
        break
    else:
        print("Enter a Valid choice!!!\n")

