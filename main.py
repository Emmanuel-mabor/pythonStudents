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

        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)

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
register_button = tk.Button(root, text="Register", command=register_student)
view_button = tk.Button(root, text="View Students", command=view_students)
delete_button = tk.Button(root, text="Delete Student", command=delete_student)
edit_button = tk.Button(root, text="Edit Student", command=edit_student)
generate_report_button = tk.Button(root, text="Generate Report", command=generate_report)
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
view_button.grid(row=6, column=0, columnspan=2)
delete_button.grid(row=7, column=0, columnspan=2)
edit_button.grid(row=8, column=0, columnspan=2)
generate_report_button.grid(row=9, column=0, columnspan=2)
message_label.grid(row=10, column=0, columnspan=2)
student_table.grid(row=0, column=0, columnspan=2)

# "Log Out" button
log_out_button = tk.Button(root, text="Log Out", command=log_out, font=custom_font)
log_out_button.grid(row=11, column=0, columnspan=2)

#  the database connection and create the student table
conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()
create_student_table(cursor)

# the initial student data
view_students()
root.mainloop()
conn.close()
