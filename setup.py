from cx_Freeze import setup, Executable
import os

build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["assets"]
}

executables = [
    Executable("main.py")
]

setup(
    name="Fuga Espacial",
    version="1.0",
    description="Fuga Espacial app",
    options={"build_exe": build_exe_options},
    executables=executables
)

#