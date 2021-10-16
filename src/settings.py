#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import json as js
import logging as log
import os

j_folder = os.path.expanduser('~/.config/l-nvidia')
j_file = j_folder + '/settings.json'

default_js = {
    "Language": "Default",
    "SysTray": "False",
    "Splash": "False"
}

# Check if exist settings.json, else file as create
try:
    with open(j_file):
        pass
except Exception as msg:
    log.warning("\033[33m %s. \033[32mCreate a settings.json ...", msg)
    if not os.path.isdir(j_folder):
        os.makedirs(j_folder)
    with open(j_file, 'w') as jfile:
        js.dump(default_js, jfile, indent=2)


# Set value of the json file
def set_json(op):
    with open(j_file) as jf:
        objJson = js.load(jf)
    return objJson[op]


# Write value of the json file
def write_json(op, val):
    with open(j_file, 'r') as jf:
        objJson = js.load(jf)
        objJson[op] = val

    # Replace original file
    os.remove(j_file)
    with open(j_file, 'w') as jf:
        js.dump(objJson, jf, indent=2)


# Enable or disable systray options
def enable_tray(var):
    if var.get() == 1:
        write_json('SysTray', 'True')
    else:
        write_json('SysTray', 'False')


# Enable or disable splash options
def enable_splash(var):
    if var.get() == 1:
        write_json('Splash', 'True')
    else:
        write_json('Splash', 'False')
