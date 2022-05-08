import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("./RPS-3/src/rps-3_app.py", base=base)]

cx_Freeze.setup(
    name = "RPS-3",
    options = {"build_exe": {"packages":["tkinter","matplotlib","pandas","numpy","PIL"], "include_files":["./RPS-3/src/rock.png","./RPS-3/src/paper.png","./RPS-3/src/scissors.png"]}},
    version = "0.1",
    description = "RPS-3 Simulator",
    executables = executables
    )