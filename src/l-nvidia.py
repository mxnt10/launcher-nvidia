#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import importlib as imp

# Define attributes for logging
import logging as log
log.basicConfig(level=log.INFO)
log.root.name = ''

# Import tkinter modules
import tkinter as tk
from tkinter import font

# Import tray modules
from pystray import Icon, MenuItem
from PIL import Image, ImageTk

# Import sources
import help as hl
import management as mg
import options as op
import settings as st
import translate as t
import utils as ut
import version as v

# Variables
tray_st = False


# Exit Program
def stop_app(win):
    ut.close_win(win)
    if st.set_json('SysTray') == 'False':
        stop_icon()


# Restart applications for apply settings
def restart_program(win):
    print("\033[30;42m Restart application! \033[m")
    ut.close_win(win)
    imp.reload(t)  # Necessary for aply translation in restart program
    launcher_nvidia(False)


# Splash for application
def splash_show():
    # Config splash interface
    splash_app = tk.Tk()
    splash_app.geometry('570x270')
    splash_app.overrideredirect(True)
    splash_app.config(bg='#4b984f')
    ut.center(splash_app)

    # Responsive frame for programs
    label_frame = tk.Frame(splash_app)
    label_frame.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)

    # View logo in splash
    img = ImageTk.PhotoImage(Image.open(ut.set_icon()))
    logo = tk.Label(label_frame, image=img)
    logo.grid(row=0, column=0)

    # Label for logo in splash
    font_size = font.Font(size=26)
    label = tk.Label(label_frame, text='Launcher NVIDIA    \nv' + str(v.__version__) + '\t\t', font=font_size)
    label.grid(row=0, column=1)

    # Time for view splash, open splash
    splash_app.after(1500, lambda: launcher_nvidia(splash_app))
    splash_app.mainloop()


# Main interface
def launcher_nvidia(win):
    # Necessary for close splash
    if win:
        win.destroy()

    # Config interface
    main_app = tk.Tk()
    main_app.minsize(600, 400)
    main_app.wait_visibility(main_app)
    main_app.attributes('-alpha', 0.0)
    ut.center(main_app)
    main_app.title('Launcher NVIDIA')

    # Set program icon case function is not None
    ico = ut.set_icon()
    if ico is not None:
        main_app.iconphoto(True, tk.PhotoImage(file=ico))

    # Menubar
    menu_bar = tk.Menu(main_app)

    # General menu
    menu_program = tk.Menu(menu_bar, tearoff=0)
    menu_program.add_command(label=t.ADD_DESK, command=lambda: mg.add_desktop(main_app, listbox))
    menu_program.add_command(label=t.UP_LIST, command=lambda: op.update_list(listbox))
    menu_program.add_command(label=t.EXIT, command=lambda: stop_app(main_app))
    menu_bar.add_cascade(label=t.GENERAL, menu=menu_program)

    # Options menu
    menu_options = tk.Menu(menu_bar, tearoff=0)
    menu_options.add_command(label=t.RST_PROGRAM, command=lambda: restart_program(main_app))
    menu_options.add_command(label=t.PREF, command=lambda: op.preferencies(main_app))
    menu_bar.add_cascade(label=t.OPTIONS, menu=menu_options)

    # Help menu
    menu_help = tk.Menu(menu_bar, tearoff=0)
    menu_help.add_command(label=t.CHECK_UP, command=lambda: hl.check_for_updates(main_app))
    menu_help.add_command(label=t.ABOUT, command=lambda: hl.about(main_app))
    menu_bar.add_cascade(label=t.HELP, menu=menu_help)

    # Responsive frame for programs
    label_frame = tk.LabelFrame(main_app, text=t.SOFTWARES, bd=2, relief="groove")
    label_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.8)

    # Responsive frame for buttons
    button_frame = tk.Frame(main_app)
    button_frame.place(relx=0.01, rely=0.83, relwidth=0.98, relheight=0.15)

    # Listbox for list programs
    listbox = tk.Listbox(label_frame)
    listbox.place(relx=0.01, rely=0.01, relwidth=0.7, relheight=0.96)
    listbox.config(font='-weight bold -size 10')
    mg.populate_list(listbox)

    # Label select
    label_text = tk.Label(main_app, text=t.LAST_RUN)
    label_text.place(relx=0.72, y=100)
    label_select = tk.Label(main_app)
    label_select.place(relx=0.72, y=120)

    # Run button
    addbutton = tk.Button(label_frame, text=t.LAUNCH, command=lambda: mg.launch(label_select, listbox))
    addbutton.place(relx=0.72, rely=0.01, width=150, height=30)

    # Add button
    addbutton = tk.Button(button_frame, text=t.ADD, command=lambda: mg.add_desktop(main_app, listbox))
    addbutton.place(x=0, y=5, width=200, height=30)

    # Remove button
    rembutton = tk.Button(button_frame, text=t.REMOVE, command=lambda: mg.remove(listbox))
    rembutton.place(x=210, y=5, width=200, height=30)

    # Open interface
    log.info("\033[36m Welcome! Interface open successful.\033[m")
    mg.create_nvidia_categories()
    main_app.config(menu=menu_bar)
    main_app.attributes('-alpha', 1.0)
    main_app.protocol("WM_DELETE_WINDOW", lambda: stop_app(main_app))
    main_app.mainloop()


# Stop icon for quit application.
def stop_icon():
    print("\033[30;42m Quit application! \033[m")
    if tray_st:
        icon.stop()


# Open main interface
if __name__ == '__main__':
    print("\033[30;42m Start application! \033[m")
    # For splash screen support
    splash = st.set_json('Splash')
    if splash == 'True':
        splash_show()
    else:
        launcher_nvidia(False)
    # Icon support
    tray = st.set_json('SysTray')
    if tray == 'True':
        i_tray = ut.set_icon()
        if i_tray is not None:
            image = Image.open(i_tray)
            menu = (MenuItem(t.OPEN, lambda: launcher_nvidia(False)), MenuItem(t.QUIT, stop_icon))
            icon = Icon('Launcher Nvidia', image, 'Launcher Nvidia', menu)
            print("\033[30;42m Start icon! \033[m")
            # Open or close application using icon in systray.
            tray_st = True
            icon.run()
        else:
            log.warning("\033[33m Ignore start systray, icon not found.\033[m")
