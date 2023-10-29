from cx_Freeze import setup, Executable

executables = [Executable("your_main_script.py")]

options = {
    "build_exe": {
        "packages": ["tkinter", "sqlite3", "logging"],
        "include_files": ["student_database.db", "home.py"],
    }
}

setup(
    name="StudentRegistrationApp",
    version="1.0",
    description="Student Registration Application",
    executables=executables,
    options=options
)
