from domains.Helper import Helper
from Input import Input
from Output import Output

helper = Helper()
inputObj = Input()
outputObj = Output()

print("Student management program")
while True:
    print("1. Enter student infos")
    print("2. Enter course infos")
    print("3. Enter marks for students")
    print("4. List courses")
    print("5. List students descending GPA order")
    print("6. List marks")
    print("7. Get average GPA for a student")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        totalStudents = inputObj.getNumberOfStudents()
        inputObj.getStudentInfos(totalStudents,helper)
    elif (choice == 2):
        numberOfCourses = inputObj.getCourses()
        inputObj.getCourseInfos(numberOfCourses,helper)
    elif (choice == 3):
        id = input("Enter the course id: ")
        inputObj.getMarks(id, helper)
    elif (choice == 4):
        outputObj.listCourses(helper.getCourseList())
    elif (choice == 5):
        outputObj.listStudents(helper.getStudentList())
    elif (choice == 6):
        id = input("Enter the course id: ")
        outputObj.listMarks(id, helper)
    elif (choice == 7):
        id = input("Enter the student id: ")
        outputObj.getGPA(id,helper)
    elif (choice == 8):
        break
    else:
        print("Invalid choice")
