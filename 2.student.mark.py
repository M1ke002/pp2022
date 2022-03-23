studentList = []
courseList = []

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__courses = {}

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getId(self):
        return self.__id

    def getCourse(self, course):
        return self.__courses.get(course)
    
    def addCourse(self, course, mark):
        self.__courses[course] = mark

class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

def getNumberOfStudents():
    number = int(input("Enter the number of students: "))
    return number

def getStudentInfos(totalStudents):
    for i in range(totalStudents):
        id = input("Enter the student id: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student DOB: ")
        studentList.append(Student(id,name,dob))

def getCourses():
    number = int(input("Enter the number of courses: "))
    return number

def getCourseInfos(numberOfCourses):
    for i in range(numberOfCourses):
        id = input("Enter the course id: ")
        name = input("Enter the course name: ")
        courseList.append(Course(id,name))

def getMarks(course, studentList):
    found = False
    for i in range(len(courseList)):
        if courseList[i].getName() == course :
            found = True
            break
    if not found:
        print("Course not found")
        return
    if len(studentList) == 0:
        print("No students found for this course")
        return
    for i in range(len(studentList)):
        message = "Enter mark for student {}: ".format(studentList[i].getName())
        mark = float(input(message))
        studentList[i].addCourse(course, mark)

def listCourses(courseList):
    if len(courseList) == 0:
        print("No courses found")
        return
    for i in range(len(courseList)):
        print("course id: {}, course name: {}".format(courseList[i].getId(), courseList[i].getName()))

def listStudents(studentList):
    if len(studentList) == 0:
        print("No students found")
        return
    for i in range(len(studentList)):
        print("student id: {}, student name: {}, student DOB: {}".format(studentList[i].getId(), studentList[i].getName(), studentList[i].getDob()))

def listMarks(course, studentList):
    if len(studentList) == 0:
        print("No students found for this course")
        return
    print("Marks for course {}:".format(course))
    for i in range(len(studentList)):
        if (studentList[i].getCourse(course) == None):
            print("No marks for student {} in this course".format(studentList[i].getName()))
        else:
            print("Student name: {}, mark: {}".format(studentList[i].getName(), studentList[i].getCourse(course)))


print("Student management program")

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
        getStudentInfos(totalStudents)
    elif (choice == 2):
        numberOfCourses = getCourses()
        getCourseInfos(numberOfCourses)
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


