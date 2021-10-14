#!/usr/bin/python3
# -*- coding: utf-8 -*-

# splash
# root.overrideredirect(1)

# Import modules
import importlib as imp
import logging as log
import tkinter as tk

# Import internal modules
import pystray
from pystray import MenuItem as Men
from PIL import Image

# Import sources
import help as hl
import management as mg
import options as op
import settings as st
import translate as t
import utils as ut


# Exit Program
def stop_app(win):
    ut.close_win(win)
    if st.set_json('SysTray') == 'False':
        # noinspection PyBroadException
        try:
            stop_icon()
        except Exception:
            pass


# Restart applications for apply settings
def restart_program(win):
    stop_app(win)
    imp.reload(t)  # Necessary for aply translation in restart program
    launcher_nvidia()


# Main interface
def launcher_nvidia():
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
    menu_program.add_command(label=t.ADD_DESK, command=lambda: mg.add_desktop(listbox))
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
    addbutton = tk.Button(button_frame, text=t.ADD, command=lambda: mg.add_desktop(listbox))
    addbutton.place(x=0, y=5, width=200, height=30)

    # Remove button
    rembutton = tk.Button(button_frame, text=t.REMOVE, command=lambda: mg.remove(listbox))
    rembutton.place(x=210, y=5, width=200, height=30)

    # Open interface
    print("\033[36mWelcome! Interface open successful.\033[m")
    mg.create_nvidia_categories()
    main_app.config(menu=menu_bar)
    main_app.attributes('-alpha', 1.0)
    main_app.protocol("WM_DELETE_WINDOW", lambda: stop_app(main_app))
    main_app.mainloop()


# Stop icon for quit application.
def stop_icon():
    print("\033[30;42mQuit application!\033[m")
    icon.stop()


# Open main interface
if __name__ == '__main__':
    print("\033[30;42mStart application!\033[m")
    st.check_json()
    launcher_nvidia()

    # Icon support
    control = st.set_json('SysTray')
    if control == 'True':
        i_tray = ut.set_icon()
        if i_tray is not None:
            image = Image.open(i_tray)
            menu = (Men(t.OPEN, launcher_nvidia), Men(t.QUIT, stop_icon))
            icon = pystray.Icon('Launcher Nvidia', image, 'Launcher Nvidia', menu)
            print("\033[30;42mStart icon!\033[m")
            # Open or close application using icon in systray.
            icon.run()
        else:
            log.warning("\033[33mIgnore start systray, icon not found.\033[m")
