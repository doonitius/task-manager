from tkinter import *
from tkinter import ttk
from menu.project_menu import add_project_window, find_project_window, delete_project_window, display_project_window
from menu.task_menu import add_task_window

from controller.user_controller import user_login, get_user_info


def close_main(app):
    app.destroy()

def back_to_main(app):
    app.destroy()
    main()

def main_menu(current_user):
    root = Tk()
    root.title("Task-Schedule @Main")
    tabControl = ttk.Notebook(root)

    tab_project = ttk.Frame(tabControl)
    tab_task = ttk.Frame(tabControl)

    tabControl.add(tab_project, text='Prject')
    tabControl.add(tab_task, text='Task')
    tabControl.pack(expand=1, fill="both")

    user_name, user_role = get_user_info(current_user)

    ttk.Label(tab_project,text="Welcome to Task Scheduler " + user_name).grid(column=0,row=0)
    ttk.Label(tab_project,text="Role: " + user_role).grid(column=0,row=1)
    Button(tab_project, text="Add Project", command=add_project_window).grid(column=0,row=2)
    Button(tab_project, text="Edit Project", command=find_project_window).grid(column=0,row=3)
    Button(tab_project, text="Display Project", command=display_project_window).grid(column=0,row=4)
    Button(tab_project, text="Delete Project", command=delete_project_window).grid(column=0,row=5)

    ttk.Label(tab_task,text="Lets dive into the\world of computers").grid(column=0,row=0,padx=30,pady=30)

    root.geometry("300x300")
    root.mainloop()

def login_user(app, user_id, user_name):
    close_main(app)
    current_user = user_login(user_id, user_name)
    main_menu(current_user)



# def director_menu(app):
#     close_main(app)
#     print('You are director')
#     app_director = Tk()
#     app_director.title("Task-Scheduler @Director")

#     Label(app_director,text="Director", font=20).pack()

#     menubar = Menu(app_director)
#     app_director.config(menu=menubar)

#     project_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     exit_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     # add menu items to the File menu
#     project_menu.add_command(label='Add Project', command=add_project_window)
#     project_menu.add_command(label='Edit Project', command=edit_project_window)
#     project_menu.add_command(label='Delete Project', command=delete_project_window)
#     project_menu.add_command(label='Display Project', command=display_project_window)

#     menubar.add_cascade(
#         label="Project",
#         menu=project_menu
#     )

#     exit_menu.add_command(
#         label='Return to Root User',
#         command=lambda: back_to_main(app_director)
#     )
#     # add Exit menu item
#     exit_menu.add_command(
#         label='Exit Program',
#         command=app_director.destroy
#     )

#     menubar.add_cascade(
#         label="Exit",
#         menu=exit_menu
#     )

#     app_director.geometry("500x500")
#     app_director.mainloop()


# def manager_menu(app):
#     close_main(app)
#     print('You are manager')
#     app_manager = Tk()
#     app_manager.title("Task-Scheduler @Manager")

#     Label(app_manager, text="Manager", font=20).pack()

#     menubar = Menu(app_manager)
#     app_manager.config(menu=menubar)

#     task_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     team_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     exit_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     # add menu items to the File menu
#     task_menu.add_command(label='Add Task', command=add_task_window)
#     task_menu.add_command(label='Edit Task')
#     task_menu.add_command(label='Delete Task')

#     menubar.add_cascade(
#         label="Task",
#         menu=task_menu
#     )

#     team_menu.add_command(label='Add Team')
#     team_menu.add_command(label='Edit Team')
#     team_menu.add_command(label='Delete Team')

#     menubar.add_cascade(
#         label="Team",
#         menu=team_menu
#     )

#     exit_menu.add_command(
#         label='Return to Root User',
#         command=lambda: back_to_main(app_manager)
#     )
#     # add Exit menu item
#     exit_menu.add_command(
#         label='Exit Program',
#         command=app_manager.destroy
#     )

#     menubar.add_cascade(
#         label="Exit",
#         menu=exit_menu
#     )


#     app_manager.geometry("500x500")
#     app_manager.mainloop()


# def developer_menu(app):
#     close_main(app)
#     print('You are developer')
#     app_developer = Tk()
#     app_developer.title("Task-Scheduler @Developer")

#     Label(app_developer, text="Developer", font=20).pack()
#     menubar = Menu(app_developer)
#     app_developer.config(menu=menubar)

#     task_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     exit_menu = Menu(
#         menubar,
#         tearoff=0
#     )

#     # add menu items to the File menu
#     task_menu.add_command(label='View Task Board')
#     task_menu.add_command(label='Update Task Status')
#     task_menu.add_command(label='Review Request')

#     menubar.add_cascade(
#         label="Task",
#         menu=task_menu
#     )

#     exit_menu.add_command(
#         label='Return to Root User',
#         command=lambda: back_to_main(app_developer)
#     )
#     # add Exit menu item
#     exit_menu.add_command(
#         label='Exit Program',
#         command=app_developer.destroy
#     )

#     menubar.add_cascade(
#         label="Exit",
#         menu=exit_menu
#     )

#     app_developer.geometry("500x500")
#     app_developer.mainloop()

def main():
    app = Tk()
    app.title('Task-Scheduler @Login')

    select_user = Label(text="Who are you?",font=20)
    select_user.grid(row=0,column=1)

    Label(app, text = "User ID").grid(row=1)
    Label(app, text = "User Name").grid(row=2)

    user_id = Entry(app)
    user_name = Entry(app)

    user_id.grid(row=1, column=1)
    user_name.grid(row=2, column=1)

    login = Button(app, text="Login", command = lambda: login_user(app,user_id.get(),user_name.get()))

    login.grid(row=3, column=1)

    app.geometry("300x200")
    app.mainloop()
    
if __name__ == "__main__":
    main()