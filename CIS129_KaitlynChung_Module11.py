#Kaitlyn Chung
#Module 11: Lab
#These consist of exercises 9.1, 9.2, and 9.3 from Deitel & Deitel

#Exercise 9.1 - Writing code that enables you to store any number of grades into a grades.txt plain text file
grade = 'value'
with open('grades.txt',mode='w') as grades:
    while not grade.isnumeric():
        print('Please enter grade. Enter -1 to stop entering grades: ')
        grade=input()
        if grade != '-1':
            grade=int(grade)
            print(grade, file=grades)
            grade = 'string'
        else:
            break
            
#Exercise 9.2 - Write code that reads the grades from the grades.txt file you created, display individual grades and their total, count, and average

total = 0
count = 0

with open('grades.txt', mode='r') as grades:
    print('All Student Grades')
    for record in grades:
        print(record,end="")
        count += 1
        total += int(record)
print('The student has taken', count, 'tests')
print('The sum of the grades is', total)
print('The average test score for this student is', total/count)

#Exercise 9.3 - Write code that enables an instructor to enter each student's first name and last name as strings and the three grades as integers and save as a .csv.s
    
import csv
with open('grades.csv',mode='w',newline='') as grades:
    writer = csv.writer(grades)
    
    def tests(testnumber): #Determines the test score
        print(f'What was the score on test {testnumber}?')
        score = input()
        while not score.isnumeric() or int(score) < 0:
            print('Invalid entry. Test score is not in the approved range or not an integer.')
            print(f'What was the score on test {testnumber}?')
            score = input()
        return int(score)
    
    print("Please enter student's last name:")
    lastname = input()
    while not lastname.isalpha(): #Ensures the lastname is alphabetical
        print('Invalid entry. Names must be alphabetical.')
        print("Please enter student's last name:")
        lastname = input()
            
    print("Please enter student's first name:")
    firstname = input()
    while not firstname.isalpha(): #Ensures the first name is alphabetical
        print('Invalid entry. Names must be alphabetical.')
        print("Please enter student's last name:")
        firstname = input()
    
    exam1grade = tests(1)
    exam2grade = tests(2)
    exam3grade = tests(3)
    
    writer.writerow([firstname,lastname,exam1grade,exam2grade,exam3grade])
