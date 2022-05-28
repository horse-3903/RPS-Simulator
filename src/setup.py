import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("./src/rps-3_app.py", base=base)]

cx_Freeze.setup(
    name = "RPS-3",
    options = {"build_exe": {"packages":["tkinter","matplotlib","pandas","numpy","PIL"], "include_files":[f"./src/images/{path}.png" for path in ["rock","paper","scissors","glue","pen"]]}},
    version = "0.1",
    description = "RPS-3 Simulator",
    executables = executables
    )
