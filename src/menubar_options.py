#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import management as mg
import utils as ut

from tkinter import END


# Option for update list

def update_list(lst):
    lst.delete(0, END)
    mg.populate_list(lst)


# View preferencies for program configurations

def preferencies(main):

    # Config Interface
    pref_app = tk.Toplevel()
    pref_app.wait_visibility(pref_app)
    pref_app.attributes('-alpha', 0.0)
    pref_app.minsize(400, 600)
    ut.center(pref_app)
    pref_app.title("Launcher NVIDIA - Preferencies")
    pref_app.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    pref_app.transient(main)
    pref_app.focus_force()
    pref_app.grab_set()

    # Button Close
    closebutton = tk.Button(pref_app, text="Close", command=lambda: ut.close_win(pref_app))
    closebutton.place(relx=0.58, rely=0.94, width=160, height=30)

    # Open Interface
    print("\033[36mPreferencies open successful.\033[m")
    pref_app.attributes('-alpha', 1.0)
    pref_app.mainloop()
