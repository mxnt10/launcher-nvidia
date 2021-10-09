#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging as log
import requests

import tkinter as tk
from tkinter import messagebox

import utils


# Check Updates Function

def check_for_updates():
    print("\033[33mChecking updates...\033[m")
    try:
        res = requests.get("https://raw.githubusercontent.com/mxnt10/launcher-nvidia/master/RELEASE")

        if res.status_code != 200:
            raise ValueError('Connection fail, ' + str(res.status_code))

        new_ver = res.text.split("\n")
        cur_ver = "1.2"

        if new_ver[0] == cur_ver:
            print("\033[32mProgram already updated.\033[m")
            messagebox.showinfo(title="Updated", message="Program already updated!")
        else:
            print("\033[32mUpdate available: \033[31m" + str(new_ver[0]) + "\033[m")
            messagebox.showwarning(title="Important", message="Update avaliable: " + str(new_ver[0]) + "!")

    except ValueError as msg:
        log.error("\033[33mUpdate check failed. \033[31m%s \033[m", msg)
        messagebox.showerror(title="Error", message="Update check failed!")


# Function About

def about(main):

    # Config Interface
    help_app = tk.Toplevel()
    help_app.wait_visibility(help_app)
    help_app.attributes('-alpha', 0.0)
    help_app.minsize(400, 200)
    utils.center(help_app)
    help_app.title("Launcher NVIDIA - About")
    help_app.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    help_app.transient(main)
    help_app.focus_force()
    help_app.grab_set()

    # Text Info
    tk.Label(help_app, text="Launcher NVIDIA", font=12).place(x=10, y=10)
    tk.Label(help_app, text="Version 1.2").place(x=150, y=14)
    tk.Label(help_app, text="Utility created to facilitate running programs and games on").place(x=10, y=50)
    tk.Label(help_app, text="linux distributions such as Slackware.").place(x=10, y=65)
    tk.Label(help_app, text="Maintainer: Mauricio Ferrari").place(x=10, y=100)
    tk.Label(help_app, text="Contact: m10ferrari1200@gmail.com").place(x=10, y=120)

    # Button Close
    closebutton = tk.Button(help_app, text="Close", command=lambda: utils.close_win(help_app))
    closebutton.place(relx=0.58, rely=0.8, width=160, height=30)

    # Open Interface
    print("\033[36mAbout open successful.\033[m")
    help_app.attributes('-alpha', 1.0)
    help_app.mainloop()
