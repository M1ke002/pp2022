def getNumberOfStudents():
    number = int(input("Enter the number of students: "))
    return number

def getStudentInfos(totalStudents):
    studentList = []
    for i in range(totalStudents):
        id = input("Enter the student id: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student DOB: ")
        student = {
            "id": id,
            "name": name,
            "dob": dob
        }
        studentList.append(student)
    return studentList

def getCourses():
    number = int(input("Enter the number of courses: "))
    return number

def getCourseInfos(numberOfCourses):
    courseList = []
    for i in range(numberOfCourses):
        courseId = input("Enter the course id: ")
        courseName = input("Enter the course name: ")
        course = {
            "id": courseId,
            "name": courseName
        }
        courseList.append(course)
    return courseList

def getMarks(course, studentList):
    if studentList == None:
        print("No students found for this course")
        return
    for i in range(len(studentList)):
        message = "Enter mark for student {}: ".format(studentList[i]["name"])
        mark = float(input(message))
        studentList[i][course] = mark

def listCourses(courseList):
    if courseList == None:
        print("No courses found")
        return
    for i in range(len(courseList)):
        print("course id: {}, course name: {}".format(courseList[i]["id"], courseList[i]["name"]))

def listStudents(studentList):
    if studentList == None:
        print("No students found")
        return
    for i in range(len(studentList)):
        print("student id: {}, student name: {}, student DOB: {}".format(studentList[i]["id"], studentList[i]["name"], studentList[i]["dob"]))

def listMarks(course, studentList):
    if studentList == None:
        print("No students found for this course")
        return
    print("Marks for course {}:".format(course))
    for i in range(len(studentList)):
        if (studentList[i].get(course) == None):
            print("No marks for student {} in this course".format(studentList[i]["name"]))
        else:
            print("Student name: {}, mark: {}".format(studentList[i]["name"], studentList[i][course]))


print("Student management program")
studentList = None
courseList = None
while True:
    print("1. Enter student infos")
    print("2. Enter course infos")
    print("3. Enter marks for students")
    print("4. List courses")
    print("5. List students")
    print("6. List marks")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        totalStudents = getNumberOfStudents()
        studentList = getStudentInfos(totalStudents)
    elif (choice == 2):
        numberOfCourses = getCourses()
        courseList = getCourseInfos(numberOfCourses)
    elif (choice == 3):
        course = input("Enter the course name: ")
        getMarks(course, studentList)
    elif (choice == 4):
        listCourses(courseList)
    elif (choice == 5):
        listStudents(studentList)
    elif (choice == 6):
        course = input("Enter the course name: ")
        listMarks(course, studentList)
    elif (choice == 7):
        break
    else:
        print("Invalid choice")


