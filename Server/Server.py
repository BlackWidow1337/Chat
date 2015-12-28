# Edited and redesigned from https://docs.python.org/2/library/socket.html
# Echo server program

import socket
import MySQLdb
import time
online = 1

print "Server is Online waiting users"
HOST = '' # Symbolic name meaning all available interfaces
PORT = 1010             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # Bind the host and port together
s.listen(4) # Listen for the connection
conn, addr = s.accept() # allow connection for the address
print("Press Enter to start the server")
talk = raw_input("Send: ")

#print "Current Users Online", online
i = True

while i is True:
    if(s.accept):
        nigcon = MySQLdb.connect("localhost", "root", "", "igtest")
        cursor = nigcon.cursor()
        cursor.execute("select name from user_pwd") # Select the name of the user from user_pwd
        username = cursor.fetchone()
        print username, "Has Joined"
        print 'Connected On', addr
        while True:
            databytes = conn.recv(1024) #T
            if not databytes: # What is says m8
                break
            data = databytes.decode('utf-8') # the variable data is going  ever message is being sent from the client, and it's being decoded
            print ''
            print username, data  # Prints the recieved data from the client
#            message = raw_input(">")
#            conn.send(message)
#            print conn.recv(1024)

conn.close()
#        while 1:
#            data = conn.recv(2000) #recieving the data?
#            if not data:
#                break
#            conn.sendall(data)
#conn.close()