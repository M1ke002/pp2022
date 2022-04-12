from domains.Helper import Helper
from Input import Input
from Output import Output

helper = Helper()
inputData = Input()
outputData = Output()

#load data
if (inputData.decompressFiles()):
    helper.loadStudentInfo(inputData.getStudentFile())
    helper.loadCourseInfo(inputData.getCourseFile())
    helper.loadMarks(inputData.getMarkFile())

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
        totalStudents = inputData.getNumberOfStudents()
        inputData.getStudentInfos(totalStudents,helper)
    elif (choice == 2):
        numberOfCourses = inputData.getCourses()
        inputData.getCourseInfos(numberOfCourses,helper)
    elif (choice == 3):
        id = input("Enter the course id: ")
        inputData.getMarks(id, helper)
    elif (choice == 4):
        outputData.listCourses(helper.getCourseList())
    elif (choice == 5):
        outputData.listStudents(helper.getStudentList())
    elif (choice == 6):
        id = input("Enter the course id: ")
        outputData.listMarks(id, helper)
    elif (choice == 7):
        id = input("Enter the student id: ")
        outputData.getGPA(id,helper)
    elif (choice == 8):
        inputData.writeToFiles()
        inputData.compressFiles()
        inputData.removeFiles()
        break
    else:
        print("Invalid choice")
