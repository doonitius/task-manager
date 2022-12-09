from tkinter import *
from menu.project_menu import add_project_window, edit_project_window, delete_project_window
from menu.task_menu import add_task_window
def close_main(app):
    app.destroy()

def back_to_main(app):
    app.destroy()
    main()

def director_menu(app):
    close_main(app)
    print('You are director')
    app_director = Tk()
    app_director.title("Task-Scheduler @Director")

    Label(app_director,text="Director", font=20).pack()

    menubar = Menu(app_director)
    app_director.config(menu=menubar)

    project_menu = Menu(
        menubar,
        tearoff=0
    )

    exit_menu = Menu(
        menubar,
        tearoff=0
    )

    # add menu items to the File menu
    project_menu.add_command(label='Add Project', command=add_project_window)
    project_menu.add_command(label='Edit Project', command=edit_project_window)
    project_menu.add_command(label='Delete Project', command=delete_project_window)

    menubar.add_cascade(
        label="Project",
        menu=project_menu
    )

    exit_menu.add_command(
        label='Return to Root User',
        command=lambda: back_to_main(app_director)
    )
    # add Exit menu item
    exit_menu.add_command(
        label='Exit Program',
        command=app_director.destroy
    )

    menubar.add_cascade(
        label="Exit",
        menu=exit_menu
    )

    app_director.geometry("500x500")
    app_director.mainloop()


def manager_menu(app):
    close_main(app)
    print('You are manager')
    app_manager = Tk()
    app_manager.title("Task-Scheduler @Manager")

    Label(app_manager, text="Manager", font=20).pack()

    menubar = Menu(app_manager)
    app_manager.config(menu=menubar)

    task_menu = Menu(
        menubar,
        tearoff=0
    )

    team_menu = Menu(
        menubar,
        tearoff=0
    )

    exit_menu = Menu(
        menubar,
        tearoff=0
    )

    # add menu items to the File menu
    task_menu.add_command(label='Add Task', command=add_task_window)
    task_menu.add_command(label='Edit Task')
    task_menu.add_command(label='Delete Task')

    menubar.add_cascade(
        label="Task",
        menu=task_menu
    )

    team_menu.add_command(label='Add Team')
    team_menu.add_command(label='Edit Team')
    team_menu.add_command(label='Delete Team')

    menubar.add_cascade(
        label="Team",
        menu=team_menu
    )

    exit_menu.add_command(
        label='Return to Root User',
        command=lambda: back_to_main(app_manager)
    )
    # add Exit menu item
    exit_menu.add_command(
        label='Exit Program',
        command=app_manager.destroy
    )

    menubar.add_cascade(
        label="Exit",
        menu=exit_menu
    )


    app_manager.geometry("500x500")
    app_manager.mainloop()


def developer_menu(app):
    close_main(app)
    print('You are developer')
    app_developer = Tk()
    app_developer.title("Task-Scheduler @Developer")

    Label(app_developer, text="Developer", font=20).pack()
    menubar = Menu(app_developer)
    app_developer.config(menu=menubar)

    task_menu = Menu(
        menubar,
        tearoff=0
    )

    exit_menu = Menu(
        menubar,
        tearoff=0
    )

    # add menu items to the File menu
    task_menu.add_command(label='View Task Board')
    task_menu.add_command(label='Update Task Status')
    task_menu.add_command(label='Review Request')

    menubar.add_cascade(
        label="Task",
        menu=task_menu
    )

    exit_menu.add_command(
        label='Return to Root User',
        command=lambda: back_to_main(app_developer)
    )
    # add Exit menu item
    exit_menu.add_command(
        label='Exit Program',
        command=app_developer.destroy
    )

    menubar.add_cascade(
        label="Exit",
        menu=exit_menu
    )

    app_developer.geometry("500x500")
    app_developer.mainloop()



def main():
    app = Tk()
    app.title('Task-Scheduler')

    select_user = Label(text="Who are you?",font=20)
    select_user.pack()

    director_button = Button(app,text='Director', command= lambda: director_menu(app))
    manager_button = Button(app, text='Manager', command= lambda: manager_menu(app))
    developer_button = Button(app,text='Developer', command= lambda: developer_menu(app))

    director_button.pack(side = LEFT, expand =True)
    manager_button.pack(side=LEFT, expand=True)
    developer_button.pack(side=LEFT, expand=True)

    app.geometry("500x500")
    app.mainloop()
    
if __name__ == "__main__":
    main()