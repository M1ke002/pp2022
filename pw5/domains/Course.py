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