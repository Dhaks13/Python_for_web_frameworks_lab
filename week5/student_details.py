"""
Write a program to show the details of the students who are all scored the total mark
> 250. Create a List of List to store the N number of students' details such as Rollno,
name, Mark1, Mark2, Mark3. Write all the students' details in “Data.csv” using an
user defined function. Include another user defined function called extract() to read
the student details if the total mark is above 250 and store it in another
“OUTPUT.csv” file. Print both the file contents.
"""
#imports
import csv

#user-defined funtion
#write fn
def write(file,data):
    #Write the data into csv file
    with open(file,'w',newline='') as fw:
        writer = csv.writer(fw)
        writer.writerows(data)
    return

#read fn
def read():
    #Read the data from csv file
    rList = []
    with open("DATA.csv") as fr:
        reader = csv.reader(fr)
        for row in reader:
            rList.append(row)
        print(rList)
        return rList

#list-of-list to store student details
students=[]
N = int(input("Enter number of students:"))

#get the data from user
for i in range(N):
    roll = input("Enter Roll No:.")
    name = input("Enter Name:.")
    m1 = float(input("Enter mark 1:."))
    m2 = float(input("Enter mark 2:."))
    m3 = float(input("Enter mark 3:."))
    students.append([roll,name,m1,m2,m3])
write("DATA.csv",students)
rStudents = read()
print()

#filter data by total marks
out = []
for row in rStudents:
    if (float(row[-1])+float(row[-2])+float(row[-3]))>250 :
        print(row)
        out.append(row)
write("OUTPUT.csv",out)

