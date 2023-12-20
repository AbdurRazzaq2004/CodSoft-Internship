import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    length = int(length)

    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(window)
password_entry.pack()

window.mainloop()