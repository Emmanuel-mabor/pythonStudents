import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (entered_username, entered_password))
        user = cursor.fetchone()
        connection.close()

        if user:
            messagebox.showinfo("Login", "Login successful!")
            open_main_application()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_main_application():
    try:
        subprocess.run(['python', 'main.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open main.py: {str(e)}")

root = tk.Tk()




root.title("User Login")

#  labels
username_label = tk.Label(root, text="Username")
password_label = tk.Label(root, text="Password")

# entry fields
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

#  login button
login_button = tk.Button(root, text="Login", command=login)

# Layout - Grid
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, columnspan=2)


root.mainloop()
