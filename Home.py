import tkinter as tk
from tkinter import ttk
import subprocess  # Import the subprocess module for running external scripts

# Function to open the registration script
def open_registration_script():
    subprocess.run(["python", "user_registration.py"])  # Replace with the actual script name

# Function to open the login script
def open_login_script():
    subprocess.run(["python", "login.py"])  # Replace with the actual script name

# Create the main application window
root = tk.Tk()
root.title("University System")

# Set the window size and position it in the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create labels and buttons
label = tk.Label(root, text="University System", font=("Arial", 24, "bold"), bg="white")
label.pack(pady=20)

register_button = tk.Button(root, text="Register", command=open_registration_script, width=20)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=open_login_script, width=20)
login_button.pack()

# Start the GUI application
root.mainloop()
