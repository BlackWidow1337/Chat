import socket

host = '127.0.0.1'
port = 1010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
Message = raw_input("Send: ")
s.sendall(Message.encode('utf-8'))

while True:
    response = raw_input("Send: ")  #Send what ever is typed to be encoded
    s.sendall(response.encode('utf-8')) #is the message being sent to the server
    # Now we need to recieve the message from the server
s.close()
