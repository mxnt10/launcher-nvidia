#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import tkinter as tk

# Import source
import utils as ut


# Function for view message
def message(win, title, img, txt):
    # No necessary minimize window
    # noinspection PyUnusedLocal
    def on_unmap(*args):
        msg.deiconify()
        msg.focus_force()

    msg = tk.Toplevel()
    msg.wait_visibility(msg)
    msg.attributes('-alpha', 0.0)
    msg.title(title)
    msg.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    msg.transient(win)
    msg.focus_force()
    msg.grab_set()

    # Create frame for full organization
    frame = tk.Frame(msg)
    frame.pack()

    # Label logo
    logo = tk.Label(frame, image=img)
    logo.grid(row=0, column=0, pady=(10, 10), padx=(10, 10))

    # Insert text
    text = tk.Label(frame, text=txt)
    text.grid(row=0, column=1, pady=(10, 10), padx=(10, 20))

    # Create button
    button = tk.Button(msg, text="OK", command=msg.destroy, width=10)
    button.pack(pady=(0, 10))

    ut.center(msg)
    msg.attributes('-alpha', 1.0)
    msg.bind("<Unmap>", on_unmap)  # For not minimize message dialog
    msg.mainloop()

# Dialog for information
def showinfo(win, title, text):
    image = '::tk::icons::information'
    message(win, title, image, text)

# Dialog for warning
def showwarn(win, title, text):
    image = '::tk::icons::warning'
    message(win, title, image, text)

# Dialog for error
def showerror(win, title, text):
    image = '::tk::icons::error'
    message(win, title, image, text)
