from tkinter import *

def submit_add_task(app_add_task, name, desc, start_dt, duration, status):
    app_add_task.destroy()
    print("Task Added")
    print(name, desc, start_dt, duration, status)


def submit_edit_task(app_edit_task, name, desc, start_dt, duration, status):
    app_edit_task.destroy()
    print("Task Edited")
    print(name, desc, start_dt, duration, status)


def cancel_button_task(app_task):
    app_task.destroy()


def add_task_window():
    app_add_task = Tk()
    app_add_task.title("Add New Task")

    # Label(app_add_task, text="Add New Project Here", font=20).pack()

    Label(app_add_task, text="Task Name").grid(row=0)
    Label(app_add_task, text="Task Description").grid(row=1)
    Label(app_add_task, text="Start Date").grid(row=2)
    Label(app_add_task, text="Duration").grid(row=3)
    Label(app_add_task, text="Status").grid(row=4)

    task_name = Entry(app_add_task)
    task_description = Entry(app_add_task)
    task_start_dt = Entry(app_add_task)
    task_duration = Entry(app_add_task)
    task_status = Entry(app_add_task)

    task_name.grid(row=0, column=1)
    task_description.grid(row=1, column=1)
    task_start_dt.grid(row=2, column=1)
    task_duration.grid(row=3, column=1)
    task_status.grid(row=4, column=1)

    add_button = Button(app_add_task, text='Add',
                        command=lambda: submit_add_task(app_add_task, task_name.get(), task_description.get(), task_start_dt.get(), task_duration.get(), task_status.get()))
    cancel_button = Button(app_add_task, text='Cancel',
                        command=lambda: cancel_button_task(app_add_task))

    add_button.grid(row=5, column=1)
    cancel_button.grid(row=5, column=2)

    app_add_task.geometry("500x300")
    app_add_task.mainloop()
