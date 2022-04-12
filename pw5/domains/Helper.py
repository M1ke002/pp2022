import json
from domains.Student import *
from domains.Course import *

class Helper:
    def __init__(self):
        self.__studentList = []
        self.__courseList = []

    def getStudentList(self):
        return self.__studentList

    def getCourseList(self):
        return self.__courseList

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

    def loadStudentInfo(self, fileName):
        try:
            with open(fileName, 'r') as file:
                line = file.readline()
                while line:
                    data = json.loads(line) #get a dictionary
                    student = Student(data["id"],data["name"],data["dob"])
                    self.getStudentList().append(student)
                    line = file.readline()
        except Exception as e:
            print(e)

    def loadCourseInfo(self, fileName):
        try:
            with open(fileName, 'r') as file:
                line = file.readline()
                while line:
                    data = json.loads(line) #get a dictionary
                    course = Course(data["id"],data["name"],data["credits"])
                    self.getCourseList().append(course)
                    line = file.readline()
        except Exception as e:
            print(e)

    def loadMarks(self, fileName):
        try:
            with open(fileName, 'r') as file:
                line = file.readline()
                while line:
                    data = json.loads(line) #get a dictionary
                    studentId = data["studentId"]
                    course = self.getCourseFromId(data["courseId"])
                    mark = data["mark"]
                    for i in range(len(self.getStudentList())):
                        if self.getStudentList()[i].getId() == studentId:
                            self.getStudentList()[i].addCourse(course.getId(),course,mark)
                            self.getStudentList()[i].calGPA()
                            break
                    line = file.readline()
        except Exception as e:
            print(e)

