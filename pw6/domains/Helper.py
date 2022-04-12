import pickle
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
            file = open(fileName, 'rb')
            data = pickle.load(file)
            for item in data:
                student = Student(item["id"],item["name"],item["dob"])
                self.getStudentList().append(student)
            file.close()
        except Exception as e:
            print(e)

    def loadCourseInfo(self, fileName):
        try:
            file = open(fileName, 'rb')
            data = pickle.load(file)
            for item in data:
                course = Course(item["id"],item["name"],item["credits"])
                self.getCourseList().append(course)
            file.close()
        except Exception as e:
            print(e)

    def loadMarks(self, fileName):
        try:
            file = open(fileName, 'rb')
            data = pickle.load(file)
            for item in data:
                studentId = item["studentId"]
                course = self.getCourseFromId(item["courseId"])
                mark = item["mark"]
                for i in range(len(self.getStudentList())):
                    if self.getStudentList()[i].getId() == studentId:
                        self.getStudentList()[i].addCourse(course.getId(),course,mark)
                        self.getStudentList()[i].calGPA()
                        break
            file.close()
        except Exception as e:
            print(e)

