import tkinter as tk
from tkinter import messagebox

class StudentPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Portal")
        self.root.geometry("600x400")  # Increased width

        # Create a table to organize the navigation bar
        self.nav_table = tk.Frame(self.root)
        self.nav_table.pack(fill=tk.X)

        # Create the navigation bar labels
        self.home_button = tk.Label(self.nav_table, text="HOME", padx=20)
        self.information_button = tk.Label(self.nav_table, text="INFORMATION UPDATE", padx=20)
        self.fees_button = tk.Label(self.nav_table, text="FEES", padx=20)
        self.timetables_button = tk.Label(self.nav_table, text="TIMETABLES", padx=20)
        self.course_registration_button = tk.Label(self.nav_table, text="COURSE REGISTRATION", padx=20)
        self.results_button = tk.Label(self.nav_table, text="RESULTS", padx=20)
        self.my_requests_button = tk.Label(self.nav_table, text="MY REQUESTS", padx=20)
        self.sign_out_button = tk.Label(self.nav_table, text="SIGN OUT", padx=20)

        # Add the labels to the navigation bar
        self.home_button.grid(row=0, column=0)
        self.information_button.grid(row=0, column=1)
        self.fees_button.grid(row=0, column=2)
        self.timetables_button.grid(row=0, column=3)
        self.course_registration_button.grid(row=1, column=0)
        self.results_button.grid(row=1, column=1)
        self.my_requests_button.grid(row=1, column=2)
        self.sign_out_button.grid(row=1, column=3)

        # Create a login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        # Create login form
        self.login_label = tk.Label(self.login_frame, text="Students Login")
        self.login_label.pack()

        self.login_student_id_label = tk.Label(self.login_frame, text="Student ID / Reg. Number:")
        self.login_student_id_label.pack()
        self.login_student_id_entry = tk.Entry(self.login_frame)
        self.login_student_id_entry.pack()

        self.login_password_label = tk.Label(self.login_frame, text="Password:")
        self.login_password_label.pack()
        self.login_password_entry = tk.Entry(self.login_frame, show="*")  # Hide the password
        self.login_password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        # Create Applicants / New Students section
        self.applicants_frame = tk.Frame(self.root)
        self.applicants_frame.pack()

        self.applicants_label = tk.Label(self.applicants_frame, text="Applicants / New Students")
        self.applicants_label.pack()

        self.application_ref_label = tk.Label(self.applicants_frame, text="Application Ref. No:")
        self.application_ref_label.pack()
        self.application_ref_entry = tk.Entry(self.applicants_frame)
        self.application_ref_entry.pack()

        self.index_no_label = tk.Label(self.applicants_frame, text="Index No / Exam Year:")
        self.index_no_label.pack()
        self.index_no_entry = tk.Entry(self.applicants_frame)
        self.index_no_entry.pack()

        self.applicants_note_label = tk.Label(self.applicants_frame,
                                              text="The year of registration must be in full eg 01234567001/2015")
        self.applicants_note_label.pack()

        # Create copyright information
        self.copyright_frame = tk.Frame(self.root)
        self.copyright_frame.pack()

        self.copyright_label = tk.Label(self.copyright_frame,
                                        text="© 2023 Mount Kenya University . Hosted by Fountain ICT Services")
        self.copyright_label.pack()

        self.registered_students = {"12345": "password123"}  # Store registered students here (example)

    def login(self):
        student_id = self.login_student_id_entry.get()
        password = self.login_password_entry.get()

        if student_id in self.registered_students and self.registered_students[student_id] == password:
            messagebox.showinfo("Login Successful", "Login successful.")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Login failed. Please check your credentials.")

    def show_main_menu(self):
        # Implement the main menu GUI here
        pass

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    portal = StudentPortal(root)
    portal.start()
