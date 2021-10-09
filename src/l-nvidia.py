#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import management as mg
import menubar_help as hl
import menubar_options as op
import utils as ut

# Config Interface
main_app = tk.Tk()
main_app.minsize(600, 400)
main_app.wait_visibility(main_app)
main_app.attributes('-alpha', 0.0)
ut.center(main_app)
main_app.title("Launcher NVIDIA - By MXNT10")
ut.set_icon(main_app)

# Menubar
menu_bar = tk.Menu(main_app)

# General Menu
menu_program = tk.Menu(menu_bar, tearoff=0)
menu_program.add_command(label="Add from Desktop File", command=lambda: mg.add_desktop(listbox))
menu_program.add_command(label="Exit", command=lambda: ut.close_win(main_app))
menu_bar.add_cascade(label="General", menu=menu_program)

# Options menu
menu_options = tk.Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Update List", command=lambda: op.update_list(listbox))
# menu_options.add_command(label="Preferences", command=lambda: op.preferencies(main_app))
menu_bar.add_cascade(label="Options", menu=menu_options)

# Help menu
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="Check for Updates", command=hl.check_for_updates)
menu_help.add_command(label="About", command=lambda: hl.about(main_app))
menu_bar.add_cascade(label="Help", menu=menu_help)

# Responsive frame for Programs
label_frame = tk.LabelFrame(main_app, text="Softwares", bd=2, relief="groove")
label_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.8)

# Responsive frame for buttons
button_frame = tk.Frame(main_app)
button_frame.place(relx=0.01, rely=0.83, relwidth=0.98, relheight=0.15)

# Listbox for list programs
listbox = tk.Listbox(label_frame)
listbox.place(relx=0.01, rely=0.01, relwidth=0.7, relheight=0.96)
mg.populate_list(listbox)

# Label select
label_text = tk.Label(main_app, text="Last run:")
label_text.place(relx=0.72, y=100)
label_select = tk.Label(main_app)
label_select.place(relx=0.72, y=120)

# Run button
addbutton = tk.Button(label_frame, text="Launch", command=lambda: mg.launch(label_select, listbox))
addbutton.place(relx=0.72, rely=0.01, width=150, height=30)

# Add button
addbutton = tk.Button(button_frame, text="Add", command=lambda: mg.add_desktop(listbox))
addbutton.place(x=0, y=5, width=200, height=30)

# Remove button
rembutton = tk.Button(button_frame, text="Remove", command=lambda: mg.remove(listbox))
rembutton.place(x=210, y=5, width=200, height=30)

# Open interface
print("\033[36mWelcome! Interface open successful.\033[m")
mg.create_nvidia_categories()
main_app.config(menu=menu_bar)
main_app.attributes('-alpha', 1.0)
main_app.mainloop()
