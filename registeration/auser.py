#Registration Script
#Author BlackWidow aka Zachary

import time
import MySQLdb
import os

yes = 1
no = 1


def addusermen():
    global name
    nigcon = MySQLdb.connect("localhost", "root", "", "igtest")
    if (nigcon):
        print "Successfully Connected to Database"
        cursor = nigcon.cursor()
    else:
        print "There was a error while trying to connect to the Database"

    time.sleep(1)
    print ""
    print "Signing up is easy & Free!"
    print ""
    time.sleep(1)
    print "Please input your desired credits"
    print ""
    time.sleep(1)
    username = raw_input("username: ")
    print(username)
    print("Are you sure you want this username")
    print ""
    raw_input("Yes or No: ")
    if yes:
        print "We need to register a password"
        os.system('cls')
    password = raw_input("Password: ")
    print "Re-type your password: "
    password1 = raw_input('Password: ')
    if password1 == password:
        print "Passwords Match"

    if password1 != password:
        print "Password do not match up"
        print ""
    print(password)
    print ""
    print ("Registration Complete")
    # add_user = ("INSERT INTO `user_pwd`(`NAME`, `PASS`) VALUES ('" + username + "')")
    add_user = ("INSERT INTO `user_pwd`(`NAME`, `PASS`) VALUES('" + username + "', '" + password + "')")
    # VALUES('" + $username + "', '" + $password + "')"
    # add_pass = ("INSERT INTO `user_pwd`(`PASS`) VALUES ('" + password + "')")
    assert isinstance(cursor.execute, object)
    cursor.execute(add_user)
addusermen()
