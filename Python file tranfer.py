import socket
import threading
import os
import operator
import sys

#File tranfer server
def file_tranfer_server():
    os.system('cls')
    os.system('color a')
    print(' _____  ____  _        ___      ______  ____    ____  ____   _____  ___  ____        _____   ___  ____  __ __    ___  ____')
    print('|     ||    || |      /  _]    |      ||    \  /    ||    \ |     |/  _]|    \      / ___/  /  _]|    \|  |  |  /  _]|    \ ')
    print('|   __| |  | | |     /  [_     |      ||  D  )|  o  ||  _  ||   __/  [_ |  D  )    (   \_  /  [_ |  D  )  |  | /  [_ |  D  )')
    print('|  |_   |  | | |___ |    _]    |_|  |_||    / |     ||  |  ||  |_|    _]|    /      \__  ||    _]|    /|  |  ||    _]|    / ')
    print('|   _]  |  | |     ||   [_       |  |  |    \ |  _  ||  |  ||   _]   [_ |    \      /  \ ||   [_ |    \|  :  ||   [_ |    \ ')
    print('|  |    |  | |     ||     |      |  |  |  .  \|  |  ||  |  ||  | |     ||  .  \     \    ||     ||  .  \\   / |     ||  .  \ ')
    print('|__|   |____||_____||_____|      |__|  |__|\_||__|__||__|__||__| |_____||__|\_|      \___||_____||__|\_| \_/  |_____||__|\_|')
    print('\n')



    serverPort = int(input('Enter host port: '))

    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(('',serverPort)) 

    serverSocket.listen(2) #accepting up to 2 incoming connections

    print ('Server listening...')
    print (socket.gethostbyname(socket.gethostname()))

    while True:

        #return value of accept() is assigned to socket object
        #and address bound to that socket
        connectionSocket, addr = serverSocket.accept()
        
        #connection established with client
        print ('Got connection from', addr)

        #waiting for GET or SEND command from client
        print ('Awaiting command from client...')
        client_request = connectionSocket.recv(1024)
        #convert from byte object so we can read as string
        request_str = client_request.decode("utf-8")


        #server receives GET command from client and reads from file to be sent back
        #to client after they input the filename
        if request_str == 'GET':
            print('Received GET command from client. Waiting for filename.')

            client_request = connectionSocket.recv(1024)        


            file_name = client_request.decode("utf-8")

            f = open(file_name, "rb")
            print('Sending file...')
            l = f.read(1024)
            while(l):
                connectionSocket.send(l)
                l = f.read(1024)
            f.close()
            print('Done sending')

        #server receives SEND command from client and creates file to be received
        #by the client
        elif request_str == 'SEND':
            print('Received SEND command from client. Awaitng filename')
            client_request = connectionSocket.recv(1024)
            file_name = client_request.decode("utf-8")

            f = open(file_name, "wb")
            print('Receiving file from client..')
            l = connectionSocket.recv(1024)
            while(l):
                f.write(l)
                l = connectionSocket.recv(1024)
            f.close()
            print('Done receiving file')

        connectionSocket.close()  
#End File tranfer sevrer

#file tranfer client
def file_tranfer_client():
    os.system('cls')
    os.system('color a')
    print(' _____  ____  _        ___      ______  ____    ____  ____   _____  ___  ____          __  _      ____    ___  ____   ______')
    print('|     ||    || |      /  _]    |      ||    \  /    ||    \ |     |/  _]|    \        /  ]| |    |    |  /  _]|    \ |      |')
    print('|   __| |  | | |     /  [_     |      ||  D  )|  o  ||  _  ||   __/  [_ |  D  )      /  / | |     |  |  /  [_ |  _  ||      |')
    print('|  |_   |  | | |___ |    _]    |_|  |_||    / |     ||  |  ||  |_|    _]|    /      /  /  | |___  |  | |    _]|  |  ||_|  |_|')
    print('|   _]  |  | |     ||   [_       |  |  |    \ |  _  ||  |  ||   _]   [_ |    \     /   \_ |     | |  | |   [_ |  |  |  |  |')
    print('|  |    |  | |     ||     |      |  |  |  .  \|  |  ||  |  ||  | |     ||  .  \    \     ||     | |  | |     ||  |  |  |  |')
    print('|__|   |____||_____||_____|      |__|  |__|\_||__|__||__|__||__| |_____||__|\_|     \____||_____||____||_____||__|__|  |__|')
    print('\n')





    serverName = input('Enter server IP: ')
    serverPort = int(input('Enter port number: '))


    #in this loop, sockets open and close for each request the client makes
    while True:

        #create socket object for client
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        clientSocket.connect((serverName,serverPort))
        print('Connected to server.')

        sentence = input('Enter a GET or SEND command:')

        clientSocket.send(sentence.encode('utf-8'))

        fileName = input('\nEnter name of file: ')

        clientSocket.send(fileName.encode('utf-8'))
        if sentence == 'GET':
            f = open(fileName, "wb")
            print('Receiving file..')
            l = clientSocket.recv(1024)
            while (l):
                f.write(l)
                l = clientSocket.recv(1024)
            f.close()
            print('Done receiving file')

        elif sentence == 'SEND':
            f = open(fileName,"rb")

            print('Sending file to server...')
            l = f.read(1024)
            while (l):
                clientSocket.send(l)
                l = f.read(1024)
            f.close()
            print('Done sending')

        clientSocket.close()
#End File tranfer Client

def cmd():
    os.system('cls')
    os.system('color a')
    os.system('title PTVC')
#function call statement

def call():
    cmd()
    print('_________________________   _____________')
    print('\______   \__    ___/\   \ /   /\_   ___ \ ')
    print(' |     ___/ |    |    \   Y   / /    \  \/')
    print(' |    |     |    |     \     /  \     \____')
    print(' |____|     |____|      \___/    \______  /')
    print('                                        \/')
    print('')
    print('Python File Tranfer project Develop By Karibura')
    print('')
    print('1.File tranfer server \n2.File tranfer client\n3.Exit')
    i = int(input("Enter Number: "))
    print('\n')
    if i == 1:
       file_tranfer_server()
    elif i == 2:
       file_tranfer_client()
    elif i == 3:
        exit()
    else:
        print('please Enter a number')
    


call()

#end function call statement
