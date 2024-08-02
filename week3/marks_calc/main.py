"""
Create a Python module named marks_Calculator that encapsulates funcMonaliMes
for students' marks computaMon in different subjects. Within this module, design
a funcMon that:
    a. Takes inputs and calculates the total marks obtained by a student in various
        subjects.
    b. Computes the average marks and grade obtained by the student across all
        subjects.
    c. Returns the calculated average marks and grade.
"""
#Importing marks_Calculator module as mc
import marks_Calculator as mc

#main() funtion
def main():
    # Get no. of subjects and create marks list
    num_sub = int(input("Enter the number of subjects: "))
    marks = []

    # For each subject get marks
    for i in range(num_sub):
        mark = float(input(f"Enter the mark for subject {i+1} : "))
        marks.append(mark)

    # Call the funtions to caluclate
    total_marks = mc.calculate_total_marks(marks)
    average_marks,grade = mc.calculate_average_and_grade(total_marks,num_sub)

    # Printing the result
    print(f"Total Marks: {total_marks:.2f}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")


# if this is not a module
if __name__=='__main__':
    main()
