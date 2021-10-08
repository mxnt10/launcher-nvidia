#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import logging as log


# Search word in text file.

def search_word(file, txt):
    with open(file, 'r', encoding='utf8') as a:
        for line in a:
            if txt in line:
                # Return True case "txt" word as found
                return True
    return False


# Close interface

def close_win(win):
    # :param win: the main window or Toplevel window to close
    print("\033[34mClosing interface!\033[m")
    win.destroy()


# Define application icon

def set_icon(win):
    # :param win: the main window or Toplevel window to define icon

    icon = "/usr/share/pixmaps/l-nvidia.png"
    l_icon = "../images/l-nvidia.png"

    try:
        with open(icon, 'r'):
            win.iconphoto(True, tk.PhotoImage(file=icon))
    except Exception as msg:
        log.warning("\033[33m%s.\033[32m Use a local icon...\033[m", msg)
        try:
            win.iconphoto(True, tk.PhotoImage(file=l_icon))
        except Exception as msg:
            # Exception for icon not found
            log.warning("\033[31m%s\033[m", msg)


# Open application in screen center

def center(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()
