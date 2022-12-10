class Project:
    def __init__(self, name, desc, start_dt, task):
        self.__name = name
        self.__desc = desc
        self.__start_dt = start_dt
        self.__task = task

    def getProjectName(self):
        return self.__name

    def getProjectDesc(self):
        return self.__desc

    def getProjectStartDt(self):
        return self.__start_dt

    def getProjectTask(self):
        return self.__task

    def setProjectName(self, name):
        self.__name = name
