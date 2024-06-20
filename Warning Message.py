import tkinter as tk
from tkinter import messagebox
import winsound

def show_warning():
    messagebox.showwarning("Warning", "Your system has been compromised.Please Call 555-555-5555 to resolve this")


root = tk.Tk()
root.withdraw()


for i in range(20):
    root.after(0, show_warning)


root.mainloop()


