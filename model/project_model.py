class Project:
    def __init__(self):
        self.name = ''
        self.desc = ''
        self.start_dt = ''
        self.task = ''
        print("intit")

    def addProject(self, name, desc, start_dt, task):
        self.name = name
        self.desc = desc
        self.start_dt = start_dt
        self.task = task

    def getProjectName(self):
        print("project: ", self.name)
        return self.name