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
