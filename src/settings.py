#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import json as js
import logging as log
import os

j_file = "settings.json"

default_js = {
    "Language": "Default",
    "SysTray": "False"
}


# Check if exist settings.json, else file as create
def check_json():
    try:
        with open(j_file):
            pass
    except Exception as msg:
        log.warning("\033[33m %s. \033[32mCreate a settings.json ...", msg)
        with open(j_file, 'w') as jf:
            js.dump(default_js, jf, indent=2)


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
