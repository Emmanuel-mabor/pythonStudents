import sys
from cx_Freeze import setup, Executable

# Define the target script and the target directory
target_script = 'combined.py'
target_dir = 'dist'

executables = [Executable(target_script)]

setup(
    name="STUDENT MANAGEMENT SYSTEM",
    version="1.0",
    description="ITS A TRIAL SYSTEM",
    executables=executables,
    options={
        "build_exe": {
            "include_files": [],  # Add any additional files or data here
        }
    }
)
