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
    # Hide the login window
    root.withdraw()

    # Run the main application
    subprocess.run(["python", "main.py"])

    # Destroy the login window when the main application is closed
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("User Login")

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
password_entry = tk.Entry(root, show="*", font=label_font)

# login button
login_button = tk.Button(root, text="Login", command=login, font=button_font)

# Layout - Grid
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
