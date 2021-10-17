#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import module
import gettext
import logging as log

# Import source
import settings as st


# Write configurations for aplication language
def define_language(op):
    st.write_json('Language', lang_find[op])


# Set translate locale
def set_locale(op):
    local = '/usr/share/locale'
    l_local = '../locale'
    file = '/' + str(op) + '/LC_MESSAGES/l-nvidia.mo'
    try:
        ck = local + file
        with open(ck, 'r'):
            return local
    except Exception as msg:
        log.warning("\033[33m %s.\033[32m Use a local file...\033[m", msg)
        try:
            ck = l_local + file
            with open(ck, 'r'):
                return l_local
        except Exception as msg:
            # Exception for file not found
            log.error("\033[31m %s \033[m", msg)
            return None


# Define application language
lang_abv = {
    "Default": None,
    "Portuguese": "pt_BR"
}

abv = lang_abv[st.set_json('Language')]
if abv is not None:
    locale = set_locale(abv)
    if locale is not None:
        gettext = gettext.translation('l-nvidia', localedir=locale, languages=[abv])
        gettext.install()

# Tranlate all variables
_ = gettext.gettext

# General
OPEN = _('Open')
QUIT = _('Quit')
PREF = _('Preferences')
ABOUT = _('About')

# Buttons
ADD = _('Add')
REMOVE = _('Remove')
LAUNCH = _('Launch')
CLOSE = _('Close')

# Text for MenuBar
ADD_DESK = _('Add from Desktop File')
UP_LIST = _('Update List')
EXIT = _('Exit')
GENERAL = _('General')
RST_PROGRAM = _('Restart Program')
OPTIONS = _('Options')
CHECK_UP = _('Check for Updates')
HELP = _('Help')

# Text for Main Interface
SOFTWARES = _('Softwares')
LAST_RUN = _('Last run:')

# Text for Management
ASK_OPEN = _('Open a desktop file')
DESK_FILE = _('Desktop Files')
INFO = _('Info')
MSG_INFO = _('The program is already on the list!')

# Text for Preferencies
LANGUAGE = _('Language:')
THEME = _('Theme:')
SYSTRAY_TXT = _('Close program to system tray.')
SPLASH_TXT = _('Enable splash screen.')
DEFAULT = _('Default')
PORTUGUESE = _('Portuguese')

# Text for Updates
UPDATED = _('Updated')
IMPORTANT = _('Important')
ERROR = _('Error')
UP_ALREADY = _('Program already updated!')
UP_AVALIABLE = _('Update avaliable')
UP_FAIL = _('Update check failed!')

# Text for help files
VERSION = _('Version')
HELP_TXT1 = _('Utility created to facilitate execution of programs and games on')
HELP_TXT2 = _('linux distributions such as Slackware in notebooks with')
HELP_TXT3 = _('Nvidia + Intel hybrid graphics card.')
MAINTAINER = _('Maintainer')
CONTACT = _('Contact')

# Define list for options languages
lang_find = {
    DEFAULT: "Default",
    PORTUGUESE: "Portuguese"
}
