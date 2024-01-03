import tkinter as tk
from tkinter import messagebox

#changes
# Create the main window (it won't be visible)
root = tk.Tk()
root.withdraw()

# Display a pop-up message box
messagebox.showinfo("Success", "This code runs successfully")

# This line is optional but keeps the window from appearing
root.destroy()
