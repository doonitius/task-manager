from model.project_model import Project
from model.project_list_model import ProjectList

project_list = ProjectList()

def add_new_project(name, desc, start_dt, task):
    print("add new project")
    
    new_project = Project(name, desc, start_dt, task)

    project_list.add_project_to_list(new_project)

def edit_project_by_name(project_index,name, desc, start_dt, task):
    print("edit project")

def display_all_project():
    for i in project_list.get_project_list():
        print("display all project: ",i.getProjectName())
    return project_list.get_project_list()

def get_project_by_name(name):
    i = 0
    for project in project_list.get_project_list():
        if name == project.getProjectName():
            print("found", project.getProjectName())
            return i
        i += 1
