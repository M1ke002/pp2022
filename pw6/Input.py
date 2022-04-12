from domains.Student import Student
from domains.Course import Course
import os
import zipfile
import pickle
import math

class Input:
    def __init__(self):
        self.__studentFile = "students.txt"
        self.__courseFile = "courses.txt"
        self.__markFile = "marks.txt"
        self.__dataFile = "students.dat"
        self.__studentData = []
        self.__courseData = []
        self.__markData = []

    def getStudentFile(self):
        return self.__studentFile

    def getCourseFile(self):
        return self.__courseFile

    def getMarkFile(self):
        return self.__markFile

    def getDataFile(self):
        return self.__dataFile

    def getStudentData(self):
        return self.__studentData

    def getCourseData(self):
        return self.__courseData

    def getMarkData(self):
        return self.__markData
    
    def getNumberOfStudents(self):
        number = int(input("Enter the number of students: "))
        return number

    def getStudentInfos(self,totalStudents,helper):
        for i in range(totalStudents):
            id = input("Enter the student id: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student DOB: ")
            helper.getStudentList().append(Student(id,name,dob))
            data = {
                "id": id,
                "name": name,
                "dob": dob
            }
            self.getStudentData().append(data)

    def getCourses(self):
        number = int(input("Enter the number of courses: "))
        return number

    def getCourseInfos(self,numberOfCourses,helper):
        for i in range(numberOfCourses):
            id = input("Enter the course id: ")
            name = input("Enter the course name: ")
            credits = int(input("Enter the number of credits: "))
            helper.getCourseList().append(Course(id,name,credits))
            data = {
                "id": id,
                "name": name,
                "credits": credits
            }
            self.getCourseData().append(data)

    def getMarks(self, courseId, helper):
        studentList = helper.getStudentList()
        course = helper.getCourseFromId(courseId)
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
            studentList[i].addCourse(courseId,course,mark)
            studentList[i].calGPA()
            data = {
                "courseId": courseId,
                "studentId": studentList[i].getId(),
                "mark": mark
            }
            self.getMarkData().append(data)

    def writeToFiles(self):
        try:
            file = open(self.getStudentFile(),"wb")
            pickle.dump(self.getStudentData(),file)
            file.close()
            file = open(self.getCourseFile(),"wb")
            pickle.dump(self.getCourseData(),file)
            file.close()
            file = open(self.getMarkFile(),"wb")
            pickle.dump(self.getMarkData(),file)
            file.close()
        except Exception as e:
            print(e)

    def compressFiles(self):
        try:
            with zipfile.ZipFile(self.getDataFile(),"w") as zip:
                zip.write(self.getStudentFile())
                zip.write(self.getCourseFile())
                zip.write(self.getMarkFile())
                zip.write(self.getDataFile())
        except Exception as e:
            print(e)
    
    def decompressFiles(self):
        try:
            with zipfile.ZipFile(self.getDataFile(),"r") as zip:
                zip.extractall()
                return True
        except Exception as e:
            print(e)
            return False

    def removeFiles(self):
        if (os.path.exists(self.getStudentFile())):
            os.remove(self.getStudentFile())
        if (os.path.exists(self.getCourseFile())):
            os.remove(self.getCourseFile())
        if (os.path.exists(self.getMarkFile())):
            os.remove(self.getMarkFile())