import cx_Freeze,tkinter,checklistcombobox,numpy,pandas,PIL,os

cx_Freeze.setup(
    name = "RPS-3",
    options = {"build_exe": {"packages":["tkinter","matplotlib","pandas","numpy","PIL","os"], "include_files":[f"./src/{path}.png" for path in ["rock","paper","scissors","glue","pen"]]+["./src/checklistcombobox.py"]}},
    version = "0.1",
    description = "RPS-3 Simulator",
    executables = [cx_Freeze.Executable("./src/RPS.py", base="Win32GUI")]
    )
