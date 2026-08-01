from tkinter.messagebox import showerror

def displayError(e: Exception):
    showerror(title="Critical Failure", message="The game has unexpectedly crashed. reason can be found below:\n\n" + str(e))
    quit(-1)