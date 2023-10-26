import tkinter as tk
import sqlite3
from tkinter import messagebox
import subprocess

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        try:
            connection = sqlite3.connect('user_database.db')
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            connection.close()
            messagebox.showinfo("Registration", "User registered successfully!")

            # Open the login.py script after successful registration
            subprocess.run(["python", "login.py"])
        except Exception as e:
            messagebox.showerror("Error", str(e))




root = tk.Tk()
root.title("User Registration")

# labels
username_label = tk.Label(root, text="Username")
password_label = tk.Label(root, text="Password")

# entry fields
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

# registration button
register_button = tk.Button(root, text="Register", command=register_user)

# Layout - Grid
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
register_button.grid(row=2, columnspan=2)


root.mainloop()
