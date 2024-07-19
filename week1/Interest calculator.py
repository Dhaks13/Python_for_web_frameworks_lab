"""
Write a python program to calculate simple and compound interest.
"""

def si(P,R,T):
    return (P*R*T)/100

def ci(P,R,T):
    return (P*((1+R*0.01)**T))-P

while(True):
    print("Interest calculator:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Exit")
    ch = int(input("Enter your Choice(1-3):"))
    if(ch==1):
        p=float(input("Enter the Principle Amount:"))
        r=float(input("Enter the Rate of interest(in %):"))
        t=float(input("Enter the Time period(in years):"))
        print("Simple Interest = ", round(si(p,r,t),2))
    elif(ch==2):
        p=float(input("Enter the Principle Amount:"))
        r=float(input("Enter the Rate of interest(in %):"))
        t=float(input("Enter the Time period(in years):"))
        print("Compund Interest = ", round(ci(p,r,t),2))
    elif(ch==3):
        print("Exiting...\n")
        break
    else:
        print("Enter a Valid choice!!!\n")

