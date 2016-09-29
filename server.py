#import socket module
from socket import *
import sys                                          # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = '192.168.0.5'
PORT = 4200

serverSocket.bind((HOST,PORT))
serverSocket.listen(1)

while True:

    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in start #Fill in end

    try:
        message = connectionSocket.recv(1024)       #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()                   #Fill in start #Fill in end

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:

        #Send response message for file not found

        #Fill in start
        #Fill in end

        #Close client socket

        #Fill in start
        #Fill in end

        serverSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data
