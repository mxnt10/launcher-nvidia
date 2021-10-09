#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging as log
import subprocess as sh
import shutil as st
import os

from tkinter import messagebox
from tkinter import END, ANCHOR
from tkinter.filedialog import askopenfilename

import utils as ut

l_folder = os.path.expanduser('~/.local/share/applications')


# Start menu update

def update_start_menu():
    print("\033[36mUpdate desktop files in start menu.\033[m")
    desk_file_update = '/usr/share/l-nvidia/tools/desktop_file_update'
    l_desk_file_update = '../tools/desktop_file_update'

    try:
        with open(desk_file_update, 'r'):
            sh.call(desk_file_update, shell=True)
    except Exception as msg:
        log.warning("\033[33m%s.\033[32m Use a local file...\033[m", msg)
        sh.call(l_desk_file_update, shell=True)


# Create Nvidia categories in start menu

def create_nvidia_categories():
    print("\033[36mVerify if categories Nvidea as created.\033[m")
    nvidia_menu = '/usr/share/l-nvidia/tools/nvidia_menu'
    l_nvidia_menu = '../tools/nvidia_menu'

    try:
        with open(nvidia_menu, 'r'):
            sh.call(nvidia_menu, shell=True)
    except Exception as msg:
        log.warning("\033[33m%s.\033[32m Use a local file...\033[m", msg)
        sh.call(l_nvidia_menu, shell=True)
    update_start_menu()  # Update necessary


# Search name in the program of desktop file and replace occurrences if necessary.

def search_replace(file, replace):
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            if "Name=" in line:
                # Return case "Name=" word as found
                return line.replace("Name=", replace).strip('\n')
    return None


# Search desktop files optimized to run with Nvidia driver

def populate_list(lst):
    # Mapping desktop files in folder
    for root, subdir, files in os.walk(l_folder):
        for file in files:
            local = os.path.join(os.path.realpath(root), file)
            if ut.search_word(local, 'LIBGL_ALWAYS_SOFTWARE=1'):
                print("\033[32mFound: \033[33m" + local + "\033[m")
                lst.insert(END, search_replace(local, ""))


# Optimizations for desktop files

def create_nvidia(file, new):
    # Read file and write in other temporary file
    with open(file, 'r') as inp, open(new, 'w') as out:
        for line in inp:
            if "Exec=" in line:
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
                if "<Include>" in line:
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
        text = "Name=" + lst.get(ANCHOR) + "\n"
        command = extract_command(text)
        if not command:
            raise ValueError("Command not selected!")
        print("\033[32mExecutando: \033[36m" + command + "\033[m")
        sh.call(command, shell=True)
    except ValueError as msg:
        log.warning("\033[33m %s \033[m", msg)


# Function for add button

def add_desktop(lst):
    desktop_file = askopenfilename(title='Open a desktop file',
                                   initialdir='/usr/share/applications',
                                   filetypes=(('Desktop files', "*.desktop"),))
    try:
        if not desktop_file:
            raise ValueError("File not selected!")
        print("\033[32mFound: \033[33m" + desktop_file + "\033[m")
        new_file = os.path.join(l_folder, os.path.basename(desktop_file))
        if not os.path.isfile(new_file):
            create_nvidia(desktop_file, new_file)
            print("\033[32mMove: \033[33m" + new_file + "\033[m")
            lst.insert(END, search_replace(desktop_file, ""))
            start_menu(os.path.basename(desktop_file), 'add')
            update_start_menu()
        else:
            print("\033[31mThe program is already on the list!\033[m")
            messagebox.showinfo(title="Info", message="The program is already on the list!")
    except ValueError as msg:
        log.warning("\033[33m %s \033[32m", msg)


# Function for remove button

def remove(lst):
    text = "Name=" + lst.get(ANCHOR) + "\n"
    for root, subdir, files in os.walk(l_folder):
        for file in files:
            local = os.path.join(os.path.realpath(root), file)
            if ut.search_word(local, text):
                os.remove(local)
                print("\033[31mRemove: \033[34m" + local + "\033[m")
                lst.delete(ANCHOR)
                start_menu(os.path.basename(local), 'rm')
                update_start_menu()
