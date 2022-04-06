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


