from tkinter import *
from controller.project_controller import add_new_project, display_all_project, get_project_by_name, edit_project_by_name

# project_list = Project()

def submit_add_project(app_add_project, name, desc, start_dt, task):
    app_add_project.destroy()
    # project_list.addProject(name, desc, start_dt, task)
    add_new_project(name, desc, start_dt, task)
    print("Project Added")
    print(name, desc, start_dt, task)


def submit_edit_project(app_edit_project,project_index, name, desc, start_dt, task):
    app_edit_project.destroy()
    edit_project_by_name(project_index, name, desc, start_dt, task)
    print("Project Edited")
    print(name, desc, start_dt, task)


def cancel_button_project(app_add_project):
    app_add_project.destroy()


def find_button_project(app_find_project, project_name):
    app_find_project.destroy()
    project_index = get_project_by_name(project_name)
    edit_project_window(project_index)

def add_project_window():
    app_add_project = Tk()
    app_add_project.title("Add New Project")

    # Label(app_add_project, text="Add New Project Here", font=20).pack()

    Label(app_add_project, text="Project Name").grid(row=0)
    Label(app_add_project, text="Project Description").grid(row=1)
    Label(app_add_project, text="Start Date").grid(row=2)
    Label(app_add_project, text="task").grid(row=3)

    project_name = Entry(app_add_project)
    project_description = Entry(app_add_project)
    project_start_dt = Entry(app_add_project)
    project_task = Entry(app_add_project)

    project_name.grid(row=0, column=1)
    project_description.grid(row=1, column=1)
    project_start_dt.grid(row=2, column=1)
    project_task.grid(row=3, column=1)

    add_button = Button(app_add_project, text='Add',
                        command=lambda: submit_add_project(app_add_project, project_name.get(), project_description.get(), project_start_dt.get(), project_task.get()))
    cancel_button = Button(app_add_project, text='Cancel',
                        command=lambda: cancel_button_project(app_add_project))

    add_button.grid(row=4, column=1)
    cancel_button.grid(row=4, column=2)

    app_add_project.geometry("500x300")
    app_add_project.mainloop()

def find_project_window():
    app_find_project = Tk()
    app_find_project.title("Enter Project Name")

    project_name = Entry(app_find_project)
    project_name.grid(row=0, column=1)

    find_button = Button(app_find_project, text='Find',
                        command=lambda: find_button_project(app_find_project, project_name.get()))
    cancel_button = Button(app_find_project, text='Cancel',
                        command=lambda: cancel_button_project(app_find_project))

    find_button.grid(row=1, column=1)
    cancel_button.grid(row=1, column=2)

    app_find_project.geometry("500x300")
    app_find_project.mainloop()

def edit_project_window(project_index):
    app_edit_project = Tk()
    app_edit_project.title("Edit Project")

    # Label(app_add_project, text="Add New Project Here", font=20).pack()

    Label(app_edit_project, text="Project Name").grid(row=0)
    Label(app_edit_project, text="Project Description").grid(row=1)
    Label(app_edit_project, text="Start Date").grid(row=2)
    Label(app_edit_project, text="task").grid(row=3)

    project_name = Entry(app_edit_project)
    project_description = Entry(app_edit_project)
    project_start_dt = Entry(app_edit_project)
    project_task = Entry(app_edit_project)

    project_name.grid(row=0, column=1)
    project_description.grid(row=1, column=1)
    project_start_dt.grid(row=2, column=1)
    project_task.grid(row=3, column=1)

    add_button = Button(app_edit_project, text='Edit',
                        command=lambda: submit_edit_project(app_edit_project, project_index, project_name.get(), project_description.get(), project_start_dt.get(), project_task.get()))
    cancel_button = Button(app_edit_project, text='Cancel',
                        command=lambda: cancel_button_project(app_edit_project))

    add_button.grid(row=4, column=1)
    cancel_button.grid(row=4, column=2)

    app_edit_project.geometry("500x300")
    app_edit_project.mainloop()


def show(label, clicked):
    label.config(text=clicked.get())

def delete_project_window():
    app_edit_project = Tk()
    app_edit_project.title("Edit Project")

    # Label(app_add_project, text="Add New Project Here", font=20).pack()

    options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("Monday")

    # Create Dropdown menu
    drop = OptionMenu(app_edit_project, clicked, *options)
    drop.pack()

    # Create button, it will change label text
    button = Button(app_edit_project, text="click Me",
                    command=lambda: show(label, clicked)).pack()

    # Create Label
    label = Label(app_edit_project, text=" ")
    label.pack()

    app_edit_project.geometry("500x300")
    app_edit_project.mainloop()

def display_project_window():
    app_show_project = Tk()
    app_show_project.title("Show All Project")

    project_list = display_all_project()
    i = 0
    for project in project_list:
        print(project.getProjectName())
        label = Label(app_show_project, text=project.getProjectName())
        label.grid(row=i,column=1)
        i += 1

    app_show_project.geometry("500x300")
    app_show_project.mainloop()
