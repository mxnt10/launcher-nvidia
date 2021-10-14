#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import thinter modules
import tkinter as tk
from tkinter import END, ttk

# Import sources
import management as mg
import settings as st
import translate as t
import utils as ut


# Option for update list
def update_list(lst):
    lst.delete(0, END)
    mg.populate_list(lst)


# View preferencies for program configurations
def preferencies(main):
    # No necessary minimize window
    # noinspection PyUnusedLocal
    def on_unmap(*args):
        pref_app.deiconify()
        pref_app.focus_force()

    # Method for pass argument for define_language
    # noinspection PyUnusedLocal
    def event(*args):
        t.define_language(combo_lang.get())

    # Set variables
    set_tray = tk.IntVar()
    set_lang = [t.DEFAULT, t.PORTUGUESE]
    set_theme = [t.DEFAULT]

    if st.set_json('SysTray') == 'True':
        set_tray.set(1)

    # Config Interface
    pref_app = tk.Toplevel()
    pref_app.minsize(400, 600)
    pref_app.wait_visibility(pref_app)
    pref_app.attributes('-alpha', 0.0)
    ut.center(pref_app)
    pref_app.title(t.PREF)
    pref_app.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    pref_app.transient(main)
    pref_app.focus_force()
    pref_app.grab_set()

    # Options for language
    label_lang = tk.Label(pref_app, text=t.LANGUAGE)
    label_lang.place(x=10, y=20)
    combo_lang = ttk.Combobox(pref_app, values=set_lang)
    combo_lang.current(0)
    combo_lang.bind("<<ComboboxSelected>>", event)
    combo_lang.place(x=100, y=20)

    # select language
    lang = st.set_json('Language')
    if lang == 'Default':
        combo_lang.set(t.DEFAULT)
    if lang == 'Portuguese':
        combo_lang.set(t.PORTUGUESE)

    # Label for themes
    label_theme = tk.Label(pref_app, text=t.THEME)
    label_theme.place(x=10, y=60)
    combo_theme = ttk.Combobox(pref_app, values=set_theme)
    combo_theme.set(t.DEFAULT)
    combo_theme.place(x=100, y=60)

    # Checkbutton for tray icon
    check_tray = tk.Checkbutton(pref_app, text=t.SYSTRAY_TXT, variable=set_tray,
                                onvalue=1, offvalue=0, command=lambda: st.enable_tray(set_tray))
    check_tray.place(x=10, y=120)

    # Button Close
    closebutton = tk.Button(pref_app, text=t.CLOSE, command=lambda: ut.close_win(pref_app))
    closebutton.place(relx=0.58, rely=0.94, width=160, height=30)

    # Open Interface
    print("\033[36mPreferencies open successful.\033[m")
    pref_app.attributes('-alpha', 1.0)
    pref_app.protocol("WM_DELETE_WINDOW", lambda: ut.close_win(pref_app))
    pref_app.bind("<Unmap>", on_unmap)  # For not minimize configuration window
    pref_app.mainloop()
