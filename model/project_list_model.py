class ProjectList:
    def __init__(self):
        self.__project = []

    def add_project_to_list(self, project):
        self.__project.append(project)

    def get_project_list(self):
        return self.__project