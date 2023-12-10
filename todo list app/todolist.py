from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image



# Create the main window
window = Tk()
window.title("To-Do App")
# Set background color
window.configure(bg="#f5f5f5")
# Set the icon for the application window
window.iconbitmap(r"C:\Users\Abdur Razzaq\Downloads\todo list app\target.ico")

# Set the background image
image = Image.open(r"C:\Users\Abdur Razzaq\Downloads\todo list app\bg.jpeg")
image = image.resize((750, 400), Image.BILINEAR)  # Resize the image the way you want
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# Creating a list to store tasks
tasks = []

# Function --> To Add The Task
def add_task():
    def save_task():
        new_task = entry_task.get()
        if new_task:
            tasks.append(new_task)
            messagebox.showinfo("Success", "Task added successfully!")
            update_list()
            root.destroy()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    root = Toplevel(window)
    root.title("Add Task")
    # Set bg-color
    root.configure(bg="#f5f5f5")

    entry_task = Entry(root, width=30)
    entry_task.pack(pady=10)

    button_save = Button(root, text="Save", command=save_task)
    button_save.pack(pady=5)

# Function -->  To delete The Task
def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this task?")
        if confirmed:
            tasks.pop(selected_task[0])
            update_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function -->  To edit The Task
def edit_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        current_task = tasks[selected_task[0]]

        def save_changes():
            new_task = entry_edit.get()
            if new_task:
                tasks[selected_task[0]] = new_task
                messagebox.showinfo("Success", "Task edited successfully!")
                update_list()
                root.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a task!")

        root = Toplevel(window)
        root.title("Edit Task")
        # Set background color
        root.configure(bg="#f5f5f5")

        entry_edit = Entry(root, width=30)
        entry_edit.insert(0, current_task)
        entry_edit.pack(pady=10)

        button_save = Button(root, text="Save Changes", command=save_changes)
        button_save.pack(pady=5)
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# Function --> To Mark a Task As Completed
def complete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        task = tasks[selected_task[0]]
        if task.endswith(" ✔"):
            messagebox.showinfo("Info", "Task already marked as complete!")
        else:
            task = task + " ✔"
            tasks[selected_task[0]] = task
            update_list()
            messagebox.showinfo("Success", "Task marked as complete!")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete!")

# Function --> To Update The Task --> example Rename
def update_list():
    listbox_tasks.delete(0, END)
    for task in tasks:
        listbox_tasks.insert(END, task)

# Frame To hold the task-list and Scrollbar
frame_task = Frame(window)
frame_task.pack()

#listbox To Display the Tasks
listbox_tasks = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="Helvetica")
listbox_tasks.pack(side=LEFT)

# Create a scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

# Creating  Buttons for Adding, Deleting, Editing, and Completing tasks
button_add = Button(window, text="Add Task", width=50, command=add_task)
button_add.pack(pady=5)

button_delete = Button(window, text="Delete Task", width=50, command=delete_task)
button_delete.pack(pady=5)

button_edit = Button(window, text="Edit Task", width=50, command=edit_task)
button_edit.pack(pady=5)

button_complete = Button(window, text="Complete Task", width=50, command=complete_task)
button_complete.pack(pady=5)

window.mainloop()