#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import logging as log
import subprocess as sh
import shutil as st
import os

# Import tkinter modules
from tkinter import END, ANCHOR
from tkinter.filedialog import askopenfilename

# Import source
import messagebox as msgbox
import translate as t
import utils as ut

l_folder = os.path.expanduser('~/.local/share/applications')

# Start menu update
def update_start_menu():
    log.info("\033[36m Update desktop files in start menu.\033[m")
    desk_file_update = '/usr/share/l-nvidia/utils/desktop_file_update'
    l_desk_file_update = '../utils/desktop_file_update'

    try:
        with open(desk_file_update, 'r'):
            sh.call(desk_file_update, shell=True)
    except Exception as msg:
        log.warning("\033[33m %s.\033[32m Use a local file...\033[m", msg)
        sh.call(l_desk_file_update, shell=True)


# Create Nvidia categories in start menu
def create_nvidia_categories():
    log.info("\033[36m Verify if categories Nvidea as created.\033[m")
    nvidia_menu = '/usr/share/l-nvidia/utils/nvidia_menu'
    l_nvidia_menu = '../utils/nvidia_menu'

    try:
        with open(nvidia_menu, 'r'):
            sh.call(nvidia_menu, shell=True)
    except Exception as msg:
        log.warning("\033[33m %s.\033[32m Use a local file...\033[m", msg)
        sh.call(l_nvidia_menu, shell=True)
    update_start_menu()  # Update necessary


# Search name in the program of desktop file and replace occurrences if necessary.
def search_replace(file, replace):
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            if not 'GenericName=' in line:
                if 'Name=' in line:
                    # Return case "Name=" word as found
                    return line.replace('Name=', replace).strip('\n')
    return None


# Search desktop files optimized to run with Nvidia driver
def populate_list(lst):
    sort_lst = []
    # Mapping desktop files in folder
    for root, subdir, files in os.walk(l_folder):
        for file in files:
            local = os.path.join(os.path.realpath(root), file)
            if ut.search_word(local, 'LIBGL_ALWAYS_SOFTWARE=1'):
                log.info("\033[32m Found \'\033[33m%s\033[32m\'.\033[m", local)
                sort_lst.append(search_replace(local, ""))
    for i in sorted(sort_lst):
        lst.insert(END, i)


# Optimizations for desktop files
def create_nvidia(file, new):
    # Read file and write in other temporary file
    with open(file, 'r') as inp, open(new, 'w') as out:
        for line in inp:
            if 'Exec=' in line:
                out.write(line.replace('Exec=', 'Exec=LIBGL_ALWAYS_SOFTWARE=1 '))
            else:
                out.write(line)


# Add and remove desktop file in Nvidia categories in start menu
def start_menu(file, option):
    l_menu = os.path.expanduser('~/.config/menus/applications-merged/nvidia.menu')
    tmp_file = os.path.expanduser('~/.config/menus/applications-merged/nvidia.menu.new')
    with open(l_menu, 'r') as inp, open(tmp_file, 'w') as out:

        if option == 'add':
            for line in inp:
                if '<Include>' in line:
                    out.write(line)
                    out.write('\t\t\t<Filename>' + file + '</Filename>\n')  # Incluse desktop file to list
                else:
                    out.write(line)

        if option == 'rm':
            for line in inp:
                # Omitting the line if the pattern is found.
                if not file in line:
                    out.write(line)

    st.move(tmp_file, l_menu)


# Needed to map the commands to be executed.
def extract_command(text):
    for root, subdir, files in os.walk(l_folder):
        for file in files:
            local = os.path.join(os.path.realpath(root), file)
            if ut.search_word(local, text):
                with open(local, 'r', encoding='utf8') as run:
                    for line in run:
                        if 'Exec=' in line:
                            start = line.replace('Exec=', '').split('\n')
                            return start[0]


# Execute program
def launch(lab, lst):
    try:
        lab.config(text=lst.get(ANCHOR))
        text = 'Name=' + lst.get(ANCHOR) + "\n"
        command = extract_command(text)
        if not command:
            raise Exception('Program not selected!')
        log.info("\033[32m Running\033[36m %s \033[m", command)
        sh.call(command + ' &', shell=True)
    except Exception as msg:
        log.info('\033[32m %s \033[m', msg)


# Function for add button
def add_desktop(win, lst):
    desktop_file = askopenfilename(title=t.ASK_OPEN, initialdir='/usr/share/applications',
                                   filetypes=((t.DESK_FILE, "*.desktop"),))

    try:
        if not desktop_file:
            raise ValueError("File not selected!")
        log.info("\033[32m Found \'\033[33m%s\033[32m\'.\033[m", desktop_file)
        new_file = os.path.join(l_folder, os.path.basename(desktop_file))

        if not os.path.isfile(new_file):
            create_nvidia(desktop_file, new_file)
            log.info("\033[32m Move \'\033[33m%s\033[32m\'.\033[m", new_file)
            lst.insert(END, search_replace(desktop_file, ''))
            start_menu(os.path.basename(desktop_file), 'add')
            update_start_menu()
        else:
            log.warning("\033[33m The program is already on the list!\033[m")
            msgbox.showinfo(win, t.INFO, t.MSG_INFO)

    except ValueError as msg:
        log.info('\033[32m %s \033[m', msg)


# Function for remove button
def remove(lst):
    try:
        if not lst.get(ANCHOR):
            raise ValueError("Program not selected!")
        text = 'Name=' + lst.get(ANCHOR) + "\n"

        for root, subdir, files in os.walk(l_folder):
            for file in files:
                local = os.path.join(os.path.realpath(root), file)
                if ut.search_word(local, text):
                    os.remove(local)
                    log.info("\033[31m Remove \'\033[33m%s\033[31m\'.\033[m", local)
                    lst.delete(ANCHOR)
                    start_menu(os.path.basename(local), 'rm')
                    update_start_menu()

    except ValueError as msg:
        log.info("\033[32m %s \033[m", msg)
