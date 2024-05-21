import string
from courses import courses_for_it;  # Import IT courses from the courses module
from courses import courses_for_civil;  # Import Civil courses from the courses module
from courses import courses_for_computer;  # Import Computer courses from the courses module
from courses import courses_for_bba;  # Import BBA courses from the courses module

# Initialize global variables
user_department = '';
department = ['civil', 'it', 'bba', 'computer'];  # List of valid departments
mark_of_student = [];  # List to store student marks

# Main function to determine the user's department and handle accordingly
def main():
    global user_department, department;
    user_department = input("Please enter your department: ").lower();  # Get the user's department
    if user_department in department:  # Check if the department is valid
        match user_department:  # Match the department to handle appropriately
            case 'it':
                handle_department(courses_for_it);  # Handle IT department
            case 'civil':
                handle_department(courses_for_civil);  # Handle Civil department
            case 'bba':
                handle_department(courses_for_bba);  # Handle BBA department
            case 'computer':
                handle_department(courses_for_computer);  # Handle Computer department
            case _:
                print("Your department has not registered any courses yet. Sorry!");  # Default case for unregistered department

# Function to handle the specific department and record student details
def handle_department(courses):
    global mark_of_student;
    number = int(input('Enter the total number of students: '));  # Get the total number of students
    title = f'Department of {user_department.capitalize()}\n';  # Title for the file
    # Open the file for appending student details
    #any desired location of the text file can be given....
    with open(f'D:\\Python\\education\\Students_Of_{user_department.capitalize()}.txt', 'a') as file:
        file.write(title);  # Write the title to the file
        for i in range(number):  # Loop to get details for each student
            print(f'Please enter details of Student {i+1}.');
            name = input('Please enter your name: ');  # Get the student's name
            student_details = f'Student {i+1}.\nName: {name}\n';  # Prepare student details
            mark_of_student = [];  # Reset the marks list for each student
            for k in range(len(courses)):  # Loop to get marks for each course
                inp = float(input(f'Please enter your {courses[k]} mark: '));
                mark_of_student.append(inp);  # Append the mark to the list
            per, mark = calculation(mark_of_student);  # Calculate percentage and total marks
            course_details = '';  # Initialize course details string
            for n in range(len(mark_of_student)):  # Loop to prepare course details string
                course_details += f'\n{courses[n]}: {mark_of_student[n]}';
            keep = f'{student_details}Percentage: {per:.2f}%\nTotal Mark: {mark}{course_details}\n';  # Prepare final student record
            file.write(keep);  # Write the student record to the file
            print('Your details have been successfully recorded in a file.......\n');  # Confirmation message

# Function to calculate total marks and percentage
def calculation(marks):
    total_mark = sum(marks);  # Calculate the total marks
    length = len(marks);  # Get the number of courses
    percentage = (total_mark / (length * 100)) * 100;  # Calculate the percentage
    return percentage, total_mark;  # Return percentage and total marks

# Run the main function 
main();
