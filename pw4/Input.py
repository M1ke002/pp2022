import math
from domains.Student import Student
from domains.Course import Course

class Input:
    def getNumberOfStudents(self):
        number = int(input("Enter the number of students: "))
        return number

    def getStudentInfos(self,totalStudents,helper):
        for i in range(totalStudents):
            id = input("Enter the student id: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student DOB: ")
            helper.getStudentList().append(Student(id,name,dob))

    def getCourses(self):
        number = int(input("Enter the number of courses: "))
        return number

    def getCourseInfos(self,numberOfCourses,helper):
        for i in range(numberOfCourses):
            id = input("Enter the course id: ")
            name = input("Enter the course name: ")
            credits = int(input("Enter the number of credits: "))
            helper.getCourseList().append(Course(id,name,credits))

    def getMarks(self, id, helper):
        studentList = helper.getStudentList()
        course = helper.getCourseFromId(id)
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