import math
import numpy as np

studentList = []
courseList = []

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__courses = {}
        self.__GPA = 0.0

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getId(self):
        return self.__id

    def getCourses(self):
        return self.__courses

    def getCourse(self, courseId):
        if (self.__courses.get(courseId) is None):
            return None
        return self.__courses.get(courseId)[0]

    def getMark(self, courseId):
        if (self.__courses.get(courseId) is None):
            return -1
        return self.__courses.get(courseId)[1]

    def getGPA(self):
        return self.__GPA
    
    def addCourse(self, id, course, mark):
        self.__courses[id] = [course, mark]

    def calGPA(self):
        weightedSum = 0
        totalCredits = 0
        for courseId in self.__courses:
            mark = self.getMark(courseId) #1:mark, 0:course
            course = self.getCourse(courseId)
            credits = course.getCredits()
            weightedSum += credits * mark
            totalCredits += credits
        if totalCredits == 0:
            return 0
        avg = weightedSum / totalCredits
        self.__GPA = round(avg, 2)

class Course:
    def __init__(self,id,name,credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCredits(self):
        return self.__credits

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
        credits = int(input("Enter the number of credits: "))
        courseList.append(Course(id,name,credits))

def getCourseFromId(id):
    course = None
    for i in range(len(courseList)): #validate id
        if courseList[i].getId() == id :
            course = courseList[i]
            break
    return course

def getStudentFromId(id):
    student = None
    for i in range(len(studentList)): #validate id
        if studentList[i].getId() == id :
            student = studentList[i]
            break
    return student

def getMarks(id, studentList):
    course = getCourseFromId(id)
    if course is None:
        print("Course not found")
        return
    if len(studentList) == 0:
        print("No students found for this course")
        return
    print("Entering marks for course {}:".format(course.getName()))
    for i in range(len(studentList)):
        message = "Enter mark for student {}: ".format(studentList[i].getName())
        mark = math.floor(float(input(message)))
        studentList[i].addCourse(id,course,mark)
        studentList[i].calGPA()

def listCourses(courseList):
    if len(courseList) == 0:
        print("No courses found")
        return
    for i in range(len(courseList)):
        print("course id: {}, course name: {}, credits: {}".format(courseList[i].getId(), courseList[i].getName(), courseList[i].getCredits()))

def listStudents(studentList):
    if len(studentList) == 0:
        print("No students found")
        return
    #sort students by ascending GPA
    GPAarray = []
    for student in studentList:
        GPAarray.append(student.getGPA())
    sortedGPAIndex = np.argsort(GPAarray)
    for i in reversed(sortedGPAIndex):
        print("student id: {}, name: {}, DOB: {}, GPA: {}".format(studentList[i].getId(), studentList[i].getName(), studentList[i].getDob(), studentList[i].getGPA()))

def listMarks(id, studentList):
    course = getCourseFromId(id)
    if course is None:
        print("Course not found")
        return
    if len(studentList) == 0:
        print("No students found for this course")
        return
    print("Marks for course {}:".format(course.getName()))
    for i in range(len(studentList)):
        if (studentList[i].getCourse(id) is None):
            print("No marks for student {} in this course".format(studentList[i].getName()))
        else:
            print("Student name: {}, mark: {}".format(studentList[i].getName(), studentList[i].getMark(id)))

def getGPA(id):
    student = getStudentFromId(id)
    if student is None:
        print("Student not found")
        return
    print("GPA for student {}: {}".format(student.getName(), student.getGPA()))


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
        totalStudents = getNumberOfStudents()
        getStudentInfos(totalStudents)
    elif (choice == 2):
        numberOfCourses = getCourses()
        getCourseInfos(numberOfCourses)
    elif (choice == 3):
        id = input("Enter the course id: ")
        getMarks(id, studentList)
    elif (choice == 4):
        listCourses(courseList)
    elif (choice == 5):
        listStudents(studentList)
    elif (choice == 6):
        id = input("Enter the course id: ")
        listMarks(id, studentList)
    elif (choice == 7):
        id = input("Enter the student id: ")
        getGPA(id)
    elif (choice == 8):
        break
    else:
        print("Invalid choice")
