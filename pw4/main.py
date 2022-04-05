from domains.Helper import Helper

helper = Helper()

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
        totalStudents = helper.getNumberOfStudents()
        helper.getStudentInfos(totalStudents)
    elif (choice == 2):
        numberOfCourses = helper.getCourses()
        helper.getCourseInfos(numberOfCourses)
    elif (choice == 3):
        id = input("Enter the course id: ")
        helper.getMarks(id, helper.getStudentList())
    elif (choice == 4):
        helper.listCourses(helper.getCourseList())
    elif (choice == 5):
        helper.listStudents(helper.getStudentList())
    elif (choice == 6):
        id = input("Enter the course id: ")
        helper.listMarks(id, helper.getStudentList())
    elif (choice == 7):
        id = input("Enter the student id: ")
        helper.getGPA(id)
    elif (choice == 8):
        break
    else:
        print("Invalid choice")
