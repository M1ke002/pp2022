import numpy as np
import math
from domains.Student import Student
from domains.Course import Course


class Helper:
    def __init__(self):
        self.__studentList = []
        self.__courseList = []

    def getStudentList(self):
        return self.__studentList

    def getCourseList(self):
        return self.__courseList

    def getNumberOfStudents(self):
        number = int(input("Enter the number of students: "))
        return number

    def getStudentInfos(self,totalStudents):
        for i in range(totalStudents):
            id = input("Enter the student id: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student DOB: ")
            self.getStudentList().append(Student(id,name,dob))

    def getCourses(self):
        number = int(input("Enter the number of courses: "))
        return number

    def getCourseInfos(self,numberOfCourses):
        for i in range(numberOfCourses):
            id = input("Enter the course id: ")
            name = input("Enter the course name: ")
            credits = int(input("Enter the number of credits: "))
            self.getCourseList().append(Course(id,name,credits))

    def getCourseFromId(self,id):
        course = None
        courseList = self.getCourseList()
        for i in range(len(courseList)): #validate id
            if courseList[i].getId() == id :
                course = courseList[i]
                break
        return course

    def getStudentFromId(self,id):
        student = None
        studentList = self.getStudentList()
        for i in range(len(studentList)): #validate id
            if studentList[i].getId() == id :
                student = studentList[i]
                break
        return student

    def getMarks(self, id, studentList):
        course = self.getCourseFromId(id)
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

    def listCourses(self,courseList):
        if len(courseList) == 0:
            print("No courses found")
            return
        for i in range(len(courseList)):
            print("course id: {}, course name: {}, credits: {}".format(courseList[i].getId(), courseList[i].getName(), courseList[i].getCredits()))

    def listStudents(self,studentList):
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

    def listMarks(self, id, studentList):
        course = self.getCourseFromId(id)
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

    def getGPA(self,id):
        student = self.getStudentFromId(id)
        if student is None:
            print("Student not found")
            return
        print("GPA for student {}: {}".format(student.getName(), student.getGPA()))
