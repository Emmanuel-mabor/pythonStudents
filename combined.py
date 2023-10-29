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

register_button = tk.Button(root, text="Register", command=open_registration_script, width=40, height=5, bg="red")
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=open_login_script, width=40, height=5, bg="red")
login_button.pack()


root.mainloop()
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
login_button = tk.Button(root, text="Login", command=login, font=button_font, bg="red")

# Layout - Grid
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
import subprocess
import tkinter as tk
from tkinter import ttk, font
import sqlite3
import logging

def create_student_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        student_id TEXT UNIQUE,
        department TEXT,
        course TEXT
    )
    """)

def register_student():
    name = name_entry.get()
    student_id = student_id_entry.get()
    department = department_entry.get()
    course = course_entry.get()

    if not name or not student_id:
        message_label.config(text="Name and Student ID are required", fg="red")
        logging.error("Failed to register student: Name and Student ID are required")
    else:
        try:
            cursor.execute("INSERT INTO students (name, student_id, department, course) VALUES (?, ?, ?, ?)",
                           (name, student_id, department, course))
            conn.commit()
            message_label.config(text="Student registered successfully", fg="green")
            name_entry.delete(0, "end")
            student_id_entry.delete(0, "end")
            department_entry.delete(0, "end")
            course_entry.delete(0, "end")
            view_students()
            logging.info(f"Student registered: Name={name}, Student ID={student_id}")
        except sqlite3.Error as e:
            message_label.config(text="Database error: " + str(e), fg="red")
            logging.error("Database error during student registration: " + str(e))

def view_students():
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        student_table.delete(*student_table.get_children())

        for student in students:
            student_table.insert("", "end", values=(student[0], student[1], student[2], student[3], student[4]))
    except sqlite3.Error as e:
        message_label.config(text="Database error: " + str(e), fg="red")
        logging.error("Database error during student data retrieval: " + str(e))

def delete_student():
    selected_item = student_table.selection()
    if selected_item:
        student_id = student_table.item(selected_item, "values")[0]
        try:
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            message_label.config(text="Student deleted successfully", fg="green")
            view_students()
        except sqlite3.Error as e:
            message_label.config(text="Database error: " + str(e), fg="red")
            logging.error("Database error during student deletion: " + str(e))
    else:
        message_label.config(text="Select a student to delete", fg="red")

def edit_student():
    selected_item = student_table.selection()
    if selected_item:
        student_id = student_table.item(selected_item, "values")[0]
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Student")

        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student_info = cursor.fetchone()

        def save_changes():
            new_name = name_edit.get()
            new_student_id = student_id_edit.get()
            new_department = department_edit.get()
            new_course = course_edit.get()
            try:
                cursor.execute("UPDATE students SET name=?, student_id=?, department=?, course=? WHERE id=?",
                               (new_name, new_student_id, new_department, new_course, student_id))
                conn.commit()
                message_label.config(text="Student information updated successfully", fg="green")
                view_students()
                edit_window.destroy()
            except sqlite3.Error as e:
                message_label.config(text="Database error: " + str(e), fg="red")
                logging.error("Database error during student information update: " + str(e))

        name_edit = tk.Entry(edit_window)
        student_id_edit = tk.Entry(edit_window)
        department_edit = tk.Entry(edit_window)
        course_edit = tk.Entry(edit_window)

        name_edit.insert(0, student_info[1])
        student_id_edit.insert(0, student_info[2])
        department_edit.insert(0, student_info[3])
        course_edit.insert(0, student_info[4])

        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, bg="red")

        name_label_edit = tk.Label(edit_window, text="Name:")
        student_id_label_edit = tk.Label(edit_window, text="Student ID:")
        department_label_edit = tk.Label(edit_window, text="Department:")
        course_label_edit = tk.Label(edit_window, text="Course:")

        name_label_edit.grid(row=0, column=0)
        name_edit.grid(row=0, column=1)
        student_id_label_edit.grid(row=1, column=0)
        student_id_edit.grid(row=1, column=1)
        department_label_edit.grid(row=2, column=0)
        department_edit.grid(row=2, column=1)
        course_label_edit.grid(row=3, column=0)
        course_edit.grid(row=3, column=1)
        save_button.grid(row=4, columnspan=2)

def generate_report():
    try:
        cursor.execute("SELECT department, COUNT(*) FROM students GROUP BY department")
        department_data = cursor.fetchall()

        if department_data:
            logging.info("Generating data analytics report")

            report_window = tk.Toplevel(root)
            report_window.title("Data Analytics Report")

            report_label = tk.Label(report_window, text="Department-wise Student Count:")
            report_label.pack()

            report_text = tk.Text(report_window, height=10, width=40)
            report_text.pack()
            report_text.insert(tk.END, "Department\tStudent Count\n")

            for row in department_data:
                department, count = row
                report_text.insert(tk.END, f"{department}\t{count}\n")

    except sqlite3.Error as e:
        message_label.config(text="Database error: " + str(e), fg="red")
        logging.error("Database error during report generation: " + str(e))

def log_out():
    subprocess.Popen(["python", "Home.py"])
    root.destroy()

root = tk.Tk()
root.title("Student Registration System")

root.configure(bg="lightblue")

# the window size to fit the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

#  custom font for labels, buttons, and entry widgets
custom_font = font.nametofont("TkDefaultFont")
custom_font.configure(family="Arial", size=16)

#  configure labels, entry widgets, and buttons
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
student_id_label = tk.Label(root, text="Student ID:")
student_id_entry = tk.Entry(root)
department_label = tk.Label(root, text="Department:")
department_entry = tk.Entry(root)
course_label = tk.Label(root, text="Course:")
course_entry = tk.Entry(root)
register_button = tk.Button(root, text="Register", command=register_student, bg="red")
view_button = tk.Button(root, text="View Students", command=view_students, bg="red")
delete_button = tk.Button(root, text="Delete Student", command=delete_student, bg="red")
edit_button = tk.Button(root, text="Edit Student", command=edit_student, bg="red")
generate_report_button = tk.Button(root, text="Generate Report", command=generate_report, bg="red")
message_label = tk.Label(root, text="", fg="black")

# Treeview widget to display data in a table
style = ttk.Style()
style.configure("Treeview.Heading", font=custom_font)
student_table = ttk.Treeview(root, columns=("ID", "Name", "Student ID", "Department", "Course"), show="headings", style="Treeview.Heading")
student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Student ID", text="Student ID")
student_table.heading("Department", text="Department")
student_table.heading("Course", text="Course")

# Place labels, entry widgets, and buttons on the grid
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
student_id_label.grid(row=2, column=0)
student_id_entry.grid(row=2, column=1)
department_label.grid(row=3, column=0)
department_entry.grid(row=3, column=1)
course_label.grid(row=4, column=0)
course_entry.grid(row=4, column=1)
register_button.grid(row=5, column=0, columnspan=2)
view_button.grid(row=5, column=1, columnspan=2)
delete_button.grid(row=5, column=2, columnspan=2)
edit_button.grid(row=6, column=0, columnspan=2)
generate_report_button.grid(row=6, column=1, columnspan=2)
message_label.grid(row=10, column=0, columnspan=2)
student_table.grid(row=0, column=0, columnspan=2)

# "Log Out" button
log_out_button = tk.Button(root, text="Log Out", command=log_out, font=custom_font, bg="red")
log_out_button.grid(row=11, column=0, columnspan=2)

#  the database connection and create the student table
conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()
create_student_table(cursor)

# the initial student data
view_students()
root.mainloop()
conn.close()
