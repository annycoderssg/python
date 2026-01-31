# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message

from sys import argv

class Students:
    # Dictionary to store the student marks
    studentList = {}

    # Constructor
    def __init__(self):
        self.studentList = {
            "John": 85,
            "Jane": 90,
            "Jim": 78,
            "Jill": 92
        }

    # Add the student to the list
    def addStudent(self, name, marks):
        self.studentList[name] = marks

    # Remove the student from the list
    def removeStudent(self, name):
        del self.studentList[name]

    # Update the marks of the student
    def updateStudent(self, name, marks):
        self.studentList[name] = marks

    # Get the marks of the student
    def getStudentMarks(self, name):
        if name not in self.studentList:
            print("Student not found")
            return
        return self.studentList[name]
        
    def getStudentList(self):
        return self.studentList

    def getChoice(self):
        return int(input("\nEnter your choice: "))
    
    @classmethod    
    def displayMenu(cls):
        print("\nMenu:")    
        print("1. View all students list")
        print("2. Add a student")
        print("3. Remove a student")
        print("4. Update a student marks")
        print("5. Get the marks of a student")
        print("6. Exit")

def main():
    print("\n===== Welcome to Student Dictionary Program =====")
    
    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("Help: This program is used to create a dictionary of student marks")
            exit()
        elif argv[1] == "-u" or argv[1] == "-U":
            print("Usage: python StudentsDisctionary.py <student_name> <marks>")
            exit()
 
    Students.displayMenu()

    objStudents = Students()

    choice = objStudents.getChoice()

    while choice != 6:
        match (choice):
            case 1:
                list = objStudents.getStudentList()
                print("\nAll Student's List:\n")
                for name in list:
                    print(f"Student Name: {name}, Marks: {list[name]}")
            case 2:
                name = input("Enter the name of the student: ")
                marks = int(input("Enter the marks of the student: "))
                print(objStudents.addStudent(name, marks))
            case 3:
                name = input("Enter the name of the student: ")
                print(objStudents.removeStudent(name))
            case 4:
                name = input("Enter the name of the student: ")
                marks = int(input("Enter the marks of the student: "))
                print(objStudents.updateStudent(name, marks))
            case 5:
                name = input("Enter the name of the student: ")
                print(f"{name}'s marks: {objStudents.getStudentMarks(name)}")
            case 6:
                print("Thank You!")
                exit()
            case _:
                print("Invalid option! Please enter a valid choice.")
                exit()
        
        Students.displayMenu()
        choice = objStudents.getChoice()

if __name__ == "__main__":
    main()