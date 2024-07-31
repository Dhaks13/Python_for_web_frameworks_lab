"""
Design a program that assesses the strength of a given password based on specific
criteria and categorizes it as either "Weak," "Moderate," or "Strong."
• The program should prompt the user to enter a password.
• The password strength is determined based on the following criteria:
    o Length Check:
        § The password must be at least 8 characters long.
    o Case SensiMvity:
        § The password should contain a mix of uppercase and lowercase leaers.
    o Numeric Characters:
        § The password should include at least one numeric digit.
    o Special Characters:
        § The password should contain at least one special character from the set: !@#$%^&*(),.?":{}|<>
"""
#Making a main() funtionality
def main():
    password = input("Enter your password: ") #Getting user input
    l = len(password) #finding lenght of passsword
    hasnum,special = 0,0 # variables for checking number and special char
    multicase = 0 if (password == ( password.lower() or password.upper())) else 1 #check for multicase
    quality = 0 if (l<8 or (not multicase)) else 1 #check for lenght and multicase
    #Weak condtion
    if quality == 0:
        print("Weak Password")
        return #Return as password is no more modrate or strong
    #loop to iterate through password
    for i in password:
        #if it has a digit
        if (i.isdigit()):
            hasnum = 1
        #if it has a special charecter
        elif (i in "!@#$%^&*(),.?\":{}|<>"):
            special = 1
    #if the password satisfies Strong condition
    if (hasnum and special):
        print("Strong")
    #so it all fails it is moderate
    else:
        print("Moderate")

#Calling the main() fns
if __name__ == "__main__":
    main()
