import subprocess
import sys as system
from tkinter.messagebox import askyesno, showinfo, showerror

def dependencieInstaller():
    """
    Installs all needed dependencies for the game to run
    """
    
    answer = askyesno(title="Importing Packages", message="The Programm needs to install dependencies to run.\n"
                                                        + "Allow Python-Dependencies to be installed?")
    
    if answer:
        result = subprocess.run(
            [system.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "dependencies.txt"]
        )
    
    if result != 0:
        showerror(title="Something went wrong", message="we dont know what went wrong, but the installer failed. please try again or contact the dev")
        quit(int(result))
    else:
        showinfo(title="Success", message="Success! Please restart to programm to properly load everything")
        quit(0)
