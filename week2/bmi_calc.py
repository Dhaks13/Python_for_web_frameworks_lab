"""
Write a python program to calculate Body Mass Index (BMI) based on user input.

bmi = weight / (height ** 2)
bmi less than 18.5, print 'Underweight'
18.5 <= bmi < 25, print 'Normal Weight'
25 <= bmi < 30, print 'Overweight'
else 'Obese'
"""
#Getting the value of weight and height
weight = float(input("Enter the weight (in Kg): "))
height = float(input("Enter the Height (in m): "))

#Calculating and displaying BMI
bmi = weight/(height**2)
print(f"Your BMI is : {bmi: .2f}")

#Classify the group based on BMI
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal Weight")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")
