# Login Menu
# Author BlackWidow Aka Zachary
# intgamer.net or sinfulandroid.net
# Purpose Login Script for a Network Chat

import time
import MySQLdb
import socket

var1 = "Correct Login"
Yes = 1
no = 1
choice = 1
HOST = '127.0.0.1'
PORT = 50007
def loginmenu():
        print("Welcome to International Gamers Network Chat")
        print ""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        print ""
        print("Your local IP address is: ")
        print(s.getsockname()[0]) #print the ip address
        print ""
        s.close() # close the socket
        from urllib2 import urlopen
        my_ip = urlopen('http://ip.42.pl/raw').read()
        print("Your Public IP IS: ")
        print(my_ip)
        print ""
        time.sleep(1)
        # connect to the sql db
        nigcon = MySQLdb.connect("localhost", "root", "", "igtest")
        # creation of the cursor
        cursor = nigcon.cursor()
        print "Connected to Login Server"
        print ""
        print "Please input your information"
        time.sleep(1)
        username = raw_input("Username: ")
        # if( username == 'BlackWidow' ):
        password = raw_input("Password: ")
        if(cursor.execute("SELECT * FROM `user_pwd` WHERE `name` = '" + username + "' AND `pass` = '" + password + "'")):
                nigcon.commit()
                print("Welcome", username)
        else:
                print ("Incorrect Login, or your information is not in our database")
                print ""
                time.sleep(1)
                print ""
                print "Signing up is easy & Free!"
                print ""
                time.sleep(1)
                print "Please input your desired credit's"
                print ""
                time.sleep(1)
                username = raw_input("username: ")
                print(username)
                print("Are you sure you want this username")
                print ""
                raw_input("Yes or No: ")
                if Yes:
                        print "We need to register a password"
                        password = raw_input("Password: ")
                        print "Re-type your password: "
                        password1 = raw_input("Password: ")
                        if password1 == password:
                                print "Passwords Match"
                                print ("Registration Complete")
                                time.sleep(1)
                                print ("Welcome", username)
                                time.sleep(5)
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect((HOST, PORT))
                                s.sendall('Welcome to IG Network ')
                                data = s.recv(1024)
                                s.close()
                                print 'Received', repr(data)
                                print ''
                                print "Current Users Online"


loginmenu()
