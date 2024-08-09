"""
Create a Student Gradebook Management System
Design a Python program to manage a student gradebook, providing functionality
for adding students, inpu{ng their grades for various subjects, and calculating the
average grades for each student. Utilize dictionaries to store student information,
including names and corresponding lists to store grades for different subjects.
"""

# Define the student gradebook dictionary
gradebook = {}

def add_student(student_id, student_name):
    #Add a new student to the gradebook.
    if student_id in gradebook:
        print("Student ID already exists.")
        return
    
    gradebook[student_id] = {'name': student_name, 'grades': {}}
    print(f"Student '{student_name}' added successfully!")

def input_grades(student_id, subject, grade):
    #Input grades for a specific student and subject.
    if student_id not in gradebook:
        print("Student ID not found.")
        return
    
    if subject in gradebook[student_id]['grades']:
        print(f"Grade for subject '{subject}' updated to {grade}.")
    else:
        print(f"Grade for subject '{subject}' added.")
    
    gradebook[student_id]['grades'][subject] = grade

def view_grades(student_id):
    #View grades of a particular student.
    if student_id not in gradebook:
        print("Student ID not found.")
        return
    
    student = gradebook[student_id]
    print(f"\nStudent ID: {student_id} | Student Name: {student['name']}")
    print("Grades:")
    for subject, grade in student['grades'].items():
        print(f"{subject}: {grade}")

def calculate_average(student_id):
    #Calculate the average grade for a particular student.
    if student_id not in gradebook:
        print("Student ID not found.")
        return
    
    grades = gradebook[student_id]['grades'].values()
    if not grades:
        print("No grades available for this student.")
        return
    
    average = sum(grades) / len(grades)
    print(f"Average grade for {gradebook[student_id]['name']}: {average:.2f}")

def main():
    #Main function to interact with the user.
    print("Welcome to the Student Gradebook Management System!")
    
    while True:
        print("\n1. Add Student")
        print("2. Input Grades")
        print("3. View Grades")
        print("4. Calculate Average Grades")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            student_id = input("Enter student ID: ").strip()
            student_name = input("Enter student name: ").strip()
            add_student(student_id, student_name)
        
        elif choice == '2':
            student_id = input("Enter student ID: ").strip()
            subject = input("Enter subject name: ").strip()
            try:
                grade = float(input("Enter grade: ").strip())
                input_grades(student_id, subject, grade)
            except ValueError:
                print("Invalid grade input. Please enter a numeric value.")
        
        elif choice == '3':
                student_id = input("Enter student ID: ").strip()
            view_grades(student_id)
        
        elif choice == '4':
            student_id = input("Enter student ID: ").strip()
            calculate_average(student_id)
        
        elif choice == '5':
            print("Thank you for using the Student Gradebook Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
