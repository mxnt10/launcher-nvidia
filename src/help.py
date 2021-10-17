#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import logging as log
import requests as rq
import tkinter as tk

# import source
import messagebox as msgbox
import translate as t
import utils as ut
import version as v


# Check Updates Function
def check_for_updates(win):
    log.info("\033[33mChecking updates...\033[m")
    try:
        res = rq.get('https://raw.githubusercontent.com/mxnt10/launcher-nvidia/master/RELEASE')
        if res.status_code != 200:
            raise ValueError('Connection fail, ' + str(res.status_code))

        new_ver = res.text.split("\n")
        if new_ver[0] == str(v.__version__):
            log.info("\033[32m Program already updated.\033[m")
            msgbox.showinfo(win, t.UPDATED, t.UP_ALREADY)
        else:
            log.warning("\033[32m Update available\033[31m %s \033[m", str(new_ver[0]))
            msgbox.showwarn(win, t.IMPORTANT, t.UP_AVALIABLE + ': ' + str(new_ver[0]) + '!')

    except ValueError as msg:
        log.error("\033[33m Update check failed.\033[31m %s \033[m", msg)
        msgbox.showerror(win, t.ERROR, t.UP_FAIL)


# Function About
def about(win):
    # No necessary minimize window
    # noinspection PyUnusedLocal
    def on_unmap(*args):
        help_app.deiconify()
        help_app.focus_force()

    # Config Interface
    help_app = tk.Toplevel()
    help_app.minsize(400, 220)
    help_app.wait_visibility(help_app)
    help_app.attributes('-alpha', 0.0)
    ut.center(help_app)
    help_app.title(t.ABOUT + ' Launcher Nvidia')
    help_app.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    help_app.transient(win)
    help_app.focus_force()
    help_app.grab_set()

    # Text Info
    tk.Label(help_app, text='Launcher NVIDIA', font=12).place(x=10, y=10)
    tk.Label(help_app, text=t.VERSION + ' ' + str(v.__version__)).place(x=150, y=14)
    tk.Label(help_app, text=t.HELP_TXT1).place(x=10, y=50)
    tk.Label(help_app, text=t.HELP_TXT2).place(x=10, y=68)
    tk.Label(help_app, text=t.HELP_TXT3).place(x=10, y=86)
    tk.Label(help_app, text=t.MAINTAINER + ': Mauricio Ferrari').place(x=10, y=130)
    tk.Label(help_app, text=t.CONTACT + ': m10ferrari1200@gmail.com').place(x=10, y=150)

    # Button Close
    closebutton = tk.Button(help_app, text=t.CLOSE, command=lambda: ut.close_win(help_app))
    closebutton.place(relx=0.58, rely=0.82, width=160, height=30)

    # Open Interface
    log.info("\033[36m About open successful.\033[m")
    help_app.attributes('-alpha', 1.0)
    help_app.protocol("WM_DELETE_WINDOW", lambda: ut.close_win(help_app))
    help_app.bind("<Unmap>", on_unmap)  # For not minimize about window
    help_app.mainloop()
