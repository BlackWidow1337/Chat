# Create Commands
# Author Zachary aka BlackWidow



import time
import sys
import MySQLdb


adminlevel = ("select adminlvl from user_pwd")

def amenu():
    nigcon = MySQLdb.connect("localhost","root","","igtest" )
    cursor = nigcon.cursor()
    if(nigcon):
        print "Connected to Admin Command Server"
        print ""
        print "To see a list of commands type /help"
        input = raw_input("")
        #if(adminlevel > 1 ):
        for adminlevel in adminlevel:
            print (adminlevel)
            cursor.fetchone()
            print(adminlevel)
            print("You're admin level is greater then 1")

amenu()






#if(Admin Level < 0 )
#nigcon = """CREATE TABLE USER (
       # username CHAR(20) NOT NULL,
       # password CHAR(20) )"""

#cursor.execute(nigcon)
#time.sleep(10)
#print "Creating Tables"
#time.sleep(1)
#print "Tables Created"
