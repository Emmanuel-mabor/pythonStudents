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
            open_login_application()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def open_login_application():
    # Hide the registration window
    root.withdraw()

    # Run the login application
    subprocess.run(["python", "login.py"])

    # Destroy the registration window when the login application is closed
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("User Registration")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the center of the screen
x = (screen_width - 400) // 2  # You can adjust 400 to change the window width
y = (screen_height - 200) // 2  # You can adjust 200 to change the window height

# Set the window size and position
root.geometry("400x200+{}+{}".format(x, y))

root.configure(bg="lightblue")

# Increase the size of labels and buttons
label_font = ("Arial", 14)
button_font = ("Arial", 14)

# labels
username_label = tk.Label(root, text="Username", font=label_font)
password_label = tk.Label(root, text="Password", font=label_font)

# entry fields
username_entry = tk.Entry(root, font=label_font)
password_entry = tk.Entry(root, show="*", font=label_font)  # The 'show' option hides the password characters

# registration button
register_button = tk.Button(root, text="Register", command=register_user, font=button_font, bg="red")

# Layout - Grid
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
register_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
