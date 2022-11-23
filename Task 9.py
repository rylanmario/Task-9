#Name: Task 9.py
#Author: Rylan Fessey
#Date Created: October 30th, 2022
#Date Modified: November 22nd, 2022
# Purpose: The purpose of this program is to help student select the class they want to join.
#This is version 2.0, which includes bug fixes and improvements.



import sys

#This adds the courses to a dictionary.
Availablecourses = {
    "INFO0019": "Why Chromebooks are not a good laptop", 
    "INFO2901": "Windows and Operating Systems", 
    "INFO2390": "Computer Diagnostics", 
    "INFO3902": "Why computer programming is not for you" 
}

#This asks the user for information.
studentfirstName = input("What is your first name?: ")
studentlastName = input("What is your last name?: ")
studentNumber = input("What is your student number?: ")

#This tells the user what courses are available
sys.stdout.write("The courses available are as follows: ")
sys.stdout.write(",".join(
    ("{} (code : {})".format(Availablecourses[i], i)) 
    for i in Availablecourses))
sys.stdout.write("\n")

#This is where the student registers for the courses
Coursesregistered = input("Register for courses (Use a comma and space to seperate each selection):").split(", ")
print("-" * 10)

#This ensures that students verify the information
print("Name: {} {}\nStudent number:{}"
    .format(studentfirstName, studentlastName, studentNumber))

#This tells the user what courses are registered.
sys.stdout.write("Courses Registered: ")
sys.stdout.write(",".join(
    ("{} (code : {})".format(Coursesregistered[i], i)) 
    for i in Availablecourses))
sys.stdout.write("\n")

OutputFile = r"D:\Documents\output.txt"

aFile = open(OutputFile, 'a')

aFile.write(sys.stdout.write("Courses Registered: "))
aFile.write(sys.stdout.write(",".join(
    ("{} (code : {})".format(Coursesregistered[i], i)) 
    for i in Availablecourses)))
aFile.write(sys.stdout.write("\n"))