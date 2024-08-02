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
#Defining all the given Funtions
def calculate_total_marks(marks):
    """
    funtion to calculate the total marks
    para:
        marks - list - contains set of marks scored by student
    return type: int/ float - sum of all  the marks scored    
    """
    return sum(marks) # return total marks

def calculate_average_and_grade(total_marks,num_subjects):
    """
    funtion to calculate the average and grade
    para:
        total_marks - int/float - total marks scored
        num_subjects - int
    return type: tuple - average_mark , grade
    """
    average_marks = total_marks/num_subjects # calculating average marks
    # finding the grade based on average
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >=80:
        grade = 'B'
    elif average_marks >=70:
        grade = 'C'
    elif average_marks >=60:
        grade = 'D'
    else:
        grade = 'F'
    return average_marks,grade # return the average and grade
