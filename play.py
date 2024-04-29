import string
from courses import courses_for_it;
from courses import courses_for_civil;
from courses import courses_for_computer;
from courses import courses_for_bba; 

user_department = ''
department = ['civil', 'it', 'bba', 'computer']
mark_of_student = []

def main():
    global user_department, department
    user_department = input("Please enter your department: ").lower()
    if user_department in department:
        match user_department:
            case 'it':
                handle_department(courses_for_it)
            case 'civil':
                handle_department(courses_for_civil)
            case 'bba':
                handle_department(courses_for_bba)
            case 'computer':
                handle_department(courses_for_computer)
            case _:
                print("Your department has not registered any courses yet. Sorry!")

def handle_department(courses):
    global mark_of_student
    number = int(input('Enter the total number of students: '))
    title = f'Department of {user_department.capitalize()}\n'
    #Since the list is being dynamic so append'a'
    with open(f'D:\\Python\\education\\Students_Of_{user_department.capitalize()}.txt', 'a') as file:
        file.write(title)
        for i in range(number):
            print(f'Please enter details of Student {i+1}.')
            name = input('Please enter your name: ')
            student_details = f'Student {i+1}.\nName: {name}\n'
            mark_of_student = []
            for k in range(len(courses)):
                inp = float(input(f'Please enter your {courses[k]} mark: '))
                mark_of_student.append(inp)
            per, mark = calculation(mark_of_student)
            course_details = ''
            for n in range(len(mark_of_student)):
                course_details += f'\n{courses[n]}: {mark_of_student[n]}'
            keep = f'{student_details}Percentage: {per}%\nTotal Mark: {mark}{course_details}\n'
            file.write(keep)
            print('Your details have been successfully recorded in a file.......\n')

def calculation(marks):
    total_mark = sum(marks)
    length = len(marks)
    percentage = (total_mark / (length * 100)) * 100
    return percentage, total_mark

main()
