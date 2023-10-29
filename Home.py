import tkinter as tk

import subprocess

#  registration script
def open_registration_script():
    subprocess.run(["python", "register.py"])

#  the login script
def open_login_script():
    subprocess.run(["python", "login.py"])

# main application window
root = tk.Tk()
root.title("University System")

root.configure(bg="lightblue")
# window size and position it in the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# labels and buttons
label = tk.Label(root, text="University System", font=("Arial", 24, "bold"), bg="white")
label.pack(pady=20)

register_button = tk.Button(root, text="Register", command=open_registration_script, width=40, height=5,bg="red")
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=open_login_script, width=40, height=5, bg="red")
login_button.pack()


root.mainloop()
