import numpy as np

class Output:
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

    def listMarks(self, id, helper):
        studentList = helper.getStudentList()
        course = helper.getCourseFromId(id)
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

    def getGPA(self,id,helper):
        student = helper.getStudentFromId(id)
        if student is None:
            print("Student not found")
            return
        print("GPA for student {}: {}".format(student.getName(), student.getGPA()))