# Commands for admin to open meatspin
# Author BlackWidow
# This will be a module at some point
# Website: Intgamer.net or sinfulandroid.net

import webbrowser
import MySQLdb
meatspin = "/meatspin"


def meatspin():
        meatspin = raw_input("To meat spin users do /meatspin: ")
        if(meatspin):
            webbrowser.open("meatspin.cc")
            print("You just got rick rolled by an admin!")
meatspin()


