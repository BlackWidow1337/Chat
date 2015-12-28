# Purpose: Allows admins to control users in the network, it gives them a variety of commands based on modules coded up
# Author Zachary aka BlackWidow



import time
import MySQLdb


# Checks the database to see if the ip registered to the admin account matches the user trying to connect.

admincommands = ["/meatspin"]


def ipcheck():
    nigcon = MySQLdb.connect("localhost", "root""", "", "igtest")
    cursor = nigcon.cursor()
    if(nigcon):
        print "Connected to Admin Command Server"
        print ""
        time.sleep(1)
        from urllib2 import urlopen
        my_ip = urlopen('http://ip.42.pl/raw').read()
        print("Checking IP Address...")
        time.sleep(4)
        cursor.execute ("select IP from user_pwd")
        my_ip1 = cursor.fetchone()
        for my_ip1 in my_ip1:
            print("IP Address Resolved")
            print ("")
            print (my_ip1)
        nigcon.commit()
        if(my_ip == my_ip1):
            print("")
            print("IP's Match")
            print("")
            print("Please Login with your admin information")
        else:
            print("You're not authorized to use this client")

ipcheck()


#if(Admin Level < 0 )
#nigcon = """CREATE TABLE USER (
       # username CHAR(20) NOT NULL,
       # password CHAR(20) )"""
